import pandas as pd
from sklearn.ensemble import IsolationForest

# Simulated data
data = {
    'day': range(1, 31),
    'sales': [200, 210, 205, 195, 1000, 215, 220, 230, 900, 210, 205, 198, 202, 199, 300, 205, 210, 205, 1005, 215, 218, 212, 209, 207, 500, 220, 215, 214, 900, 205]
}

df = pd.DataFrame(data)

# Model
model = IsolationForest(contamination=0.1, random_state=42)
df['anomaly'] = model.fit_predict(df[['sales']])

# Display anomalies
anomalies = df[df['anomaly'] == -1]
print("Anomalies found:")
print(anomalies)
