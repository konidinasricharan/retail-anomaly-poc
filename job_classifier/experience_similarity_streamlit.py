import streamlit as st
from experience_similarity import experience_similarity

st.set_page_config(
    page_title="Experience Similarity Scoring",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Resume–Job Experience Similarity")
st.markdown(
    "Measures how closely resume experience matches a job description using TF-IDF similarity."
)

col1, col2 = st.columns(2)

with col1:
    resume_text = st.text_area(
        "📝 Resume Experience",
        height=300,
        placeholder="Paste resume experience section here..."
    )

with col2:
    job_text = st.text_area(
        "📄 Job Description",
        height=300,
        placeholder="Paste job description here..."
    )

if st.button("🔍 Calculate Experience Match"):
    if not resume_text or not job_text:
        st.warning("Please fill in both fields.")
    else:
        score = experience_similarity(resume_text, job_text)

        st.success(f"Experience Match Score: **{score}%**")

        st.progress(score / 100)
