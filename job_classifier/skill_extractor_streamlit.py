import streamlit as st
from skill_extractor import extract_skills

st.set_page_config(
    page_title="AI Skill Extraction Engine",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI Skill Extraction Engine")
st.markdown("Extracts technical skills from job descriptions or resumes using NLP.")

text_input = st.text_area(
    "📄 Paste Job Description or Resume",
    height=250,
    placeholder="Paste text here..."
)

if st.button("🔍 Extract Skills"):
    if not text_input.strip():
        st.warning("Please paste some text.")
    else:
        skills = extract_skills(text_input)

        if not skills:
            st.info("No skills detected.")
        else:
            st.success("Skills extracted successfully!")

            for category, items in skills.items():
                st.subheader(category)
                st.write(", ".join(items))
