import streamlit as st
from openai import OpenAI
import pandas as pd
from fpdf import FPDF
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="AI Resume Summary Generator", layout="wide")
st.title("🧠 AI Resume Summary Generator")
st.write("Upload a resume, and the AI will generate a concise professional summary with optional PDF export.")

uploaded_file = st.file_uploader("Upload Resume (TXT only)", type=["txt"])

if uploaded_file:
    resume_text = uploaded_file.read().decode("utf-8")
    
    with st.spinner("Generating summary using AI..."):
        prompt = f"""
        You are a professional career analyst. Summarize the following resume in a concise, impressive, professional tone.
        Focus on skills, achievements, and role fit in 4–6 sentences.

        Resume:
        {resume_text}
        """
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        summary = response.choices[0].message.content
    
    st.subheader("📝 AI-Generated Resume Summary")
    st.write(summary)
    
    # Save as PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, summary)
    pdf_output = uploaded_file.name.replace(".txt", "_summary.pdf")
    pdf.output(pdf_output)

    with open(pdf_output, "rb") as f:
        st.download_button(
            label="📥 Download Summary as PDF",
            data=f,
            file_name=pdf_output,
            mime="application/pdf",
        )
else:
    st.info("Upload a TXT resume to generate a professional summary.")
