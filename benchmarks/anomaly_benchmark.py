import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.metrics import precision_score, recall_score

# -------------------------
# 1. Load Dataset
# -------------------------
data = {
    "day": range(1, 26),
    "sales": [200, 220, 250, 260, 300, 280, 275, 290, 400, 410,
              420, 430, 390, 410, 300, 310, 320, 330, 1005, 340,
              350, 355, 360, 365, 500]
}

df = pd.DataFrame(data)

# Ground truth (manually labeled anomalies)
df["true_anomaly"] = df["sales"].apply(lambda x: 1 if x > 800 or x < 220 else 0)

# -------------------------
# 2. Isolation Forest
# -------------------------
iso = IsolationForest(contamination=0.15, random_state=42)
df["iso_pred"] = iso.fit_predict(df[["sales"]])
df["iso_pred"] = df["iso_pred"].apply(lambda x: 1 if x == -1 else 0)

# -------------------------
# 3. Z-Score Method
# -------------------------
mean = df["sales"].mean()
std = df["sales"].std()
df["z_score"] = (df["sales"] - mean) / std
df["z_pred"] = df["z_score"].apply(lambda x: 1 if abs(x) > 2 else 0)

# -------------------------
# 4. IQR Method
# -------------------------
Q1 = df["sales"].quantile(0.25)
Q3 = df["sales"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df["iqr_pred"] = df["sales"].apply(lambda x: 1 if x < lower or x > upper else 0)

# -------------------------
# 5. Evaluation Function
# -------------------------
def evaluate(y_true, y_pred):
    precision = precision_score(y_true, y_pred, zero_division=0)
    recall = recall_score(y_true, y_pred, zero_division=0)
    false_positives = ((y_pred == 1) & (y_true == 0)).sum()
    return precision, recall, false_positives

results = []

for model, col in [
    ("Isolation Forest", "iso_pred"),
    ("Z-Score", "z_pred"),
    ("IQR", "iqr_pred")
]:
    p, r, fp = evaluate(df["true_anomaly"], df[col])
    results.append([model, round(p, 2), round(r, 2), fp])

benchmark_df = pd.DataFrame(
    results,
    columns=["Model", "Precision", "Recall", "False Positives"]
)

print("\nBenchmark Results:")
print(benchmark_df)
