# job_classifier/job_classifier.py
from pathlib import Path
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report, accuracy_score, f1_score
import sys

# --- Paths (robust relative to this file) ---
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
MODEL_DIR = BASE_DIR / "model"
DATA_PATH = DATA_DIR / "job_descriptions_sample.csv"
MODEL_PATH = MODEL_DIR / "job_classifier.pkl"

# --- Sample CSV (will be created automatically if missing) ---
SAMPLE_CSV_TEXT = """label,job_description
Data Engineer,"Design and maintain scalable ETL pipelines for batch and streaming data"
Data Engineer,"Build and optimize data ingestion workflows using Airflow and Spark"
Data Engineer,"Develop data warehouse models and star schemas for analytics teams"
Data Engineer,"Implement data validation and quality monitoring solutions"
Data Engineer,"Collaborate with analysts to deliver reliable data marts"
Data Engineer,"Manage data pipelines using Python and distributed systems"
Data Engineer,"Deploy ingestion frameworks to move data from APIs and databases"
Data Engineer,"Optimize SQL queries and warehouse performance"
Data Engineer,"Create workflows for real-time data processing on cloud platforms"
Data Engineer,"Maintain Hadoop, Spark, and distributed computation clusters"
Data Engineer,"Build scalable data lake architecture for enterprise analytics"
Data Engineer,"Create lineage and metadata tracking for all data assets"
Data Engineer,"Develop fault-tolerant ingestion pipelines in AWS"
Data Engineer,"Implement CDC (Change Data Capture) solutions"
Data Engineer,"Automate data preparation for machine learning pipelines"
Data Engineer,"Optimize data movement between OLTP and OLAP systems"
Data Engineer,"Write modular Python code for data transformations"
Data Engineer,"Build frameworks for schema enforcement and validation"
Data Engineer,"Integrate third-party APIs for ingestion and enrichment"
Data Engineer,"Monitor pipeline stability and reduce processing bottlenecks"
Data Engineer,"Develop batch processing workflows using Spark SQL"
Data Engineer,"Build and maintain data catalogs for enterprise teams"
Data Engineer,"Design data retention and archival strategies"
Data Engineer,"Collaborate with ML engineers on feature extraction pipelines"
Data Engineer,"Implement orchestration using Airflow DAGs"
ML Engineer,"Train and deploy machine learning models for prediction tasks"
ML Engineer,"Optimize model performance using hyperparameter tuning"
ML Engineer,"Implement model serving APIs for real-time inference"
ML Engineer,"Monitor model drift and retrain when necessary"
ML Engineer,"Build CI/CD pipelines for ML workflows"
ML Engineer,"Develop custom feature engineering pipelines"
ML Engineer,"Deploy models using Docker and Kubernetes"
ML Engineer,"Optimize GPU usage for deep learning workloads"
ML Engineer,"Integrate MLflow for experiment tracking"
ML Engineer,"Convert notebooks into production Python modules"
ML Engineer,"Implement vector search and embedding models"
ML Engineer,"Build streaming ML inference services"
ML Engineer,"Develop multi-model architectures for ensemble predictions"
ML Engineer,"Implement transformers for NLP tasks"
ML Engineer,"Use PyTorch and TensorFlow for deep learning solutions"
ML Engineer,"Create monitoring dashboards for model performance"
ML Engineer,"Optimize memory usage of training pipelines"
ML Engineer,"Develop anomaly detection models using statistical ML"
ML Engineer,"Build automatic model retraining workflows"
ML Engineer,"Test ML models using cross-validation and bootstrapping"
ML Engineer,"Prepare large datasets for supervised learning"
ML Engineer,"Implement explainability frameworks like SHAP or LIME"
ML Engineer,"Deploy models on cloud platforms like AWS Sagemaker"
ML Engineer,"Develop recommendation systems using embeddings"
ML Engineer,"Debug data leakage and training issues in ML pipelines"
Security Analyst,"Monitor SIEM dashboards for suspicious log activity"
Security Analyst,"Investigate alerts and triage potential threats"
Security Analyst,"Analyze firewall and network logs for anomalies"
Security Analyst,"Perform vulnerability scans and risk assessments"
Security Analyst,"Respond to phishing and malware incidents"
Security Analyst,"Develop playbooks for incident response"
Security Analyst,"Analyze suspicious user behavior using UEBA systems"
Security Analyst,"Prepare reports for SOC operations"
Security Analyst,"Conduct threat hunting in cloud environments"
Security Analyst,"Monitor IDS and IPS signatures"
Security Analyst,"Analyze endpoint detection alerts"
Security Analyst,"Review email gateway logs for malicious patterns"
Security Analyst,"Create dashboards for SOC monitoring"
Security Analyst,"Investigate brute force and authentication failures"
Security Analyst,"Document incidents and remediation steps"
Security Analyst,"Perform forensic analysis on compromised systems"
Security Analyst,"Monitor DLP alerts and enforce data policies"
Security Analyst,"Analyze network packets for malicious traffic"
Security Analyst,"Respond to ransomware threat indicators"
Security Analyst,"Perform risk scoring and severity classification"
Security Analyst,"Review IAM policies and detect privilege escalation"
Security Analyst,"Identify gaps in security posture"
Security Analyst,"Monitor cloud IAM logs for abnormal access"
Security Analyst,"Respond to high-severity SOC alerts"
Security Analyst,"Collaborate with engineering teams to patch vulnerabilities"
Product Manager,"Define product roadmap and feature priorities"
Product Manager,"Gather requirements from stakeholders and customers"
Product Manager,"Write user stories and maintain the product backlog"
Product Manager,"Conduct competitive analysis for product positioning"
Product Manager,"Collaborate with engineering teams during sprints"
Product Manager,"Perform user research and interviews"
Product Manager,"Analyze product usage metrics to guide decisions"
Product Manager,"Define key success metrics (KPIs)"
Product Manager,"Lead sprint planning and grooming sessions"
Product Manager,"Document feature specifications"
Product Manager,"Prioritize bugs and improvements"
Product Manager,"Work closely with design teams on prototypes"
Product Manager,"Manage cross-functional communication"
Product Manager,"Conduct A/B tests to validate new features"
Product Manager,"Prepare product requirement documents (PRDs)"
Product Manager,"Define customer personas and journeys"
Product Manager,"Evaluate market opportunities and gaps"
Product Manager,"Collaborate with marketing for product launches"
Product Manager,"Monitor feature performance and iterate"
Product Manager,"Develop release plans and timelines"
Product Manager,"Ensure alignment with strategic objectives"
Product Manager,"Perform cost/benefit analysis for new initiatives"
Product Manager,"Review customer feedback and suggest enhancements"
Product Manager,"Support sales teams with product knowledge"
Product Manager,"Drive long-term product vision and strategy"
DevOps Engineer,"Maintain CI/CD pipelines for application deployment"
DevOps Engineer,"Manage Kubernetes clusters for microservices"
DevOps Engineer,"Automate infrastructure with Terraform"
DevOps Engineer,"Monitor application performance and uptime"
DevOps Engineer,"Implement scalable cloud architectures"
DevOps Engineer,"Configure load balancers and autoscaling"
DevOps Engineer,"Implement observability dashboards using Grafana"
DevOps Engineer,"Perform log aggregation with ELK stack"
DevOps Engineer,"Deploy infrastructure updates using GitOps workflows"
DevOps Engineer,"Write automation scripts using Python and Bash"
DevOps Engineer,"Manage container registries and versioning"
DevOps Engineer,"Optimize cloud cost and usage"
DevOps Engineer,"Perform incident response for infrastructure failures"
DevOps Engineer,"Implement zero-downtime deployment strategies"
DevOps Engineer,"Configure network and security rules in cloud"
DevOps Engineer,"Manage secrets using Vault or AWS Secrets Manager"
DevOps Engineer,"Improve deployment performance and reliability"
DevOps Engineer,"Analyze logs for system bottlenecks"
DevOps Engineer,"Implement blue-green and canary deployments"
DevOps Engineer,"Review application performance metrics"
DevOps Engineer,"Migrate workloads to cloud platforms"
DevOps Engineer,"Monitor Docker container health"
DevOps Engineer,"Automate environment provisioning"
DevOps Engineer,"Ensure compliance with infrastructure policies"
DevOps Engineer,"Collaborate with SRE teams to improve reliability"
Data Scientist,"Build predictive models using statistical and ML techniques"
Data Scientist,"Perform exploratory data analysis for business insights"
Data Scientist,"Engineer features for machine learning workflows"
Data Scientist,"Conduct hypothesis testing and statistical validation"
Data Scientist,"Develop clustering and segmentation models"
Data Scientist,"Create dashboards for presenting analytical results"
Data Scientist,"Perform time-series forecasting for business teams"
Data Scientist,"Build NLP models for text classification"
Data Scientist,"Experiment with deep learning architectures"
Data Scientist,"Prepare datasets for supervised learning"
Data Scientist,"Develop churn prediction models"
Data Scientist,"Analyze customer behavior using ML techniques"
Data Scientist,"Optimize models for accuracy and precision"
Data Scientist,"Deploy analytical models to production"
Data Scientist,"Perform anomaly detection using statistical methods"
Data Scientist,"Prepare Jupyter notebooks for reproducible analysis"
Data Scientist,"Visualize data patterns using Python libraries"
Data Scientist,"Conduct A/B testing for product experiments"
Data Scientist,"Build recommendation models for personalization"
Data Scientist,"Perform data cleaning and transformation"
Data Scientist,"Create feature importance analysis"
Data Scientist,"Develop experimentation frameworks"
Data Scientist,"Collaborate with stakeholders to interpret model results"
Data Scientist,"Build dashboards for exec-level reporting"
Data Scientist,"Develop validation pipelines for ML models"
"""

def ensure_data():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not DATA_PATH.exists():
        print(f"[INFO] Sample CSV not found. Creating sample dataset at: {DATA_PATH}")
        DATA_PATH.write_text(SAMPLE_CSV_TEXT)
    else:
        print(f"[INFO] Found dataset at: {DATA_PATH}")

def train_and_save(verbose=True):
    ensure_data()
    try:
        df = pd.read_csv(DATA_PATH)
    except Exception as e:
        print("[ERROR] Unable to read CSV:", DATA_PATH, file=sys.stderr)
        raise
    if df.shape[0] < 2:
        raise ValueError("Not enough rows in dataset to train. Add more samples to data/job_descriptions_sample.csv")

    X = df['job_description'].astype(str)
    y = df['label'].astype(str)

    # use a larger TF-IDF config for better coverage on this richer dataset
    pipe = make_pipeline(
        TfidfVectorizer(ngram_range=(1,3), max_features=20000, min_df=1),
        LogisticRegression(max_iter=3000)
    )

    if verbose:
        print("[INFO] Training classifier... This may take a few seconds.")

    pipe.fit(X, y)

    if verbose:
        try:
            # robust evaluation but avoid crashes on tiny test sets
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            preds = pipe.predict(X_test)
            acc = accuracy_score(y_test, preds)
            f1 = f1_score(y_test, preds, average='macro')
            print(f"[INFO] Eval — Accuracy: {acc:.3f}   Macro F1: {f1:.3f}")
            print("[INFO] Classification report:\n", classification_report(y_test, preds))
        except Exception as e:
            print("[WARN] Evaluation failed (likely due to small/imbalanced split):", e)

    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipe, MODEL_PATH)

    if verbose:
        print(f"[INFO] Saved model to {MODEL_PATH}")
    return MODEL_PATH

def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError("Model not trained yet. Run train_and_save() first.")
    return joblib.load(MODEL_PATH)

def predict(text):
    """
    Return (pred_label, ranked_list_of_tuples[(label, prob), ...])
    Safe: filters out invalid class names and never returns 'nan' as label.
    """
    model = load_model()
    pred = None
    try:
        raw = model.predict([text])[0]
        pred = str(raw) if (raw == raw) else None
    except Exception:
        pred = None

    ranked = []
    try:
        probs = model.predict_proba([text])[0]
        classes = list(model.classes_)
        for c, p in zip(classes, probs):
            # skip invalid class names
            if c is None:
                continue
            sc = str(c)
            if sc.lower() == "nan" or sc.strip() == "":
                continue
            ranked.append((sc, float(p)))
        ranked = sorted(ranked, key=lambda x: -x[1])
    except Exception:
        # fallback to single prediction
        if pred:
            ranked = [(pred, 1.0)]
        else:
            ranked = [("unknown", 0.0)]

    # ensure pred is meaningful
    if (not pred or pred.lower() in ["nan", "none", "null"]) and len(ranked) > 0:
        pred = ranked[0][0]

    if not pred:
        pred = "unknown"

    return pred, ranked

# CLI helpers for quick checks
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--train", action="store_true")
    parser.add_argument("--infer", type=str, help="Job description text to infer")
    args = parser.parse_args()
    if args.train:
        train_and_save()
    elif args.infer:
        p, r = predict(args.infer)
        print("Predicted:", p)
        print("Ranked probs:", r)
    else:
        print("Use --train or --infer 'text'")
