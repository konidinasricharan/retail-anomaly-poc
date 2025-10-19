import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

st.set_page_config(page_title="AI Resume Analyzer Pro", page_icon="", layout="centered")

st.title(" AI Resume Analyzer — Enhanced Edition")

uploaded_file = st.file_uploader("📄 Upload your resume (TXT format preferred)", type=["txt"])

ai_keywords = [
    "artificial intelligence", "machine learning", "deep learning", "python",
    "pytorch", "tensorflow", "data analysis", "research", "neural network",
    "nlp", "computer vision", "autonomous", "predictive", "analytics",
    "openai", "llm", "transformer", "fine-tuning", "prompt", "ai"
]

achievements = [
    "led", "published", "awarded", "patent", "research", "developed",
    "presented", "innovated", "mentored", "recognized"
]

if uploaded_file:
    text = uploaded_file.read().decode("utf-8")
    text_lower = text.lower()

    # Count keyword frequency
    keyword_counts = {kw: text_lower.count(kw) for kw in ai_keywords if kw in text_lower}
    achievement_counts = {ach: text_lower.count(ach) for ach in achievements if ach in text_lower}

    df_keywords = pd.DataFrame(list(keyword_counts.items()), columns=["Keyword", "Count"])
    df_achievements = pd.DataFrame(list(achievement_counts.items()), columns=["Achievement", "Count"])

    st.subheader("📊 Keyword Frequency Visualization")
    if not df_keywords.empty:
        fig, ax = plt.subplots()
        df_keywords.plot(kind="barh", x="Keyword", y="Count", ax=ax, color="skyblue", legend=False)
        ax.set_xlabel("Frequency")
        ax.set_ylabel("AI Keywords")
        ax.set_title("AI Keyword Distribution in Resume")
        st.pyplot(fig)
    else:
        st.warning("No AI-related keywords found in the resume.")

    st.subheader("🏆 Achievement Keywords Found")
    st.dataframe(df_achievements)

    # Prepare downloadable report
    report_content = StringIO()
    report_content.write("AI Resume Analyzer Report\n\n")
    report_content.write("AI Keywords Found:\n")
    for kw, count in keyword_counts.items():
        report_content.write(f"{kw}: {count}\n")
    report_content.write("\nAchievements Found:\n")
    for ach, count in achievement_counts.items():
        report_content.write(f"{ach}: {count}\n")

    st.download_button(
        label="📥 Download Analysis Report (.txt)",
        data=report_content.getvalue(),
        file_name="resume_analysis_report.txt",
        mime="text/plain"
    )

else:
    st.info("👆 Please upload your resume to start analysis.")
