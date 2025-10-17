# retail_anomaly_dashboard.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from io import StringIO

st.set_page_config(page_title="Retail Anomaly Detection Dashboard", layout="wide")

st.title("🛍️ Retail Anomaly Detection Dashboard")
st.markdown("""
This dashboard allows you to **upload any sales dataset (CSV)** and detect anomalies using **Isolation Forest**.
""")

# --- File uploader ---
uploaded_file = st.file_uploader("📤 Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # --- Read the uploaded file ---
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    df = pd.read_csv(stringio)

    st.write("✅ File successfully loaded!")
    st.write("### Preview of your data:")
    st.dataframe(df.head())

    # --- Ask user which column to analyze ---
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
    if len(numeric_cols) == 0:
        st.error("No numeric columns found. Please upload a dataset with at least one numeric column.")
    else:
        target_col = st.selectbox("Select the column to analyze for anomalies:", numeric_cols)

        # --- Run Isolation Forest ---
        model = IsolationForest(contamination=0.1, random_state=42)
        df["anomaly"] = model.fit_predict(df[[target_col]])

        anomalies = df[df["anomaly"] == -1]

        st.success(f"Detected {len(anomalies)} anomalies in '{target_col}'!")

                # --- Visualization ---
        st.subheader("📊 Visualization")

        # Choose x-axis dynamically
        if "Date" in df.columns:
            df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
            df = df.sort_values("Date")
            x_col = "Date"
        else:
            # Create a new column safely
            if "Index" not in df.columns:
                df["Index"] = range(len(df))
            if "Index" not in anomalies.columns:
                anomalies["Index"] = df.loc[anomalies.index, "Index"]
            x_col = "Index"

        # --- Plot chart ---
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(df[x_col], df[target_col], marker="o", label="Data", color="blue")
        ax.scatter(anomalies[x_col], anomalies[target_col], color="red", label="Anomaly", s=60)
        ax.set_xlabel(x_col)
        ax.set_ylabel(target_col)
        ax.legend()
        st.pyplot(fig)
