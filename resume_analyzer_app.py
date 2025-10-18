import streamlit as st
from transformers import pipeline
import re

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("🤖 AI Resume Analyzer")
st.write("Upload your resume text and see how strong it is for AI/ML-related keywords")

# Input
resume_text = st.text_area("Paste your resume text below:", height=300)

# Simple keyword sets
ai_keywords = ["machine learning", "deep learning", "neural network", "ai", "nlp", "transformer", "python", "data", "analytics", "research", "paper", "publication", "project", "github", "tensorflow", "pytorch"]
achievements = ["award", "grant", "recognition", "fellowship", "scholarship", "presentation", "conference", "innovation"]

if st.button("Analyze Resume"):
    if not resume_text.strip():
        st.warning("Please paste your resume text first.")
    else:
        text_lower = resume_text.lower()

        ai_score = sum(1 for kw in ai_keywords if kw in text_lower)
        achievement_score = sum(1 for kw in achievements if kw in text_lower)

        total_score = ai_score * 2 + achievement_score

        st.subheader("📊 Resume Analysis Results:")
        st.write(f"**AI Keywords Found:** {ai_score}")
        st.write(f"**Achievements Found:** {achievement_score}")

        # Basic advice
        if total_score < 10:
            st.error("⚠️ Needs Improvement: Add more AI/ML projects, technical keywords, and achievements.")
        elif total_score < 20:
            st.warning("🟡 Good Start: Add more measurable impact and leadership points.")
        else:
            st.success("✅ Strong Resume: You have good AI/ML alignment and supporting achievements!")

        # Display extracted keywords
        found_keywords = [kw for kw in ai_keywords + achievements if kw in text_lower]
        st.write("**Matched Keywords:**", ", ".join(found_keywords))
