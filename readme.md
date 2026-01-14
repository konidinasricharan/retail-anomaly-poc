[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17644837.svg)](https://doi.org/10.5281/zenodo.17644837)
## 📘 Citation
If you use this work, please cite:
**Konidina, Sri Charan (2025). _Retail AI Analytics Whitepaper — Anomaly Detection, Real-Time Retail ML, and AI Recruitment Systems._ Zenodo. https://doi.org/10.5281/zenodo.17644837**

# 🤖 AI Recruitment Suite — v1.1

An end-to-end AI-powered recruitment system that automates resume parsing, skill extraction,
experience similarity scoring, and unified candidate evaluation using explainable AI techniques.

**Release Version:** v1.1  
**Author:** Sri Charan Konidina  
**Tech Stack:** Python, Streamlit, NLP, TF-IDF, LLMs  

---

## 🚀 What’s New in v1.1
- Job Description Classification
- Resume Parsing (PDF + Text)
- Skill Extraction Engine
- Experience Similarity Scoring (TF-IDF)
- Unified Candidate Scoring Engine
- Interactive Streamlit Dashboards

---

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

---

### 🧭 Day 21 — Whitepaper: Retail AI Analytics & Recruitment Assistant
**Goal:** Publish a technical whitepaper that consolidates Days 0–20 into a reproducible research-style report.

**Files Added:**
- `Retail_AI_Analytics_Whitepaper.md`
- `Retail_AI_Analytics_Whitepaper.pdf`

**Summary:**  
This whitepaper documents the development and evaluation of:
1. A Retail Anomaly Detection proof-of-concept (Isolation Forest + streaming simulation).  
2. An AI Recruitment Assistant (resume scoring, comparison, shortlisting, and analytics dashboards).  
It contains methodology, dataset descriptions, experimental results, visualizations, and next steps.

**Evidence:** Public PDF on GitHub + GitHub Release (optionally archived on Zenodo for DOI).

## 📅 Day 22 — Paper #2: AI Recruitment System Technical Deep-Dive  
**Date:** November 19 2025  
**Type:** Technical Paper / Documentation  

### 📝 Summary  
Today, I authored **Paper #2 — "AI Recruitment System: Architecture, Evaluation & LLM-Based Ranking"**, a full technical deep-dive describing how my AI recruitment system works end-to-end.  
This paper includes:

- Full system architecture  
- Resume ingestion → Job description parsing → LLM ranking pipeline  
- Score extraction logic  
- Streamlit analytics dashboard  
- Evaluation methodology  
- Prompt engineering strategy  
- Future improvements  
- Real ATS applicability  

This serves as strong **Evidence** under:  
✔️ Original Contribution  
✔️ Authorship  
✔️ Evidence of Expertise  
✔️ Technical Documentation  

### 📂 Files Added  
- `AI_Recruitment_Technical_Paper.md`  
- `assets/day23/` (optional screenshots)  

### 📌 Steps Completed  
- Wrote full 9-section technical paper  
- Added Markdown file to GitHub  
- Updated evidence spreadsheet  
- Prepared content for future DOI submission / publication  

## 📅 Day 24 — Medium Article #2 (AI Recruitment)

**Task:** Published a full Medium article titled *“AI in Recruitment: How Resume Scoring & Hiring Analytics Transform Talent Selection”*.

**Why this matters:**  
This article demonstrates public dissemination of expertise and supports authorship & original contributions.

**Link:** https://medium.com/@konidinasricharan/ai-in-recruitment-how-resume-scoring-hiring-analytics-transform-talent-selection-20fb1f0e094c

**Evidence Added:**  
- Screenshots  
- URL  

## 📅 Day 25 — LinkedIn Research Thread

**Task:** Published a 7-part LinkedIn research thread titled *“20-Day AI Journey: From Retail Anomalies to AI Recruitment Systems.”*

**Includes:**
- Breakdown of all projects (Days 0–20)
- Public dissemination of technical expertise
- Thread with engagement + screenshots for evidence

**Link:** (https://www.linkedin.com/in/sricharankonidina/)

## 📅 Day 26 — System Architecture Diagrams (Retail + Recruitment)

**Task:** Created two professional architecture diagrams using diagrams.net:
1. Retail Anomaly Detection System
2. AI Recruitment & Resume Scoring System

**Outputs Added:**
- PNG + PDF diagrams
- `/architecture/` folder in GitHub

**Why this matters:**  
Architecture diagrams demonstrate technical clarity and are used as evidence for original contributions and engineering documentation.

**Status:** Completed.

## 📅 Day 27 — Conference Submission Version (DOI Published)

**Task:**  
Converted the AI Recruitment System whitepaper into a formal *conference-style submission version* and published it with a DOI through Zenodo.  
This counts as **extraordinary ability evidence** under:

- Authorship of scholarly articles  
- Original contributions of major significance  
- Published work in the field  
- Public dissemination of technical research  


**DOI:**  
10.5281/zenodo.17791779

**Files Added to Repo:**  
- `/conference/ai_recruitment_conference_paper.pdf`  
- `/conference/ai_recruitment_conference_submission.zip`  

**Why this matters:**  
A conference submission + DOI is considered formal research dissemination and strengthens multiple criteria. This shows active participation in the scientific community and supports your claim of contributing original work to the field of AI-driven recruitment systems.

**Status:** Completed.

## 🗓️ Day 28 — AI Job Description Classifier Module (ML Model + Streamlit UI)

### 🎯 Goal  
Build a machine-learning powered classifier that can automatically categorize job descriptions into job families using TF-IDF + Logistic Regression.  
Add a Streamlit interface for interactive predictions.

This module becomes a key part of the AI Recruitment Suite and counts as *Original Contribution* for evidence.

---

### 🧩 What I Built Today
#### 1️⃣ **A robust ML training pipeline**
- Automatically creates dataset if missing  
- Trains TF-IDF + Logistic Regression  
- Handles 125+ job description samples across 5 job families  
- Saves model to: `job_classifier/model/job_classifier.pkl`

#### 2️⃣ **A production-ready prediction function**
- Handles class errors safely  
- Returns ranked probability table  
- Useful for O-1 “original contribution” evidence

Features:
- “Train Model Now” button  
- Dataset preview  
- Probability ranking table  
- Predicted job family display  
- Debug expander showing training paths, model classes, etc.

## Run command:
## ```bash
## streamlit run job_classifier/job_classifier_streamlit.py.

## 🗓️ Day 29 — AI Skill Extraction Engine (NER-Based NLP Module)

### 🎯 Goal  
Build an explainable **Skill Extraction Engine** that automatically identifies technical skills from job descriptions and resumes using lightweight NLP (NER-style keyword matching).

This module strengthens the AI Recruitment Suite by adding transparent skill intelligence used in candidate evaluation and job matching.

---

### 🧩 What I Built Today

#### 1️⃣ **NER-Style Skill Extraction Engine**
- Rule-based NLP system using curated technical skill vocabulary
- Extracts skills across multiple categories:
  - Programming Languages  
  - Data & Machine Learning  
  - Cloud & DevOps  
  - Data Engineering  
  - Security  
  - Tools
- Designed for explainability and ATS-style interpretation

#### 2️⃣ **Reusable Python Extraction Module**
File: job_classifier/skill_extractor.py
- Normalizes text
- Uses regex-based matching
- Returns structured skill categories
- No external NLP dependencies required

#### 3️⃣ **Interactive Streamlit Interface**
File: job_classifier/skill_extractor_streamlit.py

Features:
- Paste job description or resume
- One-click skill extraction
- Grouped skill visualization
- Clean recruiter-friendly UI

### Run command:
### ```bash
### streamlit run job_classifier/skill_extractor_streamlit.py

## 🗓️ Day 30 — Resume Parsing Engine (PDF + Text Parser)

### 🎯 Goal  
Build a **Resume Parsing Engine** that extracts clean, structured text from PDF resumes and prepares the content for downstream AI modules such as skill extraction, resume scoring, and job matching.

This module forms a core component of an ATS-style AI recruitment system.

---

### 🧩 What I Built Today

#### 1️⃣ **PDF Resume Parsing Engine**
- Extracts text from multi-page PDF resumes
- Cleans and normalizes raw resume content
- Removes noise, extra spaces, and non-ASCII characters
- Produces usable plain text for NLP pipelines

File:job_classifier/resume_parser.py

---

#### 2️⃣ **Interactive Streamlit Resume Upload UI**
File:job_classifier/resume_parser_streamlit.py

Features:
- Upload PDF resumes
- Automatic parsing and extraction
- Scrollable text output for review
- Ready for integration with skill and matching engines

# Run command:
- ```bash
- streamlit run job_classifier/resume_parser_streamlit.py

## 🧠 Relevance
- Demonstrates applied NLP and document processing
- Shows real-world ATS system design
- Enables automated resume analysis workflows
- Strengthens sustained original contribution evidence

## 🗓️ Day 31 — Resume Skill Extraction (Parsed Resume → Skill Engine)

### 🎯 Goal  
Integrate the **Resume Parsing Engine (Day 30)** with the **Skill Extraction Engine (Day 29)** to automatically extract structured technical skills directly from uploaded PDF resumes.

This creates a complete **resume understanding pipeline**, a core feature of ATS and AI recruitment systems.

---

### 🧩 What I Built Today

#### 1️⃣ **End-to-End Resume Skill Extraction Pipeline**
- Upload a PDF resume
- Automatically parse resume text
- Extract categorized technical skills
- Display results in a clean, recruiter-friendly UI

Pipeline flow:PDF Resume → Parsed Text → Skill Extraction → Structured Skill Output

---

#### 2️⃣ **Integrated Streamlit Application**
File:
job_classifier/resume_skill_extractor_streamlit.py

Features:
- PDF resume upload
- Automatic text parsing
- Skill extraction using NLP
- Side-by-side view:
  - Parsed resume text
  - Extracted skills by category

# Run command:
- ```bash
- streamlit run resume_skill_extractor_streamlit.py

🧠 Relevance
- Demonstrates multi-module system integration
- Shows real-world ATS-style NLP workflow
- Strengthens evidence of applied AI expertise
- Adds depth to AI Recruitment Suite

## 🗓️ Day 32 — Experience Similarity Model (TF-IDF Baseline)

### 🎯 Goal  
Add an **Experience Similarity Model** that measures how closely a candidate’s resume experience matches a job description using **TF-IDF vectorization and cosine similarity**.

This module introduces **quantitative experience matching**, a core component of real-world ATS and AI recruitment systems.

---

### 🧩 What I Built Today

#### 1️⃣ **Experience Similarity Engine**
- Uses TF-IDF vectorization (unigrams + bigrams)
- Computes cosine similarity between resume and job text
- Outputs a normalized percentage score (0–100)
- Fully explainable baseline model

File:job_classifier/experience_similarity.py

---

#### 2️⃣ **Interactive Streamlit Interface**
File:job_classifier/experience_similarity_streamlit.py

Features:
- Side-by-side resume and job description inputs
- One-click experience similarity scoring
- Percentage score display
- Visual progress bar for match strength

# Run command:
- ```bash
- streamlit run experience_similarity_streamlit.py

## 🗓️ Day 33 — Unified Candidate Score (Skills + Experience + LLM)

### 🎯 Goal  
Build a **Unified Candidate Scoring Engine** that combines multiple evaluation signals into a single, explainable score used for candidate ranking and shortlisting.

The unified score integrates:
- Skill Match Score  
- Experience Similarity Score  
- LLM-Based Reasoning Score  

This represents the **core decision logic** of the AI Recruitment System.

---

### 🧩 What I Built Today

#### 1️⃣ **Unified Scoring Logic**
- Weighted scoring formula combining objective and AI-driven metrics
- Transparent and configurable weights
- Produces a normalized final score (0–100)

# Formula:
- Final Score =
- (Skill Match × 0.4) +
- (Experience Similarity × 0.4) +
- (LLM Reasoning × 0.2)

# File:unified_score.py

---

#### 2️⃣ **Interactive Streamlit Scoring Interface**
# File:unified_score_streamlit.py


Features:
- Adjustable sliders for each score component
- One-click unified score calculation
- Visual progress bar
- Score contribution breakdown for explainability

# Relevance
- Demonstrates system-level AI design
- Combines ML, NLP, and LLM reasoning
- Mirrors real-world ATS scoring pipelines
- Strengthens evidence of sustained original contribution

## 🗓️ Day 34 — Publish Medium Article #3 (Resume Parsing Insights)

## 🗓️ Day 35 — GitHub Release: Recruitment Suite v1.1

## 🗓️ Day 36 — AI Ranking Dashboard V2 (Interactive Charts)

### 🎯 Goal  
Build **AI Ranking Dashboard V2**, an interactive visualization layer that enables recruiters to explore, rank, and analyze candidates using unified AI scores.

This dashboard transforms model outputs into **human-centered decision intelligence**.

---

### 🧩 What I Built Today

#### 1️⃣ **Interactive Candidate Ranking Dashboard**
- Dynamic ranking based on unified AI score
- Threshold-based filtering
- Real-time updates via Streamlit

File: job_classifier/ai_ranking_dashboard_v2.py

---

#### 2️⃣ **Visual Analytics**
- Bar chart comparing candidate scores
- Threshold reference line
- Score distribution histogram
- Combined table + chart view
---
# Run command:
- ```bash
- streamlit run ai_ranking_dashboard_v2.py
---
# 🧪 Example Output
- Candidate A — 88%
- Candidate B — 81%
- Candidate C — 76%

---

## 📅 Day 37 — Paper #3: Embedding-Based Job Matching (Full Technical Paper)

### 🎯 Objective
Complete and publish a full research-style paper introducing an **embedding-based semantic matching engine** for AI-driven recruitment systems, extending beyond keyword and TF-IDF approaches.

### 🧠 What Was Done
- Authored a **complete technical paper** titled:  
  **“Embedding-Based Semantic Matching for AI-Driven Recruitment Systems”**
- The paper presents:
  - Motivation and limitations of traditional ATS systems
  - Semantic matching using text embeddings
  - System architecture integration
  - Evaluation against TF-IDF and keyword baselines
  - Explainability and recruiter-centric insights
- Structured as a **conference-ready research paper** with abstract, methodology, results, and future work.
- Written fully in **Markdown** for reproducibility and easy conversion to PDF.

### 📄 Artifacts Created
- `papers/embedding_job_matching.md`  
  (Full technical paper in Markdown format)

### 🔗 Repository
- GitHub:  
  https://github.com/konidinasricharan/retail-anomaly-poc

### 🏆 Evidence Alignment
- **Original Contribution of Major Significance**
- **Scholarly Authorship**
- **Evidence of Advanced Expertise**
- **Research Publication (submission-ready)**

### 📌 Notes
This paper strengthens the research narrative of the AI Recruitment Suite by introducing **semantic similarity modeling**, positioning the work closer to real-world ATS and enterprise hiring platforms. It is suitable for submission to workshops, conferences, arXiv, and DOI publication platforms.

---








