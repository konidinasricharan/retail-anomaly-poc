# visual_demo.py
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import plotly.express as px
import plotly.io as pio

# Optional: set default renderer (browser)
pio.renderers.default = "browser"

# --- Data: either load existing data.csv or generate sample if not present ---
import os
if os.path.exists('data.csv'):
    df = pd.read_csv('data.csv')
else:
    np.random.seed(42)
    days = np.arange(1, 31)
    sales = np.random.normal(500, 50, 30)
    sales[14] = 300   # anomaly
    sales[18] = 1005  # anomaly
    sales[24] = 500   # borderline
    df = pd.DataFrame({"day": days, "sales": sales})

# --- Model: Isolation Forest ---
model = IsolationForest(contamination=0.1, random_state=42)
df['anomaly'] = model.fit_predict(df[['sales']])

# --- Separate anomalies ---
anomalies = df[df['anomaly'] == -1]

# --- Interactive plot ---
fig = px.line(df, x='day', y='sales', title='Retail Sales: Anomaly Detection (IsolationForest)', markers=True)
fig.add_scatter(x=anomalies['day'], y=anomalies['sales'],
                mode='markers', name='Anomalies',
                marker=dict(color='red', size=10))

# show in default browser
fig.show()

# Optional: save static PNG/SVG (requires kaleido)
try:
    fig.write_image("Day2_plot.png", scale=2)
    print("Saved Day2_plot.png")
except Exception as e:
    print("Could not save static image (kaleido missing?), error:", e)

# Print anomalies to console (evidence)
print("\nAnomalies found (rows):")
print(anomalies[['day','sales']].to_string(index=False))
