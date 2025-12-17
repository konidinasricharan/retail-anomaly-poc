import streamlit as st
import tempfile
from resume_parser import parse_resume_pdf
from skill_extractor import extract_skills

st.set_page_config(
    page_title="AI Resume Skill Extractor",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI Resume Skill Extraction")
st.markdown(
    "Upload a resume PDF → extract structured technical skills automatically."
)

uploaded_file = st.file_uploader(
    "📎 Upload Resume (PDF only)",
    type=["pdf"]
)

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    with st.spinner("Parsing resume and extracting skills..."):
        resume_text = parse_resume_pdf(tmp_path)
        skills = extract_skills(resume_text)

    st.success("Resume processed successfully!")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📝 Parsed Resume Text")
        st.text_area(
            "Resume Content",
            resume_text,
            height=400
        )

    with col2:
        st.subheader("🧩 Extracted Skills")
        if not skills:
            st.info("No skills detected.")
        else:
            for category, items in skills.items():
                st.markdown(f"**{category}**")
                st.write(", ".join(items))
