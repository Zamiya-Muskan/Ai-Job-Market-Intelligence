import streamlit as st
import pandas as pd

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AI Job Market Intelligence",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# BANNER
# =====================================================

st.image(
    "assets/banner.png",
    width="stretch"
)

# =====================================================
# LOAD DATA
# =====================================================

df = pd.read_csv("data/Cleaned_engineered_jobdata.csv")

# =====================================================
# TITLE
# =====================================================
st.title("🏠 Home")

st.markdown("## 🤖 AI Job Market Intelligence Dashboard")

st.markdown("""
An interactive analytics platform that explores AI hiring trends, validates insights using
statistical analysis, forecasts future hiring demand, and helps professionals evaluate their
career readiness through an AI Skill Gap Analyzer.
""")

st.markdown("---")

# =====================================================
# DASHBOARD OVERVIEW
# =====================================================

st.subheader("📊 Dashboard Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total AI Jobs",
        f"{len(df):,}"
    )

with col2:
    st.metric(
        "Companies",
        df["Company"].nunique()
    )

with col3:
    st.metric(
        "Cities",
        df["City"].nunique()
    )

with col4:
    st.metric(
        "Forecast Horizon",
        "6 Months"
    )

st.markdown("---")

# =====================================================
# ABOUT PLATFORM
# =====================================================

st.subheader("📌 About the Platform")

st.write("""
The **AI Job Market Intelligence Dashboard** was developed to analyze AI job postings collected
between **2024 and 2026**.

The platform combines **data analytics**, **statistical analysis**, and **machine learning**
to provide meaningful insights into hiring trends, in-demand skills, emerging technologies,
future hiring forecasts, and career readiness for AI professionals.

Rather than simply visualizing data, the dashboard supports data-driven decision making for
students, job seekers, and recruiters through interactive analytics and personalized skill analysis.
""")

st.markdown("---")

# =====================================================
# PROJECT WORKFLOW
# =====================================================

st.subheader("🔄 Project Workflow")

st.markdown("""

```text
Job Market Data
        ↓
Data Cleaning
        ↓
Exploratory Data Analysis
        ↓
Feature Engineering
        ↓
Statistical Analysis
        ↓
Machine Learning Forecasting
        ↓
Interactive Dashboard
        ↓
AI Skill Gap Analyzer""")
st.markdown("---")

#=====================================================
# TECHNOLOGY STACK
#=====================================================

st.subheader("🛠 Technology Stack")

col1, col2 = st.columns(2)

with col1:

    st.info("""
### 🐍 Development

• Python

• Streamlit

• Pandas

• NumPy

• Plotly
""")

with col2:

    st.info("""
### 🤖 Machine Learning & Analytics

• XGBoost Regressor

• Scikit-learn

• Statistical Analysis

• Hypothesis Testing

• Time Series Forecasting
""")

st.markdown("---")
#=====================================================
#PROJECT HIGHLIGHTS
#=====================================================


st.subheader("⭐ Project Highlights")

st.success("""
✔ AI Job Market Analysis (2024–2026)

✔ Interactive Hiring Analytics Dashboard

✔ AI Skills Intelligence Module

✔ Statistical Analysis & Hypothesis Testing

✔ XGBoost-based Hiring Forecasting

✔ Personalized Skill Gap Analyzer

✔ Interactive Decision Support Dashboard
""")

st.markdown("---")


#=====================================================
# DASHBOARD MODULES
#=====================================================

st.subheader("🧭 Dashboard Modules")

col1, col2, col3 = st.columns(3)

with col1:

    st.success("""
### 📊 Hiring Analytics

Analyze the current AI job market.

• Hiring Trends

• Industries

• Cities

• Salaries

• Work Modes
""")

    st.success("""
### 🧠 Skills Intelligence

Discover market demand.

• Top Skills

• Skill Trends

• Emerging Technologies
""")

with col2:

    st.success("""
### 📈 Forecasting

Predict future hiring demand.

• Monthly Forecast

• Quarterly Forecast

• Job Roles

• Future Skills
""")

    st.success("""
### 📊 Statistical Analysis

Validate market insights.

• Descriptive Statistics

• Correlation Analysis

• Hypothesis Testing
""")

with col3:

    st.success("""
### 🎯 Skill Gap Analyzer

Measure career readiness.

• Select Target Role

• Compare Skills

• Skill Match Score

• Learning Roadmap
""")

    st.success("""
### 📖 About Project

Project documentation.

• Objectives

• Workflow

• Technology Stack

• ML Pipeline
""")

st.markdown("---")

#=====================================================
#FOOTER
#=====================================================

st.caption(
"🚀 Master's Project | AI Job Market Intelligence Dashboard | Developed using Python, Streamlit, Plotly, XGBoost & Statistical Analysis"
)