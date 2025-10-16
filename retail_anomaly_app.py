import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

st.set_page_config(page_title="Retail Anomaly Detector", layout="centered")

st.title("🛍️ Retail Anomaly Detection Dashboard")
st.write("Analyze daily sales data and detect anomalies using Isolation Forest.")

# Upload CSV
uploaded_file = st.file_uploader("📂 Upload a CSV file with 'day' and 'sales' columns", type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    st.info("Using sample data since no file uploaded.")
    data = {
        "day": range(1, 26),
        "sales": [200, 220, 250, 260, 300, 280, 275, 290, 400, 410, 420, 430, 390, 410, 300, 310, 320, 330, 1005, 340, 350, 355, 360, 365, 500]
    }
    df = pd.DataFrame(data)

# Model parameters
contam = st.slider("Select anomaly percentage (contamination)", 0.01, 0.3, 0.1)
st.write("Model sensitivity:", contam)

# Run model
model = IsolationForest(contamination=contam, random_state=42)
st.write("📋 Columns detected in file:", df.columns.tolist())
# Detect correct column for sales
if "sales" in df.columns:
    sales_col = "sales"
elif "Total" in df.columns:
    sales_col = "Total"
elif "gross income" in df.columns:
    sales_col = "gross income"
else:
    st.error("⚠️ Could not find a suitable sales column. Please ensure your CSV has 'sales', 'Total', or 'gross income'.")
    st.stop()

df = df.rename(columns={sales_col: "sales"})
df["anomaly"] = model.fit_predict(df[["sales"]])


# Show anomalies
anomalies = df[df["anomaly"] == -1]

st.subheader("📊 Anomaly Detection Results")
st.dataframe(anomalies)

# Plot results
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df["day"], df["sales"], marker='o', label="Sales")
ax.scatter(anomalies["day"], anomalies["sales"], color="red", label="Anomalies", s=120)
ax.set_xlabel("Day")
ax.set_ylabel("Sales ($)")
ax.set_title("Retail Sales Anomaly Detection")
ax.legend()
st.pyplot(fig)

st.success("✅ Analysis complete! Adjust the slider or upload new data to test more cases.")
