import streamlit as st
from unified_score import calculate_unified_score

st.set_page_config(
    page_title="Unified Candidate Scoring",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Unified Candidate Scoring Engine")
st.markdown(
    "Combines **Skills**, **Experience**, and **AI Reasoning** into one final score."
)

col1, col2, col3 = st.columns(3)

with col1:
    skill_score = st.slider(
        "🧩 Skill Match Score (%)",
        0, 100, 70
    )

with col2:
    experience_score = st.slider(
        "📊 Experience Similarity Score (%)",
        0, 100, 75
    )

with col3:
    llm_score = st.slider(
        "🧠 LLM Reasoning Score (%)",
        0, 100, 80
    )

if st.button("🚀 Calculate Unified Score"):
    final_score = calculate_unified_score(
        skill_score,
        experience_score,
        llm_score
    )

    st.success(f"✅ Final Candidate Score: **{final_score}%**")

    st.progress(final_score / 100)

    st.markdown("### 🔍 Score Breakdown")
    st.write(f"- Skills Contribution: {skill_score * 0.4:.1f}")
    st.write(f"- Experience Contribution: {experience_score * 0.4:.1f}")
    st.write(f"- LLM Contribution: {llm_score * 0.2:.1f}")
