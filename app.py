import streamlit as st
import requests

API_KEY = "K82622807788957"

st.title("📄 PDF OCR Reader")

uploaded_files = st.file_uploader(
    "Upload your PDF files",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    for file in uploaded_files:
        st.write(f"### 📄 {file.name}")

        response = requests.post(
            "https://api.ocr.space/parse/image",
            files={"file": file},
            data={
                "apikey": API_KEY,
                "language": "eng"
            }
        )

        result = response.json()

        try:
            text = result["ParsedResults"][0]["ParsedText"]
            st.text_area("Extracted Text", text, height=200)
        except:
            st.write("❌ Could not read PDF")
