import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# Load the sample CSV
data = pd.read_csv('data.csv')

# Fit the model
model = IsolationForest(contamination=0.1, random_state=42)
data['anomaly'] = model.fit_predict(data[['sales']])

# Print anomalies
print("Anomalies found:")
print(data[data['anomaly'] == -1])

# Plot graph
plt.figure(figsize=(10,5))
plt.plot(data['day'], data['sales'], label='Sales', marker='o')
plt.scatter(
    data[data['anomaly'] == -1]['day'],
    data[data['anomaly'] == -1]['sales'],
    color='red',
    label='Anomalies',
    s=100
)
plt.title('Retail Sales Anomaly Detection')
plt.xlabel('Day')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.show()
