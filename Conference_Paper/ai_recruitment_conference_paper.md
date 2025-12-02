# AI-Driven Recruitment System: LLM-Based Resume Scoring, Job Matching, and Hiring Recommendations  
**Author:** Sri Charan Konidina  
**Affiliation:** Independent Researcher, AI Systems  
**Date:** November 2025  

## Abstract  
This paper presents an AI-driven recruitment system that automates resume evaluation, job-description matching, candidate scoring, and hiring recommendation generation. The proposed system integrates Large Language Models (LLMs), structured scoring logic, heuristics-based preprocessing, and a Streamlit analytics dashboard. Experiments demonstrate that LLMs can provide explainable hiring insights while reducing manual screening time. The resulting system is suitable for real-world HR workflows and can be extended into a lightweight Applicant Tracking System (ATS).

## 1. Introduction  
Recruitment today requires screening hundreds of resumes per job posting. Traditional manual review is slow, inconsistent, and often subjective. AI systems—particularly LLMs—offer the potential to automate early-stage candidate evaluation while improving consistency.

This work introduces an LLM-powered recruitment analysis tool capable of:
- Resume interpretation  
- Job-fit scoring (0–100)  
- Strength & weakness identification  
- Hiring suitability explanation  
- Automated shortlist generation  
- Visual analytics  

The system contributes a structured evaluation pipeline that combines LLM reasoning with deterministic scoring extraction.

## 2. System Architecture  
The architecture consists of six core modules:

### 2.1 Resume Input Module  
Accepts multiple resumes separated by text blocks. Performs light preprocessing such as whitespace normalization.

### 2.2 Job Description Parser  
Extracts critical skills, responsibilities, and qualification patterns.

### 2.3 LLM Evaluation Engine  
Powered by *gpt-4o-mini*.  
Outputs include:  
- Match score (0–100)  
- Three strengths  
- Two improvement areas  
- Fit explanation  

### 2.4 Score Extraction Logic  
A custom parser converts LLM text into normalized score format “85/100”.  
This ensures:

- Stable sorting  
- Reliable shortlisting thresholds  
- Reproducible evaluation  

### 2.5 Shortlisting Algorithm  
Candidates meeting:
    score ≥ threshold
are shortlisted.

### 2.6 Streamlit Analytics Dashboard  
Includes:  
- Score distribution chart  
- Threshold-highlighting line  
- Full dataframe of ranked candidates  
- Recruiter summary  

This enables explainability, transparency, and interactive evaluation.

## 3. Prompting Methodology  
The system uses a structured evaluation prompt that ensures consistent output formatting. Prompt design emphasized:

- Reducing hallucinations  
- Extracting stable numeric scores  
- Achieving semantically rich candidate evaluations  

## 4. Experimental Evaluation  
The system was tested across resumes for data engineering, software engineering, cloud, ML, and security roles.

### Findings:
- Strong resumes scored 80–95  
- General resumes scored 55–70  
- Skill-light resumes scored below 50  

These patterns parallel typical ATS keyword-matching behavior, demonstrating practical utility.

## 5. Applications  
The system supports various HR and recruitment workflows:

- Talent acquisition teams  
- Staffing agencies  
- Resume review platforms  
- Candidate self-assessment tools  

Enterprise extensions include:
- Multi-role batch matching  
- Semantic embedding search  
- Automated recruiter report generation  

## 6. Future Work  
Future improvements include:  
- Embedding-based similarity scoring  
- Bias & fairness analysis  
- Calibration for role-specific weighting  
- Multi-job recommendation system  

## 7. Conclusion  
This paper demonstrates a practical AI-driven recruitment pipeline that integrates LLM reasoning, structured scoring logic, and interactive visual dashboards. The system offers a foundation for next-generation ATS platforms.

## References  
1. OpenAI API Documentation  
2. Streamlit Documentation  
3. Kaggle Datasets  
4. Industry hiring statistics (Glassdoor, Indeed)  

