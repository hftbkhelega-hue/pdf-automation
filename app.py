import streamlit as st

st.title("📄 PDF Upload System")

uploaded_files = st.file_uploader(
    "Upload your PDF files",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    st.write("### Uploaded Files:")
    for file in uploaded_files:
        st.write(file.name)
