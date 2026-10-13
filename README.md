# 📚 PDF RAG Assistant | Generative AI Project

A **Retrieval-Augmented Generation (RAG)** application that allows users to upload PDF documents and ask questions about their content. It retrieves relevant text from the PDF and uses an LLM to generate context-aware answers with source-page references.

## 🚀 Project Overview

This project combines document processing, vector search, and Large Language Models (LLMs) to create an interactive PDF question-answering system.

Instead of manually searching through a lengthy document, users can upload a PDF and ask questions in natural language.

## ✨ Key Features

- 📄 Upload and process PDF documents
- ✂️ Split document text into smaller chunks
- 🧠 Generate embeddings using OpenAI
- 🗄️ Store and search vectors using FAISS
- 🔍 Retrieve the most relevant document chunks
- 🤖 Generate answers using OpenAI's chat model
- 📌 Display source-page references
- 🌐 Interactive web interface built with Gradio

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Gradio | Web-based user interface |
| LangChain | RAG pipeline orchestration |
| PyPDF | PDF text extraction |
| RecursiveCharacterTextSplitter | Text chunking |
| OpenAI Embeddings | Text vectorization |
| FAISS | Vector storage and similarity search |
| GPT-4o mini | Context-aware answer generation |

## 🏗️ Project Architecture

```text
          PDF Document
               |
               v
         PyPDFLoader
               |
               v
        Text Extraction
               |
               v
        Text Splitting
               |
               v
       OpenAI Embeddings
               |
               v
         FAISS Vector DB
               |
               v
         User Question
               |
               v
       Similarity Search
               |
               v
       Relevant Text Chunks
               |
               v
         GPT-4o mini
               |
               v
      Answer + Source Pages
```

## 📂 Repository Structure

```text
PDF-RAG-Assistant/
│
├── pdf_rag_assistant.py
├── requirements.txt
├── README.md
├── .gitignore
└── screenshots/
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/PDF-RAG-Assistant.git
cd PDF-RAG-Assistant
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure your OpenAI API key

Windows Command Prompt:

```cmd
set OPENAI_API_KEY=your_api_key_here
```

PowerShell:

```powershell
$env:OPENAI_API_KEY="your_api_key_here"
```

**Security:** Never upload your API key to GitHub. OpenAI API access may incur separate charges.

### 5. Run the application

```bash
python pdf_rag_assistant.py
```

Open the local Gradio URL displayed in your terminal, usually:

`http://127.0.0.1:7860`

## 💡 How Does RAG Work?

**RAG stands for Retrieval-Augmented Generation.**

It combines two important processes:

1. **Retrieval:** Searches the document for text relevant to the user's question.
2. **Generation:** Uses an LLM to generate an answer based on the retrieved text.

In this project, FAISS retrieves up to five relevant chunks, which are passed to the language model to generate a response.

### Important Parameters

- `chunk_size=1000`: Splits text into chunks of approximately 1,000 characters.
- `chunk_overlap=200`: Preserves some context between consecutive chunks.
- `search_kwargs={"k": 5}`: Retrieves up to five relevant chunks.
- `temperature=0`: Encourages consistent, less-random responses.

## 🧪 Example Questions

After uploading a PDF, try asking:

- Summarize this document.
- What are the main findings?
- Explain the key concepts discussed in this PDF.
- What risks or challenges are mentioned?
- Which pages discuss a particular topic?

## 📌 Example Output

**Question:** What are the main findings of this report?

**Answer:** The assistant generates a response based on relevant retrieved passages from the uploaded PDF.

**Source Pages:** 2, 5, 8

*Illustrative example only; actual answers and page references depend on the uploaded document.*

## 🔐 Limitations and Security

- Scanned PDFs may require OCR because this version extracts selectable text.
- Answer quality depends on document quality and retrieval relevance.
- The application requires a valid OpenAI API key and API access.
- Uploaded document text is sent to the configured OpenAI API for embeddings and answer generation.
- The current global QA chain is intended for a learning project, not isolated multi-user sessions.

## 🔮 Future Improvements

- Support multiple PDF documents
- Add OCR for scanned documents
- Display retrieved text snippets alongside page references
- Add conversation history
- Add persistent vector storage
- Implement session-based user isolation
- Evaluate retrieval accuracy and answer quality

## 🎯 Learning Outcomes

Through this project, I explored:

- Retrieval-Augmented Generation (RAG)
- Document loading and text preprocessing
- Text embeddings and vector databases
- Semantic similarity search
- LLM-based question answering
- Building an interactive AI application with Gradio

## 👨‍💻 Author

**Subrata Mondal**

Data lead | Machine Learning | Generative AI | RAG Applications

---

⭐ If you find this project useful, consider starring the repository!

#GenerativeAI #RAG #LangChain #Python #FAISS #OpenAI #MachineLearning
