import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import spacy
import io

st.set_page_config(page_title="Resume Comparison Dashboard", layout="wide")

st.title("📊 AI Resume Comparison Dashboard")
st.write("Upload multiple resumes to compare skill coverage and match scores.")

nlp = spacy.load("en_core_web_sm")

# Predefined skill list
skills = ["machine learning", "python", "data analysis", "nlp", "streamlit", 
          "sql", "pandas", "scikit-learn", "ai", "deep learning"]

uploaded_files = st.file_uploader("Upload multiple resumes (.txt only)", 
                                  accept_multiple_files=True, type=["txt"])

if uploaded_files:
    results = []
    
    for file in uploaded_files:
        text = file.read().decode("utf-8").lower()
        doc = nlp(text)
        extracted = [token.text for token in doc if token.text in skills]
        coverage = [1 if skill in extracted else 0 for skill in skills]
        score = round(sum(coverage) / len(skills) * 100, 2)
        results.append({"Candidate": file.name.replace(".txt", ""), "Score": score, **dict(zip(skills, coverage))})

    df = pd.DataFrame(results)
    
    st.subheader("📈 Skill Comparison Table")
    st.dataframe(df.set_index("Candidate"))

    st.subheader("🔥 Skill Coverage Heatmap")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(df.set_index("Candidate")[skills], annot=True, cmap="YlGnBu", cbar=False, ax=ax)
    plt.title("Skill Presence by Candidate")
    st.pyplot(fig)

    st.subheader("🏆 Comparison Scores")
    st.bar_chart(df.set_index("Candidate")["Score"])

    best_candidate = df.sort_values("Score", ascending=False).iloc[0]["Candidate"]
    st.success(f"✅ Best match: **{best_candidate}** ({df['Score'].max()}%)")

else:
    st.info("Upload multiple TXT resumes to begin comparison.")
