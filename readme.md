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
### 🧭 Day 4
**Goal:** Use a real dataset from Kaggle to perform retail sales analysis and detect anomalies with Isolation Forest.

**🧠 Tasks Done**
- Downloaded the Supermarket Sales dataset from Kaggle and saved as sales.csv.
- Loaded the dataset in a Jupyter Notebook using python -m notebook.
- Performed EDA (Exploratory Data Analysis) and data cleaning.
- Visualized sales distribution and product line revenues with matplotlib & seaborn.
- Applied Isolation Forest to detect sales anomalies.
- Highlighted anomalous transactions on a time-series plot.
- Generated a PDF report from the HTML output and committed to GitHub.
**📊 Key Visuals & Insights**
- Histogram: Distribution of Total Sales values.
- Bar Chart: Total Sales by Product Line (ranked highest to lowest).
- Boxplot: Sales distribution by weekday.
- Time-Series Plot: Anomalies highlighted in red over sales timeline.
- Summary: Anomalies ≈ 1 % of transactions (rare but significant).


### 🧭 Day 5
**Goal:** Publish the project publicly on LinkedIn and Medium to showcase the results and share learnings.
**🧠 Tasks Done**
- Selected 2 visuals from Day 4 (Bar Chart + Anomaly Plot) for publication.
- Posted a short summary of the Retail Anomaly Detection PoC on LinkedIn.
- Published a detailed article on Medium explaining the process, dataset, and results.
- Added both post links and screenshots to the evidence sheet.
# LinkedIn
# → created post using provided Day 5 text and attached images.
# Medium
# → created new story, pasted full article text, added charts, published.
# Evidence updated in spreadsheet
**✅ Outcome**
- Demonstrated public communication and dissemination skills.
- Showcased the project to a professional audience on both LinkedIn and Medium.
- Prepared the project for portfolio and final O1 submission.

## 🔬 **Day 6 — Real-Time Retail Streaming Anomaly Detection**

**Date:** 2025-10-13  
**Goal:** Simulate real-time data flow and detect anomalies dynamically.

### 🧠 Tasks Done
- Created streaming data simulation for 50 days of retail sales.  
- Implemented live anomaly detection with Isolation Forest.  
- Visualized live updates in Jupyter Notebook.  
- Exported HTML report and committed to GitHub.
### 📊 Key Outputs
- Animated time-series anomaly chart
- HTML report
- GitHub commit proof