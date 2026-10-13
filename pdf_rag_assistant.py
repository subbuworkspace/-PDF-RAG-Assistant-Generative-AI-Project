```python
# ============================================================
# PDF RAG Assistant
# Technologies: Python, Gradio, LangChain, OpenAI, FAISS
# ============================================================

# Install dependencies:
# python -m pip install gradio langchain langchain-classic
# python -m pip install langchain-community langchain-openai
# python -m pip install langchain-text-splitters pypdf faiss-cpu

import os
import gradio as gr

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_classic.chains import RetrievalQA


# ============================================================
# Global QA Chain
# ============================================================

qa_chain = None


# ============================================================
# 1. Process Uploaded PDF
# ============================================================

def process_pdf(pdf_file):
    global qa_chain
    qa_chain = None

    if not pdf_file:
        return "❌ Please upload a PDF file."

    if not os.path.isfile(pdf_file):
        return "❌ The uploaded PDF file could not be found."

    if not os.getenv("OPENAI_API_KEY"):
        return "❌ Please configure your OPENAI_API_KEY."

    try:
        # Load PDF
        loader = PyPDFLoader(pdf_file)
        documents = loader.load()

        if not documents:
            return "❌ No pages were found in the PDF."

        # Split document into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

        chunks = text_splitter.split_documents(documents)

        # Validate extracted text
        if not chunks or not any(
            chunk.page_content.strip() for chunk in chunks
        ):
            return (
                "❌ No readable text was extracted. "
                "Scanned PDFs may require OCR."
            )

        # Generate embeddings
        embeddings = OpenAIEmbeddings(
            model="text-embedding-3-small"
        )

        # Create FAISS vector database
        vectorstore = FAISS.from_documents(
            chunks,
            embeddings
        )

        # Create retriever
        retriever = vectorstore.as_retriever(
            search_kwargs={"k": 5}
        )

        # Initialize language model
        llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0
        )

        # Build Retrieval QA chain
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=True
        )

        return f"""
## ✅ PDF Processed Successfully!

- **Pages:** {len(documents)}
- **Text chunks:** {len(chunks)}
- **Vector database:** FAISS
- **Embedding model:** text-embedding-3-small
- **Chat model:** gpt-4o-mini

You can now ask questions about your PDF.
"""

    except Exception as e:
        qa_chain = None
        return f"❌ Processing error: {type(e).__name__}: {e}"


# ============================================================
# 2. Ask Questions About the PDF
# ============================================================

def ask_pdf(question):
    global qa_chain

    if qa_chain is None:
        return "⚠️ Please upload and process a PDF first."

    if not question or not question.strip():
        return "⚠️ Please enter a question."

    try:
        response = qa_chain.invoke({
            "query": question.strip()
        })

        answer = response.get(
            "result",
            "No answer was returned."
        )

        source_documents = response.get(
            "source_documents",
            []
        )

        # Collect unique source page numbers
        pages = set()

        for doc in source_documents:
            page = doc.metadata.get("page")

            if page is not None:
                # PyPDFLoader page numbering starts from zero
                pages.add(int(page) + 1)

        # Append page references
        if pages:
            page_list = ", ".join(
                str(page) for page in sorted(pages)
            )

            answer += (
                "\n\n---\n"
                f"📄 **Source pages:** {page_list}"
            )

        return answer

    except Exception as e:
        return f"❌ Question error: {type(e).__name__}: {e}"


# ============================================================
# 3. Gradio User Interface
# ============================================================

with gr.Blocks(title="PDF RAG Assistant") as demo:

    gr.Markdown(
        """
        # 📚 PDF RAG Assistant

        Upload a PDF, process its content, and ask questions.

        **Workflow:** PDF → Text Splitting → Embeddings →
        FAISS → Retriever → LLM Answer
        """
    )

    # PDF upload
    pdf_file = gr.File(
        label="📄 Upload PDF",
        file_types=[".pdf"],
        type="filepath"
    )

    process_button = gr.Button(
        "🚀 Process PDF",
        variant="primary"
    )

    status = gr.Markdown()

    process_button.click(
        fn=process_pdf,
        inputs=[pdf_file],
        outputs=[status]
    )

    gr.Markdown("---")

    # Question input
    question = gr.Textbox(
        label="💬 Ask a Question",
        placeholder="Example: Summarize this PDF.",
        lines=2
    )

    ask_button = gr.Button(
        "🔍 Ask PDF",
        variant="primary"
    )

    answer = gr.Markdown()

    # Ask using button
    ask_button.click(
        fn=ask_pdf,
        inputs=[question],
        outputs=[answer]
    )

    # Ask by pressing Enter
    question.submit(
        fn=ask_pdf,
        inputs=[question],
        outputs=[answer]
    )


# ============================================================
# 4. Launch Application
# ============================================================

if __name__ == "__main__":
    demo.launch()
```
