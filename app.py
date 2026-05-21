import os

import streamlit as st

from dotenv import load_dotenv

from langsmith import traceable

from router import classify_query
from rag import get_retriever
from client import hf_chat

from prompt import (
    general_prompt,
    agriculture_prompt,
    rag_prompt
)

# ---------------------------------------------------------
# LOAD ENV
# ---------------------------------------------------------

load_dotenv()

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------

st.set_page_config(
    page_title="AgroVision AI",
    page_icon="🌱"
)

st.title("🌾 AgroVision Chatbot")

st.markdown(
    """
    Welcome to AgroVision AI 🚜  
    """
)

# ---------------------------------------------------------
# SESSION STATE
# ---------------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------------------------------------------------
# LOAD RETRIEVER
# ---------------------------------------------------------

# ---------------------------------------------------------
# LOAD RETRIEVER
# ---------------------------------------------------------

if "retriever" not in st.session_state:

    try:

        # "." means current project folder
        st.session_state.retriever = get_retriever(
            "."
        )

        st.success(
            "Agriculture Knowledge Base Loaded 🌾"
        )

    except Exception as exc:

        st.session_state.retriever = None

        st.warning(
            f"RAG is not ready yet: {exc}"
        )

# ---------------------------------------------------------
# PROCESS QUERY
# ---------------------------------------------------------

@traceable(
    name="AgroVision Pipeline",
    run_type="chain"
)

def process_query(
    user_input,
    history_text,
    retriever
):

    route = classify_query(
        user_input
    )

    # ---------------------------------------------------------
    # GENERAL
    # ---------------------------------------------------------

    if route == "GENERAL":

        answer = hf_chat(
            general_prompt(
                user_input,
                history_text
            )
        )

        sources = []

    # ---------------------------------------------------------
    # AGRICULTURE PROBLEM
    # ---------------------------------------------------------

    elif route == "PROBLEM":

        answer = hf_chat(
            agriculture_prompt(
                user_input,
                history_text
            )
        )

        sources = []

    # ---------------------------------------------------------
    # RAG
    # ---------------------------------------------------------

    else:

        if retriever is None:

            answer = (
                "I could not load the agriculture PDF knowledge base."
            )

            sources = []

        else:

            docs = retriever.retrieve(
                user_input,
                top_k=5
            )

            context = "\n\n".join([

                f"[Source: {d['source']}, page {d['page']}]\n"
                f"{d['text']}"

                for d in docs
            ])

            answer = hf_chat(

                rag_prompt(
                    user_input,
                    history_text,
                    context
                )
            )

            sources = docs

    return route, answer, sources


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

with st.sidebar:

    st.header("Configuration")

    st.write(
        "Provider:",
        os.getenv(
            "HF_PROVIDER",
            "hf-inference"
        )
    )

    st.write(
        "Chat model:",
        os.getenv(
            "HF_CHAT_MODEL",
            "meta-llama/Llama-3.1-8B-Instruct"
        )
    )

    st.write(
        "Embedding model:",
        os.getenv(
            "HF_EMBEDDING_MODEL",
            "thenlper/gte-large"
        )
    )

    if st.button("Clear Chat History"):

        st.session_state.messages = []

        st.rerun()


# ---------------------------------------------------------
# DISPLAY CHAT HISTORY
# ---------------------------------------------------------

for msg in st.session_state.messages:

    with st.chat_message(
        msg["role"]
    ):

        st.markdown(
            msg["content"]
        )


# ---------------------------------------------------------
# USER INPUT
# ---------------------------------------------------------

user_input = st.chat_input(
    "Ask agriculture-related questions..."
)

# ---------------------------------------------------------
# PROCESS INPUT
# ---------------------------------------------------------

if user_input:

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    history_text = "\n".join([

        f'{m["role"]}: {m["content"]}'

        for m in st.session_state.messages[-8:]
    ])

    try:

        route, answer, sources = process_query(
            user_input=user_input,
            history_text=history_text,
            retriever=st.session_state.retriever
        )

        st.session_state.messages.append({

            "role": "assistant",
            "content": answer
        })

        with st.chat_message("assistant"):

            st.markdown(answer)

            # ---------------------------------------------------------
            # SOURCES
            # ---------------------------------------------------------

            if sources:

                with st.expander(
                    "Sources Used"
                ):

                    for i, doc in enumerate(
                        sources,
                        start=1
                    ):

                        st.markdown(
                            f"**{i}. {doc['source']} "
                            f"— page {doc['page']}**"
                        )

                        st.write(
                            doc["text"][:500] +
                            (
                                "..."
                                if len(doc["text"]) > 500
                                else ""
                            )
                        )

    except Exception as exc:

        err = f"Error: {exc}"

        st.session_state.messages.append({

            "role": "assistant",
            "content": err
        })

        with st.chat_message("assistant"):

            st.error(err)