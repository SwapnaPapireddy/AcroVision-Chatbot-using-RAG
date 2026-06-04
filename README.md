# 🌾 AgroVision AI Chatbot

An intelligent AI-powered Agriculture Assistant built using Retrieval-Augmented Generation (RAG), FAISS, Streamlit, and Large Language Models that provides farming guidance, crop recommendations, irrigation information, fertilizer suggestions, and answers agriculture-related questions by retrieving information from agricultural knowledge-base documents.

---

## 🌐 Project Overview

Farmers and agriculture enthusiasts often struggle to find reliable and instant information regarding crops, irrigation techniques, soil management, fertilizers, pest control, and seasonal farming practices.

AgroVision AI solves this problem by combining Large Language Models with Retrieval-Augmented Generation (RAG) to provide accurate, context-aware, and document-grounded agricultural assistance.

The system retrieves information from agricultural PDF documents and uses AI to generate meaningful responses for user queries.

---

# 🌐 Live Demo

🔗 [AgroVision AI Chatbot](https://huggingface.co/spaces/swapnapapireddy3/AcroVision-chatbot)

## 🎯 Objectives

* Provide instant agriculture-related guidance
* Build a document-based agriculture knowledge assistant
* Implement Retrieval-Augmented Generation (RAG)
* Reduce dependency on manual document searching
* Improve accessibility of farming information
* Enable intelligent question answering using PDFs

---

## ✨ Features

* 🌾 Agriculture Knowledge Assistant
* 📄 PDF-Based Knowledge Retrieval
* 🔍 Semantic Search using FAISS
* 🧠 AI-Powered Question Answering
* 🚜 Crop and Farming Guidance
* 💧 Irrigation Recommendations
* 🌱 Fertilizer and Soil Management Suggestions
* 📚 Multi-PDF Knowledge Base Support
* 💬 Interactive Chat Interface
* ⚡ Fast Document Retrieval
* 🔐 Environment Variable Security

---

## 🏗️ System Workflow

User Question
│
▼
Streamlit Frontend
│
▼
Router Module
│
├── General Agriculture Query
│         │
│         ▼
│       LLM Response
│
└── Knowledge Base Query
│
▼
PDF Document Loader
│
▼
Text Chunking
│
▼
Embedding Generation
│
▼
FAISS Vector Store
│
▼
Relevant Retrieval
│
▼
Prompt Engineering
│
▼
LLM Generation
│
▼
Final Response

---

## ⚙️ How It Works

### 1️⃣ User Query

The user asks an agriculture-related question through the Streamlit chatbot interface.

Example:

* What fertilizer is suitable for rice?
* How can I improve soil fertility?
* What crops can be grown during monsoon?

---

### 2️⃣ Query Classification

The Router module classifies the query into:

* General Agriculture Query
* Knowledge Base Query

---

### 3️⃣ PDF Knowledge Processing

Agriculture PDF documents are loaded and processed.

The system:

* Extracts text from PDFs
* Splits content into smaller chunks
* Creates vector embeddings for each chunk

---

### 4️⃣ Vector Database Storage

The generated embeddings are stored inside FAISS.

FAISS enables:

* Similarity Search
* Fast Retrieval
* Semantic Search

---

### 5️⃣ Retrieval Process

When a query is received:

* Query is converted into an embedding
* FAISS finds the most relevant document chunks
* Relevant context is retrieved

---

### 6️⃣ Prompt Generation

Retrieved context and user question are combined into a structured prompt.

The prompt is sent to the Large Language Model.

---

### 7️⃣ AI Response Generation

The LLM generates a context-aware response using:

* Retrieved PDF content
* User question
* Conversation history

---

### 8️⃣ Final Output

The user receives an accurate and meaningful agriculture-related answer through the chatbot interface.

---

## 📊 Example Queries

### Crop Information

* What is the best season for paddy cultivation?
* Which crops grow well in black soil?

### Irrigation

* What is drip irrigation?
* Explain sprinkler irrigation.

### Fertilizers

* Which fertilizer is suitable for cotton crops?
* How much nitrogen is required for rice?

### Soil Management

* How can soil fertility be improved?
* What are organic farming methods?

---

## 🛠️ Tech Stack

| Component            | Technology              |
| -------------------- | ----------------------- |
| Frontend             | Streamlit               |
| LLM                  | Hugging Face / Ollama   |
| Embeddings           | SentenceTransformers    |
| Vector Database      | FAISS                   |
| PDF Processing       | PyPDF                   |
| Text Chunking        | LangChain Text Splitter |
| Prompt Engineering   | Custom Prompt Templates |
| Retrieval Framework  | RAG Pipeline            |
| Programming Language | Python                  |

---

## 📂 Project Structure

RAG_AGROVISION_PROJECT/

├── app.py

├── rag.py

├── embeddings.py

├── client.py

├── router.py

├── prompt.py

├── requirements.txt

├── .env

├── Acrovision_data.pdf

└── README.md

---

## 🚀 Installation & Setup

### 1️⃣ Clone Repository

git clone [https://github.com/your-username/agrovision-ai-chatbot.git](https://github.com/your-username/agrovision-ai-chatbot.git)

### 2️⃣ Navigate to Project

cd agrovision-ai-chatbot

### 3️⃣ Create Virtual Environment

python -m venv venv

### 4️⃣ Activate Environment

Windows:

venv\Scripts\activate

### 5️⃣ Install Dependencies

pip install -r requirements.txt

### 6️⃣ Configure Environment Variables

Create a .env file:

HF_TOKEN=your_huggingface_token

HF_CHAT_MODEL=meta-llama/Llama-3.1-8B-Instruct

### 7️⃣ Run Application

streamlit run app.py

---

## 🔮 Future Enhancements

* 🌦️ Weather API Integration
* 📍 Location-Based Crop Recommendations
* 📸 Plant Disease Detection
* 🎙️ Voice-Based Agriculture Assistant
* 🌐 Multi-Language Support
* ☁️ Cloud Deployment
* 📊 Agriculture Analytics Dashboard
* 🤖 Advanced RAG Pipeline

---

## ⚠️ Challenges Faced

* Extracting clean text from PDFs
* Chunk size optimization
* Embedding quality improvement
* Retrieval relevance tuning
* Prompt engineering for accurate responses
* Integrating FAISS with RAG workflow
* Managing hallucinations in LLM responses

---

## 📄 License

This project is developed for educational and learning purposes.

---

## 👨‍💻 Author

Swapna Papireddy

AI/ML Developer | Generative AI Enthusiast

You can directly use this as your `README.md` for the AgroVision AI Chatbot project.
