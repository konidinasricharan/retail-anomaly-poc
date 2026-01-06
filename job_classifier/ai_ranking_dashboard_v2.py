import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="AI Ranking Dashboard V2",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Ranking Dashboard V2")
st.markdown(
    "Interactive candidate ranking and analytics using unified AI scores."
)

# Sample candidate data (simulating system output)
data = [
    {"Candidate": "Candidate A", "Unified Score": 88},
    {"Candidate": "Candidate B", "Unified Score": 81},
    {"Candidate": "Candidate C", "Unified Score": 76},
    {"Candidate": "Candidate D", "Unified Score": 69},
    {"Candidate": "Candidate E", "Unified Score": 62},
]

df = pd.DataFrame(data)

# Threshold filter
threshold = st.slider(
    "🎯 Minimum Score Threshold",
    min_value=50,
    max_value=100,
    value=70
)

filtered_df = df[df["Unified Score"] >= threshold].sort_values(
    by="Unified Score", ascending=False
)

st.subheader("🏆 Ranked Candidates")
st.dataframe(filtered_df, use_container_width=True)

# Interactive bar chart
st.subheader("📈 Candidate Score Comparison")

fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(
    filtered_df["Candidate"],
    filtered_df["Unified Score"]
)
ax.axhline(
    y=threshold,
    color="red",
    linestyle="--",
    label=f"Threshold: {threshold}"
)
ax.set_ylabel("Unified Score (%)")
ax.set_title("AI Candidate Ranking")
ax.legend()

st.pyplot(fig)

# Score distribution
st.subheader("📊 Score Distribution")

fig2, ax2 = plt.subplots(figsize=(10, 4))
ax2.hist(df["Unified Score"], bins=5)
ax2.set_xlabel("Score Range")
ax2.set_ylabel("Number of Candidates")
ax2.set_title("Unified Score Distribution")

st.pyplot(fig2)
