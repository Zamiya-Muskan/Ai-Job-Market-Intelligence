import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Forecasting",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# PAGE HEADER
# =====================================================

st.title("📈 AI Job Market Forecasting")
st.caption("Home  >  Forecasting")

st.markdown("""
Predict future AI hiring demand, workforce requirements, and technology trends using an **XGBoost Regression** model trained on AI job market data from **2024–2026**.
""")

st.markdown("---")

# =====================================================
# LOAD DATA
# =====================================================

job_month = pd.read_csv("data/Job_forecast.csv")
job_quarter = pd.read_csv("data/quarterly_job_forecast.csv")
job_year = pd.read_csv("data/yearly_job_forecast.csv")

role_month = pd.read_csv("data/job_role_forecast.csv")

skill_month = pd.read_csv("data/top_skills_forecast.csv")

emerging_month = pd.read_csv("data/emerging_skills_forecast.csv")

job_month["Date_Posted"] = pd.to_datetime(job_month["Date_Posted"])

# =====================================================
# FORECAST OVERVIEW
# =====================================================

st.subheader("📌 Forecast Overview")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Forecast Period",
        "Jul – Dec 2026"
    )

with c2:
    st.metric(
        "Forecast Horizon",
        "6 Months"
    )

with c3:
    st.metric(
        "ML Model",
        "XGBoost"
    )

with c4:
    st.metric(
        "Prediction Level",
        "Monthly"
    )

st.markdown("---")

# =====================================================
# FORECAST METHODOLOGY
# =====================================================

st.subheader("🧠 Forecast Methodology")

st.info("""
Historical AI Job Data (2024–2026)

⬇

Data Cleaning & Feature Engineering

⬇

XGBoost Regression Model

⬇

Future Hiring Prediction

⬇

Job Demand • Skills • Emerging Technologies
""")

st.markdown("---")

# =====================================================
# HIRING DEMAND FORECAST
# =====================================================

st.subheader("📊 Hiring Demand Forecast")

left, right = st.columns(2)

with left:

    fig = px.line(
        job_month,
        x="Date_Posted",
        y="Job_Count",
        markers=True,
        title="Monthly Hiring Forecast"
    )

    fig.update_traces(
        line_width=4,
        marker_size=9
    )

    fig.update_layout(
        xaxis_title="Month",
        yaxis_title="Predicted Job Postings"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

with right:

    fig = px.bar(
        job_quarter,
        x="Quarter",
        y="Job_Count",
        color="Job_Count",
        title="Quarterly Hiring Forecast",
        text="Job_Count"
    )

    fig.update_layout(
        xaxis_title="Quarter",
        yaxis_title="Predicted Job Postings",
        coloraxis_showscale=False
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

highest_month = job_month.loc[
    job_month["Job_Count"].idxmax(),
    "Date_Posted"
]

highest_jobs = job_month["Job_Count"].max()

st.success(f"""
### Hiring Outlook

**Peak Hiring Month:** **{highest_month.strftime('%B %Y')}**

**Predicted Job Postings:** **{highest_jobs:.0f}**

The model forecasts a stable hiring trend throughout the six-month forecast period, indicating continued demand for AI professionals.
""")

st.markdown("---")
# =====================================================
# FUTURE WORKFORCE DEMAND
# =====================================================

st.subheader("💼 Future Workforce Demand")

role_long = role_month.melt(
    id_vars="Date",
    var_name="Job Role",
    value_name="Demand"
)

fig = px.bar(
    role_long,
    x="Date",
    y="Demand",
    color="Job Role",
    barmode="group",
    title="Projected Demand by Job Role"
)

fig.update_layout(
    xaxis_title="Forecast Month",
    yaxis_title="Predicted Demand"
)

st.plotly_chart(
    fig,
    width="stretch"
)

top_future_role = (
    role_month.drop(columns="Date")
    .sum()
    .idxmax()
)

st.info(f"""
**Highest Projected Role:** **{top_future_role}**

The forecast suggests that this role will continue to dominate AI hiring throughout the forecast period.
""")

st.markdown("---")

# =====================================================
# FUTURE SKILLS DEMAND
# =====================================================

st.subheader("🧠 Future Skills Demand")

selected_month = st.selectbox(
    "Select Forecast Month",
    skill_month["Date"].unique()
)

month_data = skill_month[
    skill_month["Date"] == selected_month
]

plot_df = month_data.melt(
    id_vars="Date",
    var_name="Skill",
    value_name="Demand"
)

plot_df = plot_df.sort_values("Demand")

fig = px.bar(
    plot_df,
    x="Demand",
    y="Skill",
    orientation="h",
    color="Demand",
    text="Demand",
    title=f"Predicted Skill Demand ({selected_month})"
)

fig.update_layout(
    height=550,
    coloraxis_showscale=False,
    xaxis_title="Predicted Demand",
    yaxis_title="Skill"
)

fig.update_traces(
    textposition="outside"
)

st.plotly_chart(
    fig,
    width="stretch"
)

top_future_skill = (
    skill_month.drop(columns="Date")
    .sum()
    .idxmax()
)

st.success(f"""
**Most In-Demand Skill:** **{top_future_skill}**

The model predicts that this skill will remain one of the most valuable competencies in the AI job market.
""")

st.markdown("---")

# =====================================================
# EMERGING AI TECHNOLOGIES
# =====================================================

st.subheader("🚀 Emerging AI Technologies")

emerging_long = emerging_month.melt(
    id_vars="Date",
    var_name="Skill",
    value_name="Demand"
)

fig = px.line(
    emerging_long,
    x="Date",
    y="Demand",
    color="Skill",
    markers=True,
    title="Emerging Technology Growth"
)

fig.update_layout(
    xaxis_title="Forecast Month",
    yaxis_title="Predicted Demand"
)

st.plotly_chart(
    fig,
    width="stretch"
)

fastest_skill = (
    emerging_month.drop(columns="Date")
    .sum()
    .idxmax()
)

st.info(f"""
**Fastest Growing Technology:** **{fastest_skill}**

Emerging AI technologies continue to gain momentum, indicating increasing adoption by employers.
""")

st.markdown("---")

# =====================================================
# FORECAST SUMMARY
# =====================================================

st.subheader("📅 Forecast Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Forecast Year",
        int(job_year["Year"].iloc[0])
    )

with col2:
    st.metric(
        "Predicted AI Jobs",
        f"{job_year['Job_Count'].iloc[0]:,.0f}"
    )

with col3:
    st.metric(
        "Forecast Horizon",
        "6 Months"
    )

st.markdown("---")

# =====================================================
# EXECUTIVE FORECAST INSIGHTS
# =====================================================

st.subheader("📌 Executive Forecast Insights")

highest_month = job_month.loc[
    job_month["Job_Count"].idxmax(),
    "Date_Posted"
]

highest_jobs = job_month["Job_Count"].max()

st.success(f"""
### AI Job Market Outlook

✔ Peak hiring is expected in **{highest_month.strftime('%B %Y')}**, with approximately **{highest_jobs:.0f}** predicted job postings.

✔ **{top_future_role}** is projected to remain the leading AI job role.

✔ **{top_future_skill}** continues to dominate future technical skill demand.

✔ **{fastest_skill}** is expected to experience strong growth among emerging AI technologies.

✔ Overall, the forecast indicates a stable and positive hiring outlook for the AI job market during **July–December 2026**.
""")

st.caption("Forecasting Module | AI Job Market Intelligence Dashboard")