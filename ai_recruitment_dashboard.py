import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from openai import OpenAI
from dotenv import load_dotenv
import os

# Setup
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="AI Recruitment Analytics Dashboard", page_icon="📈", layout="wide")

st.title("📊 AI Recruitment Analytics Dashboard")
st.markdown("Analyze candidate evaluation data and visualize skill trends, match scores, and AI summaries.")

uploaded_file = st.file_uploader("📤 Upload your shortlisted_candidates.csv file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("📋 Uploaded Data Preview")
    st.dataframe(df)

    # Clean and prepare
    df["ScoreValue"] = df["Score"].astype(str).str.extract(r"(\d+)").astype(float)
    avg_score = df["ScoreValue"].mean()
    max_score = df["ScoreValue"].max()
    min_score = df["ScoreValue"].min()

    st.metric("📈 Average Score", f"{avg_score:.1f}/100")
    st.metric("🏆 Highest Score", f"{max_score:.0f}/100")
    st.metric("⚠️ Lowest Score", f"{min_score:.0f}/100")

    # Plot distribution
    st.subheader("🎯 Score Distribution")
    fig, ax = plt.subplots(figsize=(8,4))
    sns.barplot(x="Resume ID", y="ScoreValue", data=df, palette="coolwarm")
    plt.xticks(rotation=45)
    plt.title("Candidate Match Scores")
    st.pyplot(fig)

    # Keyword extraction from AI Analysis
    st.subheader("🧩 Common Strength Keywords (AI Insights)")
    all_text = " ".join(df["AI Analysis"].astype(str).tolist()).lower()
    common_words = pd.Series(all_text.split()).value_counts().head(15)
    st.bar_chart(common_words)

    # Recruiter summary generation
    if st.button("🧠 Generate AI Hiring Summary"):
        prompt = f"""
        Analyze the following shortlisted candidate data:
        {df.to_dict()}
        Provide:
        - Overall hiring readiness score (0-100)
        - 5 key strengths across the group
        - 3 major skill gaps observed
        - Final recruiter recommendation paragraph
        """

        summary = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert AI recruiter and HR analyst."},
                {"role": "user", "content": prompt}
            ]
        ).choices[0].message.content.strip()

        st.subheader("📄 AI Hiring Summary Report")
        st.write(summary)

        # Save report
        with open("ai_hiring_summary.txt", "w", encoding="utf-8") as f:
            f.write(summary)
        st.success("✅ AI Hiring Summary saved as ai_hiring_summary.txt")

else:
    st.info("Upload the shortlisted_candidates.csv file generated from your AI Shortlisting Assistant.")
