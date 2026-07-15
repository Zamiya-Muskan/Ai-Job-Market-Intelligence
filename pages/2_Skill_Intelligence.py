import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Skills Intelligence",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# PAGE TITLE
# =====================================================

st.title("🧠 Skills Intelligence")
st.caption("Home  >  Skill Intelligence")

st.markdown("""
Discover the technologies driving today's AI job market.
Explore the most demanded skills, monitor technology trends, and identify emerging AI competencies.
""")

st.markdown("---")

# =====================================================
# LOAD DATA
# =====================================================

df = pd.read_csv("data/Cleaned_engineered_jobdata.csv")

df["Date_Posted"] = pd.to_datetime(df["Date_Posted"])

# =====================================================
# CREATE SKILL DATASET
# =====================================================

skills_df = (
    df.assign(
        Skill=df["Skills_Required"].str.split(",")
    )
    .explode("Skill")
)

skills_df["Skill"] = skills_df["Skill"].str.strip()

skill_counts = skills_df["Skill"].value_counts()

top10 = skill_counts.head(10)

# =====================================================
# KPI CARDS
# =====================================================

st.subheader("📌 Skills Overview")

col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)

with col1:
    st.metric(
        "Unique Skills",
        skill_counts.shape[0]
    )

with col2:
    st.metric(
        "Most Demanded Skill",
        top10.index[0]
    )

with col3:
    st.metric(
        "Highest Skill Demand",
        int(top10.iloc[0])
    )

with col4:
    st.metric(
        "Average Skills / Job",
        round(df["Skill_Count"].mean(),1)
    )

with col5:
    st.metric(
        "Trending GenAI Skills",
        5
    )

with col6:
    st.metric(
        "Technology Stack",
        skill_counts.shape[0]
    )

st.markdown("---")

# =====================================================
# MOST IN-DEMAND SKILLS
# =====================================================

st.subheader("🔥 Most In-Demand Skills")

chart = top10.reset_index()
chart.columns = ["Skill", "Jobs"]

fig = px.bar(
    chart,
    x="Jobs",
    y="Skill",
    orientation="h",
    color="Jobs",
    title="Top 10 AI Skills"
)

fig.update_layout(
    yaxis=dict(categoryorder="total ascending"),
    xaxis_title="Job Postings",
    yaxis_title=""
)

st.plotly_chart(fig, width="stretch")

st.markdown("---")

# =====================================================
# SKILL DEMAND TRENDS
# =====================================================

st.subheader("📈 Skill Demand Trends")

top_skills = top10.index.tolist()[:5]

skill_ts = df.copy()

skill_ts["Month"] = (
    skill_ts["Date_Posted"]
    .dt.to_period("M")
    .astype(str)
)

trend = []

for skill in top_skills:

    temp = skill_ts[
        skill_ts["Skills_Required"]
        .str.contains(
            skill,
            case=False,
            na=False
        )
    ]

    monthly = (
        temp
        .groupby("Month")
        .size()
        .reset_index(name="Jobs")
    )

    monthly["Skill"] = skill

    trend.append(monthly)

trend = pd.concat(trend)

fig = px.line(
    trend,
    x="Month",
    y="Jobs",
    color="Skill",
    markers=True,
    title="Demand Trend of Top AI Skills"
)

fig.update_layout(
    xaxis_title="Month",
    yaxis_title="Job Postings"
)

st.plotly_chart(fig, width="stretch")

st.markdown("---")

# =====================================================
# EMERGING AI TECHNOLOGIES
# =====================================================

st.subheader("🚀 Emerging AI Technologies")

emerging = [
    "OpenAI API",
    "LangChain",
    "RAG",
    "HuggingFace",
    "Transformers"
]

trend2 = []

for skill in emerging:

    temp = skill_ts[
        skill_ts["Skills_Required"]
        .str.contains(
            skill,
            case=False,
            na=False
        )
    ]

    monthly = (
        temp
        .groupby("Month")
        .size()
        .reset_index(name="Jobs")
    )

    monthly["Skill"] = skill

    trend2.append(monthly)

trend2 = pd.concat(trend2)

fig = px.line(
    trend2,
    x="Month",
    y="Jobs",
    color="Skill",
    markers=True,
    title="Growth of Generative AI Technologies"
)

fig.update_layout(
    xaxis_title="Month",
    yaxis_title="Job Postings"
)

st.plotly_chart(fig, width="stretch")

st.markdown("---")
# =====================================================
# INDUSTRY SKILL DEMAND
# =====================================================

st.subheader("🏢 Industry Skill Demand")

industry_skill = (
    skills_df.groupby(["Industry", "Skill"])
    .size()
    .reset_index(name="Jobs")
)

industry_skill = (
    industry_skill
    .sort_values("Jobs", ascending=False)
    .groupby("Industry")
    .head(1)
)

fig = px.bar(
    industry_skill,
    x="Industry",
    y="Jobs",
    color="Skill",
    title="Most Demanded Skill Across Industries"
)

fig.update_layout(
    xaxis_title="Industry",
    yaxis_title="Job Postings"
)

st.plotly_chart(fig, width="stretch")

st.markdown("---")

# =====================================================
# TECHNOLOGY ECOSYSTEM
# =====================================================

st.subheader("🧩 AI Technology Ecosystem")

col1, col2 = st.columns(2)

with col1:

    st.info("""
### 💻 Programming

• Python

• SQL

• Java

• JavaScript
""")

    st.info("""
### 🤖 AI & Machine Learning

• Machine Learning

• Deep Learning

• TensorFlow

• PyTorch

• Scikit-learn
""")

with col2:

    st.info("""
### ☁ Cloud & DevOps

• AWS

• Azure

• Docker

• Kubernetes

• REST APIs
""")

    st.info("""
### 🧠 Generative AI

• LangChain

• OpenAI API

• HuggingFace

• RAG

• Transformers
""")

st.markdown("---")

# =====================================================
# MARKET DEMAND SNAPSHOT
# =====================================================

st.subheader("📊 Market Demand Snapshot")

left, right = st.columns(2)

with left:

    st.success(f"""
### 🔥 Core Skills

The current AI market continues to be driven by:

✔ {top10.index[0]}

✔ {top10.index[1]}

✔ {top10.index[2]}

✔ {top10.index[3]}

✔ {top10.index[4]}
""")

with right:

    st.success("""
### 🚀 Fast-Growing Technologies

✔ LangChain

✔ OpenAI API

✔ HuggingFace

✔ RAG

✔ Transformers
""")

st.markdown("---")

# =====================================================
# SKILL INTELLIGENCE SUMMARY
# =====================================================

st.subheader("💡 Skill Intelligence Summary")

top_skill = top10.index[0]

st.info(f"""
### Executive Skill Insights

🧠 **{top_skill}** remains the foundation of modern AI development and is consistently the most requested skill.

☁ Cloud technologies and containerization tools are becoming standard requirements alongside AI expertise.

🤖 Employers increasingly expect professionals to possess multiple complementary technical skills rather than expertise in a single technology.

🚀 Generative AI technologies such as **LangChain**, **OpenAI API**, **HuggingFace**, **RAG**, and **Transformers** continue to gain momentum across AI job postings.

📈 Professionals combining programming, cloud computing, machine learning, and Generative AI skills are likely to have stronger career opportunities in the evolving AI job market.
""")

st.markdown("---")

# =====================================================
# FOOTER
# =====================================================

st.caption(
    "Skills Intelligence | AI Job Market Intelligence Dashboard"
)