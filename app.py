import streamlit as st
import fitz  # PyMuPDF

st.title("📄 PDF Reader System")

uploaded_files = st.file_uploader(
    "Upload your PDF files",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    for file in uploaded_files:
        st.write(f"### 📄 {file.name}")

        # Read PDF
        pdf = fitz.open(stream=file.read(), filetype="pdf")

        text = ""
        for page in pdf:
            text += page.get_text()

        # Show content
        st.text_area("Content", text, height=200)
