# Retail Anomaly Detection - Proof of Concept (PoC)

This demo detects unusual sales or inventory patterns using Isolation Forest (AI-based anomaly detection).

**Author:** Sri Charan Chowdary Konidina  
**Start Date:** Oct 7, 2025  
**Tech:** Python, Scikit-learn, Pandas, NumPy

### Objective
Help retailers identify abnormal spikes or drops in sales.

### How It Works
1. Load a CSV dataset.
2. Train IsolationForest model.
3. Detect anomalies.
4. Print anomaly indices.

### Example Output
Anomalies found:
    day  sales  anomaly
14   15    300       -1
18   19   1005       -1
24   25    500       -1


### Future Plans
- Add visualization (matplotlib)
- Add dashboard UI (Streamlit)
- Publish article on Medium / LinkedIn

### Day 1 Update — Oct 8, 2025
- Added data.csv file for testing.
- Implemented matplotlib visualization for anomaly detection.
- Project now displays a graph with red dots marking anomalies.

## 🧠 Day 2 — Interactive Anomaly Visualization (Plotly)

- Built an interactive anomaly detection chart using Plotly.
- Visualizes normal vs anomaly points on a dynamic graph.
- Technologies used: Python, Pandas, Scikit-Learn, Plotly.


### Example Output:
Anomalies found (rows):
 day  sales
  12    300
  18   1000
  24    500

### 🧩 What I Did Today
- Installed and configured **Plotly** for interactive visualization.
- Created a script (`visual_demo.py`) to visualize anomaly detection results from my Isolation Forest model.
- Successfully plotted **sales trends** and highlighted anomalies dynamically using red markers.

### 📊 What I Learned
- How visualization helps explain model results — not just raw outputs.
- Understood how **interactive graphs** (Plotly) make anomaly detection results easier to interpret.
- Learned that visual evidence of insights is a strong part of building credible AI/analytics portfolios.

### ⚙️ Technical Takeaways
- Learned the use of `plotly.express` for line plots and scatter overlays.
- Integrated anomaly data from `IsolationForest` predictions into a chart.
- Reinforced concepts of contamination ratio and anomaly labeling.

### 🧠 Why This Matters (O-1 Relevance)
- This shows my **ability to communicate machine learning insights** visually — a skill valuable for research, analytics, and AI engineering roles.
- Contributes to the “original contribution / impactful demonstration” criterion by producing **publicly verifiable code** and outputs.

---

### 🧭 Day 3 — Retail Anomaly Detection (Notebook + Report)
**Goal:** Convert anomaly detection script into a Jupyter Notebook and PDF report.  
**What I Did:**  
- Created `retail_anomaly_demo.ipynb` using Isolation Forest.  
- Visualized anomalies using Matplotlib.  
- Exported a clean PDF report for documentation.  
**Output Files:**  
- `retail_anomaly_demo.ipynb`  
- `retail_anomaly_demo_report.pdf`  
**Result:** Successfully demonstrated anomaly detection and documented results visually.

---
