import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv
import matplotlib.pyplot as plt

# Load environment variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="AI Recruitment Assistant", page_icon="🤖", layout="wide")

st.title("🤖 AI Recruitment Assistant — Resume Matching System")
st.markdown("This tool ranks uploaded resumes against a given job description using GPT intelligence.")

# Input: Job Description
job_description = st.text_area("📄 Enter Job Description", height=200, placeholder="Paste the job description here...")

# Input: Multiple resumes
resumes_input = st.text_area("👥 Enter Resumes (one per line)", height=200, placeholder="Paste or list multiple resumes separated by a blank line.")

if st.button("🔍 Match Resumes"):
    if not job_description or not resumes_input:
        st.warning("Please provide both job description and resumes.")
    else:
        resumes = [r.strip() for r in resumes_input.split("\n") if r.strip()]
        results, scores, names = [], [], []

        with st.spinner("Analyzing resumes... please wait ⏳"):
            for i, resume in enumerate(resumes):
                prompt = f"""
                Compare this resume with the job description below.
                Give:
                - Match Score (0–100)
                - Short reasoning (2–3 sentences)

                Job Description:
                {job_description}

                Resume:
                {resume}
                """

                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "You are a professional AI recruiter assistant."},
                        {"role": "user", "content": prompt}
                    ]
                )
                output = response.choices[0].message.content.strip()
                results.append(output)

                # Extract score if present
                score_line = [line for line in output.split("\n") if "score" in line.lower()]
                score = 0
                if score_line:
                    try:
                        score = int(''.join([c for c in score_line[0] if c.isdigit()]))
                    except:
                        score = 0

                scores.append(score)
                names.append(f"Resume {i+1}")

        # Display results
        st.subheader("📊 Match Results")
        for i, res in enumerate(results):
            st.markdown(f"**{names[i]} — Score: {scores[i]}**")
            st.write(res)
            st.markdown("---")

        # Visualization
        st.subheader("🎯 Resume Match Comparison")
        fig, ax = plt.subplots()
        ax.bar(names, scores, color='teal')
        ax.set_ylabel("Match Score (%)")
        ax.set_title("AI Resume Match Ranking")
        st.pyplot(fig)
