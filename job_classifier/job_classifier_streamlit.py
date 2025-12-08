# job_classifier/job_classifier_streamlit.py
import streamlit as st
from pathlib import Path
import time
import pandas as pd
import joblib

# import functions from the module
from job_classifier import train_and_save, predict, MODEL_PATH, DATA_PATH

st.set_page_config(page_title="Job Description Classifier", layout="wide")
st.title("📂 Job Description Classifier — Day 28 (Streamlit)")

BASE_DIR = Path(__file__).resolve().parent
st.caption(f"App base folder: `{BASE_DIR}`")
st.caption(f"Dataset path: `{DATA_PATH}`")
st.caption(f"Model path: `{MODEL_PATH}`")

col1, col2 = st.columns([1,2])

with col1:
    st.header("Model Controls")
    if st.button("🔁 Train model now"):
        with st.spinner("Training model... (this may take a few seconds)"):
            try:
                path = train_and_save(verbose=True)
                st.success(f"Model trained and saved to: `{path}`")
            except Exception as e:
                st.error(f"Training failed: {e}")
                st.stop()
        time.sleep(0.3)

    st.markdown("---")
    st.write("Model file exists?" )
    model_exists = Path(MODEL_PATH).exists()
    st.write(model_exists)
    if model_exists:
        st.write("Model last-modified:", time.ctime(Path(MODEL_PATH).stat().st_mtime))

    st.markdown("**Sample dataset preview**")
    try:
        if not Path(DATA_PATH).exists():
            st.info("Sample dataset missing — it will be created on training or you can add one manually.")
        else:
            df = pd.read_csv(DATA_PATH)
            st.dataframe(df)
    except Exception as e:
        st.error(f"Unable to load sample dataset: {e}")

with col2:
    st.header("Predict Job Family")
    user_text = st.text_area("Paste job description here", height=220, value="We need a Data Engineer to build ETL pipelines with Airflow and Spark.")
    if st.button("🧠 Predict"):
        try:
            pred, ranked = predict(user_text)
            st.success(f"Predicted job family: **{pred}**")
            try:
                probs_df = pd.DataFrame(ranked, columns=["label", "probability"])
                st.dataframe(probs_df)
            except Exception:
                st.write(ranked)
        except FileNotFoundError:
            st.error("Model not found. Click 'Train model now' to create model first.")
        except Exception as e:
            st.error(f"Prediction error: {e}")

st.markdown("---")
st.caption("Evidence: Save screenshots of the Train success message and Predict output. Model stored in job_classifier/model/job_classifier.pkl")

# Debug panel (expand if you need more internals) - safe to leave
with st.expander("Debug info (classes & model)"):
    try:
        if Path(MODEL_PATH).exists():
            m = joblib.load(MODEL_PATH)
            st.write("MODEL classes_:", list(getattr(m, "classes_", [])))
        else:
            st.write("Model not present yet.")
        st.write("DATA exists:", Path(DATA_PATH).exists())
    except Exception as e:
        st.write("Debug load error:", e)
