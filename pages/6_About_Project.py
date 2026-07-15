import streamlit as st

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="About Project",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# PAGE HEADER
# =====================================================

st.title("📖 About Project")

st.caption("Home  >  About Project")

st.markdown("""
Learn about the project's objectives, methodology, technology stack, machine learning pipeline, and overall outcomes.
""")

st.markdown("---")

# =====================================================
# PROJECT SNAPSHOT
# =====================================================

st.subheader("📌 Project Snapshot")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Project Duration",
        "2024–2026"
    )

with c2:
    st.metric(
        "Dataset",
        "AI Job Postings"
    )

with c3:
    st.metric(
        "Forecast Horizon",
        "6 Months"
    )

with c4:
    st.metric(
        "ML Algorithm",
        "XGBoost"
    )

st.markdown("---")

# =====================================================
# PROJECT OBJECTIVES
# =====================================================

st.subheader("🎯 Project Objectives")

left, right = st.columns(2)

with left:

    st.success("""
### Business Objectives

✔ Analyze AI hiring trends

✔ Identify in-demand skills

✔ Explore hiring across industries

✔ Monitor emerging AI technologies

✔ Forecast future workforce demand
""")

with right:

    st.success("""
### Technical Objectives

✔ Data Cleaning

✔ Exploratory Data Analysis

✔ Statistical Analysis

✔ Feature Engineering

✔ Machine Learning Forecasting

✔ Interactive Dashboard
""")

st.markdown("---")

# =====================================================
# TECHNOLOGY STACK
# =====================================================

st.subheader("🛠 Technology Stack")

col1, col2, col3 = st.columns(3)

with col1:

    st.info("""
### 🐍 Data Science

• Python

• Pandas

• NumPy

• Scikit-learn
""")

with col2:

    st.info("""
### 📊 Visualization

• Plotly

• Streamlit

• Interactive Dashboards
""")

with col3:

    st.info("""
### 🤖 Machine Learning

• XGBoost

• Feature Engineering

• Time Series Forecasting

• Statistical Analysis
""")

st.markdown("---")

# =====================================================
# PROJECT WORKFLOW
# =====================================================

st.subheader("🔄 Project Workflow")

st.code("""

Raw AI Job Dataset
        │
        ▼
Data Cleaning
        │
        ▼
Feature Engineering
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Statistical Analysis
        │
        ▼
XGBoost Forecasting
        │
        ▼
Interactive Dashboard
        │
        ▼
Business Insights

""", language="text")

st.markdown("---")

# =====================================================
# MACHINE LEARNING PIPELINE
# =====================================================

st.subheader("🤖 Machine Learning Pipeline")

st.code("""

Historical Job Data (2024–2026)
            │
            ▼
Date Feature Engineering
            │
            ▼
Training Dataset
            │
            ▼
XGBoost Regressor
            │
            ▼
Future Prediction
            │
            ├────────────► Monthly Hiring
            │
            ├────────────► Quarterly Hiring
            │
            ├────────────► Job Roles
            │
            └────────────► Skill Demand

""", language="text")

st.markdown("---")

# =====================================================
# KEY OUTCOMES
# =====================================================

st.subheader("📈 Project Outcomes")

st.success("""
✔ Analyzed AI job market trends from 2024–2026.

✔ Identified the most demanded technical skills.

✔ Explored hiring patterns across cities and industries.

✔ Applied descriptive statistics and hypothesis testing.

✔ Forecasted future hiring demand using XGBoost.

✔ Predicted future job roles and skill demand.

✔ Built an interactive decision-support dashboard for AI job market analysis.
""")

st.markdown("---")

# =====================================================
# DEVELOPER
# =====================================================

st.subheader("👨‍💻 Developer")

st.info("""
### AI Job Market Intelligence Dashboard

**Developer:** Zamiya Muskan


**Domain:** Data Analytics • Machine Learning • Forecasting

**Tools:** Python • Streamlit • Plotly • XGBoost
""")

st.markdown("---")

st.caption("AI Job Market Intelligence Dashboard | Master's Major Project")