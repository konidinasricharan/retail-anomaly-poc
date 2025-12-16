import streamlit as st
import tempfile
from resume_parser import parse_resume_pdf

st.set_page_config(
    page_title="AI Resume Parser",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Parsing Engine")
st.markdown("Upload a resume PDF to extract clean, usable text.")

uploaded_file = st.file_uploader(
    "📎 Upload Resume (PDF only)",
    type=["pdf"]
)

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    with st.spinner("Parsing resume..."):
        parsed_text = parse_resume_pdf(tmp_path)

    st.success("Resume parsed successfully!")

    st.subheader("📝 Extracted Resume Text")
    st.text_area(
        "Parsed Content",
        parsed_text,
        height=350
    )
