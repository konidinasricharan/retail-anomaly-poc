import streamlit as st
from openai import OpenAI
import os, csv
from dotenv import load_dotenv
import pandas as pd
import matplotlib.pyplot as plt

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="AI Resume Ranking System", page_icon="🏆", layout="wide")

st.title("AI Resume Ranking & Feedback System")
st.markdown("Ranks resumes, provides AI feedback, and exports results to CSV.")

# Inputs
job_desc = st.text_area("📄 Job Description", height=180)
resumes_input = st.text_area("👥 Paste Resumes (blank-line separated)", height=200)

if st.button("Rank & Generate Feedback"):
    if not job_desc or not resumes_input:
        st.warning("Please fill in both fields.")
    else:
        resumes = [r.strip() for r in resumes_input.split("\n\n") if r.strip()]
        results = []

        with st.spinner("Analyzing resumes..."):
            for idx, resume in enumerate(resumes, start=1):
                prompt = f"""
                Evaluate the following resume against the job description.
                Provide:
                - Match Score (0-100)
                - Strength Summary (2 sentences)
                - Personalized Improvement Advice (2 sentences)
                Job Description:
                {job_desc}
                Resume:
                {resume}
                """
                res = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "You are an AI recruitment expert."},
                        {"role": "user", "content": prompt}
                    ]
                ).choices[0].message.content.strip()

                # Parse score
                score = 0
                for line in res.split("\n"):
                    if "score" in line.lower():
                        digits = "".join([c for c in line if c.isdigit()])
                        if digits: score = int(digits)

                results.append({"Resume ID": f"Resume {idx}", "Score": score, "Feedback": res})

        # Sort & display
        df = pd.DataFrame(results).sort_values("Score", ascending=False)
        st.subheader("📊 Ranked Candidates")
        st.dataframe(df[["Resume ID", "Score"]])

        # Visualization
        fig, ax = plt.subplots()
        ax.bar(df["Resume ID"], df["Score"], color="seagreen")
        ax.set_ylabel("Match Score (%)")
        ax.set_title("Candidate Ranking Results")
        st.pyplot(fig)

        st.subheader("📝 Individual Feedback")
        for _, row in df.iterrows():
            st.markdown(f"### {row['Resume ID']} – Score: {row['Score']}")
            st.write(row["Feedback"])
            st.markdown("---")

        # Export CSV
        df.to_csv("resume_ranking_results.csv", index=False)
        st.success("✅ Results exported → resume_ranking_results.csv")

        # AI Summary
        summary_prompt = f"""
        Summarize this ranking:
        {df.to_dict()}
        Provide a 3-sentence recruiter recommendation and overview.
        """
        summary = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Recruitment strategist"},
                {"role": "user", "content": summary_prompt}
            ]
        ).choices[0].message.content.strip()

        st.subheader("💡 AI Recruiter Recommendation")
        st.write(summary)
