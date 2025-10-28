import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv
import matplotlib.pyplot as plt
from collections import Counter
import re

# Load environment variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="AI Recruitment Insights Dashboard", page_icon="📈", layout="wide")

st.title("📈 AI Recruitment Insights Dashboard")
st.markdown("Enhancing the AI Recruitment Assistant with data-driven insights and visual analytics.")

# Input: Job Description
job_description = st.text_area("📄 Enter Job Description", height=180, placeholder="Paste the job description here...")

# Input: Multiple resumes
resumes_input = st.text_area("👥 Enter Resumes (one per line or blank line separated)", height=200)

if st.button("🚀 Generate Insights"):
    if not job_description or not resumes_input:
        st.warning("Please provide both job description and resumes.")
    else:
        resumes = [r.strip() for r in resumes_input.split("\n\n") if r.strip()]
        scores, keywords_all = [], []
        insights = []

        with st.spinner("Analyzing resumes and generating insights... ⏳"):
            for resume in resumes:
                prompt = f"""
                Evaluate how this resume matches the given job description.
                Provide:
                - Match score (0-100)
                - Key matched skills or keywords
                - Short summary (2 sentences)
                
                Job Description:
                {job_description}

                Resume:
                {resume}
                """
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "You are an AI recruitment analyst."},
                        {"role": "user", "content": prompt}
                    ]
                )
                output = response.choices[0].message.content.strip()

                # Extract match score and keywords
                score = 0
                for line in output.split("\n"):
                    if "score" in line.lower():
                        try:
                            score = int(''.join([c for c in line if c.isdigit()]))
                        except:
                            score = 0

                keywords = re.findall(r'\b[A-Za-z]+\b', output)
                keywords_all.extend(keywords)
                scores.append(score)
                insights.append(output)

        # Keyword Frequency
        common_keywords = Counter([k.lower() for k in keywords_all if len(k) > 3]).most_common(10)

        # Display Results
        st.subheader("📊 Candidate Match Summary")
        for i, res in enumerate(insights):
            st.markdown(f"**Resume {i+1} — Match Score: {scores[i]}**")
            st.write(res)
            st.markdown("---")

        # Visualization — Scores
        st.subheader("🎯 Resume Match Scores")
        fig, ax = plt.subplots()
        ax.bar([f"Resume {i+1}" for i in range(len(scores))], scores, color='teal')
        ax.set_ylabel("Match Score (%)")
        st.pyplot(fig)

        # Visualization — Keyword Frequency
        st.subheader("🔑 Common Keywords Across Resumes")
        if common_keywords:
            words, counts = zip(*common_keywords)
            fig2, ax2 = plt.subplots()
            ax2.barh(words, counts, color='orange')
            ax2.set_xlabel("Frequency")
            st.pyplot(fig2)

        # AI Summary of Pool
        pool_prompt = f"""
        Summarize the overall candidate pool based on the following data:
        - Scores: {scores}
        - Common keywords: {common_keywords}
        Give a 3-sentence professional summary with recommendations for the recruiter.
        """
        pool_summary = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a recruitment strategist."},
                {"role": "user", "content": pool_prompt}
            ]
        ).choices[0].message.content.strip()

        st.subheader("📘 AI Summary of Candidate Pool")
        st.write(pool_summary)
