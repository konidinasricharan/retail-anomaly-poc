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

## 🧭 Day 7 — Mini Research Paper & Contribution Packet

- 📅 Date: October 14, 2025
- 🎯 Goal: Consolidate all previous work (Days 0–6) into a short research-style “mini paper” — a reproducible artifact showing your      ability to plan, execute, and document an ML project end-to-end.
## 🧩 Steps Completed
- Created mini_paper.md
- Built converter script using Python’s markdown library to generate a polished HTML report.
- Committed & pushed all artifacts to GitHub:
    - mini_paper.md
    - mini_paper.html
    - mini_paper_report.pdf
    - convert_md_to_html.py
- Captured screenshots for Drive evidence: HTML preview, PDF report, GitHub commit, and final folder structure.
- Updated O1 Evidence Sheet with entry ID 7 — “Mini Paper: Retail Anomaly Detection.”
## 🧠 Key Learnings
- Converted research progress into a citable, shareable artifact (important for O-1 visa documentation).
- Learned Markdown-to-HTML/PDF conversion and lightweight report formatting without LaTeX.
- Understood how to summarize ML projects into structured technical documentation.
- Practiced creating reproducible public deliverables (GitHub + Drive + Evidence Index).
## ✅ Outcome
- A professional mini research paper summarizing all prior project work — establishing a strong, documented technical contribution.

## 🧭 Day 8 — Publish Project on GitHub Pages  
**📅 Date:** October 16, 2025  
**🎯 Goal:** Make anomaly detection project publicly accessible online through GitHub Pages — turning mini research project into a live interactive portfolio artifact.  
### 🧩 Step Summary  
- Converted project notebook and summary into a clean HTML page.  
- Added `index.html` to the repository root for GitHub Pages.  
- Configured GitHub Pages to deploy from the **main branch (root folder)**.  
- Verified that the site loads properly online.  
- Documented the project as an official **“public evidence”** link.  
### 🧠 What Was Done  
- Generated a readable HTML report version of the project using:  
  ```bash
- notebook index.html
### 🧠 Outcome
- Project is now publicly accessible online.
- Acts as an independent, timestamped record of your original work.
- Strengthens my O-1 “original contribution” and “public dissemination” evidence.

### 🧭 Day 9 — Interactive Retail Anomaly Dashboard (Streamlit)
**Date:** October 16, 2025  
**Goal:** Created an interactive Streamlit dashboard for anomaly detection.  
**Highlights:**
- Added a web-based UI for users to upload CSVs and analyze retail data.  
- Integrated Isolation Forest to mark anomalies visually.  
- Dynamic contamination slider for flexible model tuning.  
**Output:**
Interactive dashboard visible at http://localhost:8501  
Displays anomaly points (in red) and summary table.

## 🧭 Day 10 — Retail Anomaly Interactive Dashboard
**Goal: Build a live interactive dashboard that detects anomalies from any uploaded CSV file.**
## What I Did: 
- Created retail_anomaly_dashboard.py using Streamlit for real-time interaction.
- Added file upload functionality to analyze any dataset dynamically.
- Implemented Isolation Forest to detect anomalies instantly upon upload.
- Visualized anomalies with red markers on dynamic charts and displayed a summary table.
## Output Files:
- retail_anomaly_dashboard.py
- Result: Built a fully interactive AI dashboard where users can upload datasets, visualize anomalies live, and view detailed detection summaries — showcasing real-world machine learning and dashboard development skills.

### 🧭 Day 11 — AI Resume Analyzer (Streamlit)
**Goal:** Create an AI-powered app that scores resumes for AI/ML readiness potential.  
**What I Did:**  
- Built a Streamlit app that analyzes resume text using NLP-based keyword detection.  
- Added scoring logic for AI keywords and achievements.  
- Produced a dynamic feedback interface with recommendations.  
**Output Files:**  
- `resume_analyzer_app.py`  
**Result:** Working AI app that evaluates resumes and provides resume score  feedback interactively.

### 🧠 Day 12 — Resume Analyzer Visualization & Download Report
**Goal:** Enhance the AI Resume Analyzer with visual insights and a downloadable report.  
**What I Did:**  
- Added interactive keyword frequency visualization (Matplotlib).  
- Displayed achievement-related terms in a clean dataframe.  
- Enabled one-click `.txt` report download.  
**Output Files:**  
- `resume_analyzer_app.py`  
- `resume_analysis_report.txt`  
**Result:** Built a more user-friendly and data-driven resume analyzer that provides both insights and exportable documentation.

### 🧭 Day 13 — AI Resume Analyzer Enhancement (Skill Extraction & Scoring)
**Goal:** Extend the AI Resume Analyzer by adding NLP-powered skill detection and match scoring.
**Tasks Completed:**
- Integrated spaCy for keyword-based skill extraction
- Designed an automatic resume skill scoring engine
- Created Streamlit-based visual interface with score chart
- Uploaded TXT resume, extracted key skills, and visualized presence
- Added results and screenshots to evidence repository
**Evidence Added:**
- `resume_analyzer_enhanced.py`
- `resume_analyzer_enhanced_screenshot1.png`
- `resume_analyzer_enhanced_screenshot2.png`
**Outcome:** Demonstrated AI-based resume scoring and visualization, progressing from prototype to intelligent NLP-enabled system.

---

### 🧭 Day 14 — Resume Comparison Dashboard (Multi-Resume AI Analyzer)
**Goal:** Build a multi-resume AI dashboard that compares skill match across multiple candidates.
**Tasks Completed:**
- Developed Streamlit app for multiple resume uploads
- Used spaCy NLP for skill extraction and scoring
- Created comparison heatmap using Seaborn and Matplotlib
- Visualized candidate skill match percentages and best-fit ranking
**Evidence Added:**
- `resume_comparison_dashboard.py`
**Outcome:** Demonstrated multi-document AI comparison, showing the ability to scale single-resume NLP analysis into a full comparative analytics dashboard.

---

### 🧭 Day 15 — Resume Summary Generator (OpenAI Integration)
**Goal:** Extend the AI Resume Analyzer to generate professional summaries and export them as PDFs.

**Tasks Completed:**
- Integrated OpenAI GPT model for text generation
- Created Streamlit app for single-resume summarization
- Automated PDF export using FPDF library
- Enhanced AI pipeline for real-world HR automation

**Evidence Added:**
- `resume_summary_generator.py`
- Screenshots (Summary UI, PDF Export)
- `.env` configuration for secure API usage

**Outcome:** Demonstrated generative AI capability by transforming raw resumes into structured, downloadable summaries — proving end-to-end NLP automation and product scalability.

## Day 16 — AI Resume Matching System Integration

### Description
- Integrated **AI Resume Matching System** that ranks multiple resumes against a job description.
- Generates **match score and reasoning** using GPT-4 model.
- Added **visual analytics (bar chart)** to show ranking.
- This enhancement evolves the Resume Analyzer into a **full AI Recruitment Assistant** capable of candidate screening automation.

### Evidence
- File: `resume_matcher.py`
- Output: Resume match scores printed in terminal
- Visualization: Matplotlib bar chart generated locally

## Day 17 — AI Recruitment Insights Dashboard
**Type:** AI Application Enhancement  
**URL:** [GitHub Repository](https://github.com/konidinasricharan/retail-anomaly-poc)

### Description
- Extended the **AI Recruitment Assistant** into a **Recruitment Insights Dashboard**.
- Added keyword extraction, skill coverage chart, and AI-generated pool analysis.
- Integrated **Matplotlib** for interactive charts inside Streamlit.
- Provides recruiters with a visual and narrative overview of candidate quality and skill trends.

### Evidence
- File: `resume_insight_dashboard.py`  
- Run Command: `streamlit run resume_insight_dashboard.py`  
- Output: Interactive dashboard with candidate insights, skill analytics, and AI-generated recommendations.

## Day 18 — AI Resume Ranking & Feedback System  
**Type:** AI Application Enhancement  
**URL:** [GitHub Repository](https://github.com/konidinasricharan/retail-anomaly-poc)

### Description
- Built a Resume Ranking and Feedback System extending the AI Recruitment Assistant.  
- Implements automated ranking, personalized feedback, and CSV export.  
- Provides visual candidate score distribution and recruiter recommendations via AI.  

### Evidence
- File: `resume_ranking_system.py`  
- Run: `streamlit run resume_ranking_system.py`  
- Output: Ranked dashboard with AI feedback and CSV report.  

## Day 19 — AI Shortlisting Assistant with Job Fit Reasoning
**Type:** AI Explainability & Decision Support  

### Description
- Added Smart Shortlisting Assistant to automatically shortlist candidates using AI reasoning.  
- Introduced threshold-based selection and AI explanations for each shortlisted candidate.  
- Implemented exportable CSV for recruiter reports and integrated recruiter summary generation.

### Evidence
- File: `ai_shortlisting_assistant.py`  
- Run: `streamlit run ai_shortlisting_assistant.py`  
- Output: Shortlist reasoning dashboard + CSV export  

### Day 20 — AI Recruitment Analytics Dashboard

- Goal: Extend the resume shortlisting system into a full analytics dashboard that provides insights, score distribution, keyword trends, and generates an AI Hiring Summary report.

### What was done today
- Created a new Streamlit app: ai_recruitment_dashboard.py
- Added CSV upload support for shortlisted_candidates.csv
- Extracted and cleaned score values for analysis
- Implemented a score distribution bar chart
- Extracted frequent words from AI Analysis to identify common skill themes
- Added a button to generate AI Hiring Summary Report
- Automatically saves the summary to:
- ai_hiring_summary.txt
- Prepared the dashboard as an advanced stage recruitment analytics tool
### Files Added
- ai_recruitment_dashboard.py
- ai_hiring_summary.txt (auto-generated after summary step)
### Evidence Added
- Screenshot of dashboard interface
- Screenshot of score chart + keyword chart
- AI Hiring Summary text file added to Google Drive
