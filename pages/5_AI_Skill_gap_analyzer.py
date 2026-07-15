import streamlit as st
import pandas as pd

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AI Skill Gap Analyzer",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# PAGE TITLE
# =====================================================

st.title("🎯 AI Skill Gap Analyzer")
st.caption("Home  >  AI Skill Gap Analyzer")

st.markdown("""
Analyze your current skills, identify missing competencies, and receive personalized
learning recommendations based on AI job market demand.
""")

st.markdown("---")

# =====================================================
# LOAD DATA
# =====================================================

df = pd.read_csv("data/Cleaned_engineered_jobdata.csv")

# =====================================================
# TARGET JOB ROLE
# =====================================================

st.subheader("💼 Select Your Target Career")

job_roles = sorted(df["Job_Title"].dropna().unique())

selected_role = st.selectbox(
    "Target Job Role",
    job_roles
)

# =====================================================
# CURRENT SKILLS
# =====================================================

all_skills = (
    df["Skills_Required"]
    .dropna()
    .str.split(",")
    .explode()
    .str.strip()
    .sort_values()
    .unique()
)

selected_skills = st.multiselect(
    "🧠 Select Your Current Skills",
    all_skills,
    placeholder="Search and select your skills..."
)

st.caption("💡 Tip: Use the search box to quickly find your skills.")

st.markdown("---")

# =====================================================
# SKILL ANALYSIS
# =====================================================

role_df = df[df["Job_Title"] == selected_role]

role_skills = (
    role_df["Skills_Required"]
    .str.split(",")
    .explode()
    .str.strip()
)

top_role_skills = role_skills.value_counts().head(10)

required_skills = list(top_role_skills.index)

matched = [
    skill
    for skill in required_skills
    if skill in selected_skills
]

missing = [
    skill
    for skill in required_skills
    if skill not in selected_skills
]

match_percentage = (
    len(matched) / len(required_skills)
) * 100

# =====================================================
# MATCH SCORE
# =====================================================

st.subheader("📊 Current Market Readiness")

st.progress(match_percentage / 100)

st.metric(
    label="Skill Match",
    value=f"{match_percentage:.0f}%"
)

st.markdown("---")

# =====================================================
# MATCHED VS MISSING SKILLS
# =====================================================

left, right = st.columns(2)

with left:

    st.success("### ✅ Your Strengths")

    if matched:
        for skill in matched:
            st.write(f"✔ {skill}")
    else:
        st.write("No matching skills selected yet.")

with right:

    st.warning("### 📈 Priority Skills to Learn")

    if missing:
        for skill in missing:
            st.write(f"➜ {skill}")
    else:
        st.success("Excellent! You already possess all the top required skills.")

st.markdown("---")

# =====================================================
# LEARNING ROADMAP
# =====================================================

st.subheader("📚 Personalized Learning Roadmap")

if missing:

    for i, skill in enumerate(missing, 1):
        st.write(f"**Step {i}:** Learn **{skill}**")

    st.success(
        "🚀 Completing these skills will significantly improve your readiness for this role."
    )

else:

    st.success(
        "🎉 Congratulations! You already possess the key skills required for this role."
    )

st.markdown("---")

# =====================================================
# MARKET INSIGHT
# =====================================================

st.info(f"""
### 💼 Market Insight

The **{selected_role}** role most frequently requires the following skills:

**{', '.join(required_skills)}**

Your current profile matches **{match_percentage:.0f}%** of the most demanded skills for this role.

Learning the recommended skills above will improve your competitiveness and align your profile with current AI job market expectations.
""")

st.markdown("---")

# =====================================================
# ROLE-SPECIFIC CAREER ACTION PLANS
# =====================================================

career_plans = {

    "AI Engineer": [
        "Strengthen Machine Learning and Deep Learning fundamentals.",
        "Learn LangChain, RAG, HuggingFace and LLM applications.",
        "Build an end-to-end AI application and deploy it using Streamlit.",
        "Practice ML model deployment and MLOps basics.",
        "Apply for AI Engineer and Generative AI roles."
    ],

    "Data Scientist": [
        "Improve Statistics, Machine Learning and Feature Engineering.",
        "Build predictive analytics and classification projects.",
        "Practice model evaluation and data storytelling.",
        "Learn Power BI or Tableau for visualization.",
        "Apply for Data Scientist roles."
    ],

    "Machine Learning Engineer": [
        "Master Scikit-learn, XGBoost and Deep Learning frameworks.",
        "Learn Docker, FastAPI and ML model deployment.",
        "Build production-ready ML applications.",
        "Practice model optimization and deployment.",
        "Apply for Machine Learning Engineer positions."
    ],

    "Python Developer": [
        "Strengthen Python programming fundamentals.",
        "Build REST APIs using Flask or FastAPI.",
        "Learn Docker, Git and SQL.",
        "Develop automation and backend projects.",
        "Apply for Python Developer roles."
    ],

    "Backend Developer": [
        "Master REST APIs and backend architecture.",
        "Learn Docker, AWS and database optimization.",
        "Build scalable backend applications.",
        "Practice SQL and system design interview questions.",
        "Apply for Backend Developer positions."
    ],

    "Software Engineer": [
        "Strengthen Data Structures and Algorithms.",
        "Practice object-oriented programming and system design.",
        "Build scalable software projects.",
        "Learn cloud deployment and CI/CD basics.",
        "Apply for Software Engineer roles."
    ],

    "Full Stack Developer": [
        "Strengthen frontend and backend development skills.",
        "Build full-stack web applications.",
        "Learn React, APIs and cloud deployment.",
        "Create portfolio projects with authentication and databases.",
        "Apply for Full Stack Developer roles."
    ]
}

# =====================================================
# CAREER ACTION PLAN
# =====================================================

# =====================================================
# CAREER ACTION PLAN
# =====================================================

st.subheader("🚀 Personalized Career Action Plan")

plan = career_plans.get(
    selected_role,
    [
        "Continue strengthening your technical skills.",
        "Complete the recommended skills listed above.",
        "Build at least one end-to-end project related to your target role.",
        "Publish your projects on GitHub with proper documentation.",
        "Practice interview questions and stay updated with AI job market trends."
    ]
)

st.success(f"### Recommendations for **{selected_role}**")

for step in plan:
    st.write(f"✔ {step}")

st.markdown("---")

# =====================================================
# FOOTER
# =====================================================

st.caption(
    "Skill recommendations are generated from historical AI job postings and market trend analysis."
)