import streamlit as st
from openai import OpenAI
import os, pandas as pd, matplotlib.pyplot as plt
from dotenv import load_dotenv
import re

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="AI Shortlisting Assistant", page_icon="🤖", layout="wide")

st.title("🤖 AI Shortlisting & Job Fit Explanation")
st.markdown("Automatically shortlists best-fit candidates with reasoning & exportable shortlist.")

# Inputs
job_desc = st.text_area("📄 Job Description", height=180)
resumes_input = st.text_area("👥 Paste Resumes (blank-line separated)", height=200)
threshold = st.slider("🎯 Minimum Match Score for Shortlist", 60, 100, 75)

if st.button("🚀 Generate Shortlist"):
    if not job_desc or not resumes_input:
        st.warning("Please fill in both fields.")
    else:
        resumes = [r.strip() for r in resumes_input.split("\n\n") if r.strip()]
        results = []

        with st.spinner("Evaluating candidates..."):
            for idx, resume in enumerate(resumes, start=1):
                prompt = f"""
                Evaluate the following resume for this job description:
                Job Description:
                {job_desc}
                Resume:
                {resume}

                Provide:
                - Overall Match Score (0-100)
                - 3 bullet strengths
                - 2 bullet areas of improvement
                - A 2-sentence explanation of why this candidate fits or doesn't fit.
                """

                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "You are an AI recruitment strategist."},
                        {"role": "user", "content": prompt}
                    ]
                ).choices[0].message.content.strip()

                # --- Clean Score Extraction ---
                score = 0
                match = re.search(r'(\b\d{1,3})\s*/?\s*100', response)  # looks for "85", "85/100", "Score: 85"
                if match:
                    score = int(match.group(1))
                else:
                    # fallback if no "100" pattern found
                    digits = re.findall(r'\d{1,3}', response)
                    if digits:
                        score = int(digits[0])

                # Always format display as "XX/100"
                score_str = f"{score}/100"

                results.append({
                    "Resume ID": f"Resume {idx}",
                    "Score": score,
                    "Score Display": score_str,
                    "AI Analysis": response
                })

        # --- DataFrame & Visualization ---
        df = pd.DataFrame(results).sort_values("Score", ascending=False)
        st.subheader("📊 Candidate Evaluation Results")
        st.dataframe(df[["Resume ID", "Score Display"]])

        # Visualization
        fig, ax = plt.subplots()
        ax.bar(df["Resume ID"], df["Score"], color="teal")
        ax.axhline(y=threshold, color='r', linestyle='--', label=f"Threshold: {threshold}")
        ax.set_ylabel("Match Score (%)")
        ax.set_title("Candidate Fit Distribution")
        ax.legend()
        st.pyplot(fig)

        # Shortlisted candidates
        shortlisted = df[df["Score"] >= threshold]
        st.subheader("✅ Shortlisted Candidates")
        st.dataframe(shortlisted[["Resume ID", "Score Display"]])

        # Reasoning section
        st.subheader("🧠 AI Reasoning for Shortlist")
        for _, row in shortlisted.iterrows():
            st.markdown(f"### {row['Resume ID']} – Score: {row['Score Display']}")
            st.write(row["AI Analysis"])
            st.markdown("---")

        # Export shortlist
        shortlisted.to_csv("shortlisted_candidates.csv", index=False)
        st.success("✅ Exported → shortlisted_candidates.csv")

        # Recruiter summary
        summary_prompt = f"""
        Based on these shortlisted candidates:
        {shortlisted.to_dict()}
        Provide a 5-sentence recruiter summary covering:
        - Key strengths of the top candidates.
        - How well the overall pool aligns with the job.
        - Hiring recommendation.
        """
        summary = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Professional recruiter"},
                {"role": "user", "content": summary_prompt}
            ]
        ).choices[0].message.content.strip()

        st.subheader("💬 Recruiter Summary & Recommendation")
        st.write(summary)
