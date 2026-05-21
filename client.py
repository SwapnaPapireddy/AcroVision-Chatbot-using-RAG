import os

from huggingface_hub import InferenceClient


# =========================================================
# LOAD CLIENT
# =========================================================

client = InferenceClient(

    token=os.getenv("HF_TOKEN")
)


# =========================================================
# CHAT FUNCTION
# =========================================================

def hf_chat(prompt: str) -> str:

    response = client.chat_completion(

        messages=[

            {
                "role": "system",
                "content": (
                    "You are AgroVision AI, "
                    "an agriculture assistant chatbot."
                )
            },

            {
                "role": "user",
                "content": prompt
            }
        ],

        model="HuggingFaceH4/zephyr-7b-beta",

        max_tokens=300,

        temperature=0.3
    )

    return response.choices[0].message.content