import streamlit as st
import pandas as pd
import spacy
import matplotlib.pyplot as plt

st.set_page_config(page_title="AI Resume Analyzer - Skill Scorer", layout="wide")

st.title("AI Resume Analyzer — Skill Extraction & Scoring Engine")
st.write("This enhanced tool automatically extracts key skills from resumes and generates a skill match score.")

nlp = spacy.load("en_core_web_sm")

# Skill database
required_skills = ["machine learning", "python", "data analysis", "nlp", "streamlit", "sql", "pandas", "scikit-learn", "ai", "deep learning"]

# Upload section
uploaded_file = st.file_uploader("Upload Resume (TXT file only)", type=["txt"])

if uploaded_file:
    text = uploaded_file.read().decode("utf-8")
    doc = nlp(text.lower())
    extracted = [token.text for token in doc if token.text in required_skills]
    
    score = round((len(set(extracted)) / len(required_skills)) * 100, 2)
    
    st.subheader("📋 Extracted Skills:")
    st.write(list(set(extracted)))
    
    st.subheader("📊 Skill Match Score:")
    st.metric("Score (%)", score)
    
    fig, ax = plt.subplots()
    ax.barh(required_skills, [1 if skill in extracted else 0 for skill in required_skills])
    ax.set_xlabel("Skill Presence (1=Yes)")
    ax.set_title("Skill Coverage Chart")
    st.pyplot(fig)
    
    st.success(f"✅ Resume Analysis Complete — Skill Match: {score}%")

else:
    st.info("Upload a TXT file containing resume text to analyze.")
