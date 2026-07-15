import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Hiring Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
    
)

# =====================================================
# PAGE TITLE
# =====================================================

st.title("📊 Hiring Analytics")
st.caption("Home  >  Hiring Analytics")

st.markdown("""
Explore hiring patterns across the AI job market using interactive visualizations.
Analyze recruitment trends, hiring hotspots, industry demand, salaries, and employment patterns.
""")

st.markdown("---")

# =====================================================
# LOAD DATA
# =====================================================

df = pd.read_csv("data/Cleaned_engineered_jobdata.csv")

df["Date_Posted"] = pd.to_datetime(df["Date_Posted"])

# =====================================================
# SIDEBAR FILTERS
# =====================================================

st.sidebar.header("🎛 Filter Hiring Data")

selected_year = st.sidebar.multiselect(
    "Year",
    sorted(df["Year"].unique()),
    default=sorted(df["Year"].unique())
)

selected_city = st.sidebar.multiselect(
    "City",
    sorted(df["City"].unique()),
    default=sorted(df["City"].unique())
)

selected_exp = st.sidebar.multiselect(
    "Experience Level",
    sorted(df["Experience_Level"].unique()),
    default=sorted(df["Experience_Level"].unique())
)

selected_mode = st.sidebar.multiselect(
    "Work Mode",
    sorted(df["Work_Mode"].unique()),
    default=sorted(df["Work_Mode"].unique())
)

filtered_df = df[
    (df["Year"].isin(selected_year)) &
    (df["City"].isin(selected_city)) &
    (df["Experience_Level"].isin(selected_exp)) &
    (df["Work_Mode"].isin(selected_mode))
]

# =====================================================
# KPI CARDS
# =====================================================

st.subheader("📌 Hiring Overview")

col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)

with col1:
    st.metric(
        "Total AI Jobs",
        len(filtered_df)
    )

with col2:
    st.metric(
        "Hiring Companies",
        filtered_df["Company"].nunique()
    )

with col3:
    st.metric(
        "Hiring Cities",
        filtered_df["City"].nunique()
    )

with col4:
    st.metric(
        "Average Salary",
        f"{filtered_df['Salary_LPA'].mean():.2f} LPA"
    )

with col5:

    remote_jobs = (
        filtered_df["Work_Mode"]
        .eq("Remote")
        .sum()
    )

    st.metric(
        "Remote Opportunities",
        remote_jobs
    )

with col6:
    st.metric(
        "Average Skills / Job",
        round(filtered_df["Skill_Count"].mean(),1)
    )

st.markdown("---")

# =====================================================
# HIRING TREND
# =====================================================

st.subheader("📈 AI Hiring Trend")

monthly = (
    filtered_df
    .groupby("Date_Posted")
    .size()
    .reset_index(name="Jobs")
)

fig = px.line(
    monthly,
    x="Date_Posted",
    y="Jobs",
    markers=True,
    title="Monthly AI Hiring Activity"
)

fig.update_traces(line_width=3)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Number of Job Postings"
)

st.plotly_chart(fig, width="stretch")

st.markdown("---")

# =====================================================
# LOCATION INTELLIGENCE
# =====================================================

st.subheader("🌍 Location Intelligence")

left, right = st.columns(2)

with left:

    city = (
        filtered_df["City"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    city.columns = ["City", "Jobs"]

    fig = px.bar(
        city,
        x="Jobs",
        y="City",
        orientation="h",
        color="Jobs",
        title="🏙 Hiring Hotspots"
    )

    fig.update_layout(
        yaxis=dict(categoryorder="total ascending"),
        xaxis_title="Job Postings",
        yaxis_title=""
    )

    st.plotly_chart(fig, width="stretch")

with right:

    industry = (
        filtered_df["Industry"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    industry.columns = ["Industry", "Jobs"]

    fig = px.bar(
        industry,
        x="Industry",
        y="Jobs",
        color="Jobs",
        title="🏢 Industry Demand"
    )

    fig.update_layout(
        xaxis_title="Industry",
        yaxis_title="Job Postings"
    )

    st.plotly_chart(fig, width="stretch")

st.markdown("---")
# =====================================================
# ROLE INTELLIGENCE
# =====================================================

st.subheader("💼 Role Intelligence")

left, right = st.columns(2)

with left:

    jobs = (
        filtered_df["Job_Title"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    jobs.columns = ["Job Role", "Jobs"]

    fig = px.bar(
        jobs,
        x="Jobs",
        y="Job Role",
        orientation="h",
        color="Jobs",
        title="💼 Most In-Demand Roles"
    )

    fig.update_layout(
        yaxis=dict(categoryorder="total ascending"),
        xaxis_title="Job Postings",
        yaxis_title=""
    )

    st.plotly_chart(fig, width="stretch")

with right:

    exp = (
        filtered_df["Experience_Level"]
        .value_counts()
        .reset_index()
    )

    exp.columns = ["Experience", "Jobs"]

    fig = px.pie(
        exp,
        names="Experience",
        values="Jobs",
        hole=0.5,
        title="👨‍💼 Hiring by Experience Level"
    )

    st.plotly_chart(fig, width="stretch")

st.markdown("---")

# =====================================================
# EMPLOYMENT INSIGHTS
# =====================================================

st.subheader("🏢 Employment Insights")

left, right = st.columns(2)

with left:

    work = (
        filtered_df["Work_Mode"]
        .value_counts()
        .reset_index()
    )

    work.columns = ["Work Mode", "Jobs"]

    fig = px.bar(
        work,
        x="Work Mode",
        y="Jobs",
        color="Work Mode",
        title="🏠 Workplace Preferences"
    )

    fig.update_layout(
        xaxis_title="Work Mode",
        yaxis_title="Job Postings"
    )

    st.plotly_chart(fig, width="stretch")

with right:

    jobtype = (
        filtered_df["Job_Type"]
        .value_counts()
        .reset_index()
    )

    jobtype.columns = ["Job Type", "Jobs"]

    fig = px.pie(
        jobtype,
        names="Job Type",
        values="Jobs",
        hole=0.45,
        title="📄 Employment Type"
    )

    st.plotly_chart(fig, width="stretch")

st.markdown("---")

# =====================================================
# SALARY LANDSCAPE
# =====================================================

st.subheader("💰 Salary Landscape")

fig = px.histogram(
    filtered_df,
    x="Salary_LPA",
    nbins=20,
    color_discrete_sequence=["#4C78A8"],
    title="Salary Distribution Across AI Jobs"
)

fig.update_layout(
    xaxis_title="Salary (LPA)",
    yaxis_title="Number of Job Postings"
)

st.plotly_chart(fig, width="stretch")

st.markdown("---")

# =====================================================
# KEY HIRING TAKEAWAYS
# =====================================================

st.subheader("📌 Key Hiring Takeaways")

top_city = filtered_df["City"].mode()[0]
top_role = filtered_df["Job_Title"].mode()[0]
top_industry = filtered_df["Industry"].mode()[0]
top_exp = filtered_df["Experience_Level"].mode()[0]

remote_percent = (
    filtered_df["Work_Mode"]
    .eq("Remote")
    .mean() * 100
)

avg_salary = filtered_df["Salary_LPA"].mean()

st.success(f"""
### Executive Hiring Summary

📍 **Hiring Hotspot:** **{top_city}** continues to lead AI recruitment.

💼 **Most In-Demand Role:** **{top_role}** dominates current hiring.

🏢 **Leading Industry:** **{top_industry}** recruits the largest share of AI professionals.

👨‍💼 **Preferred Experience:** Organizations primarily seek **{top_exp}** candidates.

🏠 **Remote Hiring:** Approximately **{remote_percent:.1f}%** of AI jobs offer remote work opportunities.

💰 **Average Salary:** AI professionals receive an average salary of **{avg_salary:.2f} LPA**.

📊 **Total Filtered Jobs:** **{len(filtered_df)}** job postings satisfy the selected filters.
""")

st.markdown("---")

# =====================================================
# PAGE FOOTER
# =====================================================

st.caption(
    "Hiring Analytics | AI Job Market Intelligence Dashboard"
)