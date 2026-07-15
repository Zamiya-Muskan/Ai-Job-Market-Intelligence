import streamlit as st
import pandas as pd
import plotly.express as px
from scipy.stats import skew, kurtosis
from scipy.stats import pearsonr, f_oneway

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Statistical Analysis",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# PAGE HEADER
# =====================================================

st.title("📊 Statistical Analysis")
st.caption("Home  >  Statistical Analysis")

st.markdown("""
Explore the statistical characteristics of the AI Job Market dataset through descriptive statistics,
distribution analysis, correlation analysis, and hypothesis testing.
""")

st.markdown("---")

# =====================================================
# LOAD DATA
# =====================================================

df = pd.read_csv("data/Cleaned_engineered_jobdata.csv")

salary = df["Salary_LPA"]

# =====================================================
# QUICK STATISTICS
# =====================================================

st.subheader("📌 Quick Statistics")

mean_salary = salary.mean()
median_salary = salary.median()
std_salary = salary.std()
avg_skill = df["Skill_Count"].mean()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Average Salary",
        f"{mean_salary:.2f} LPA"
    )

with col2:
    st.metric(
        "Median Salary",
        f"{median_salary:.2f} LPA"
    )

with col3:
    st.metric(
        "Std. Deviation",
        f"{std_salary:.2f}"
    )

with col4:
    st.metric(
        "Average Skills / Job",
        f"{avg_skill:.1f}"
    )

st.markdown("---")

# =====================================================
# STATISTICAL METHODS
# =====================================================

st.subheader("📚 Statistical Methods Used")

methods = pd.DataFrame({
    "Technique": [
        "Descriptive Statistics",
        "Skewness & Kurtosis",
        "Pearson Correlation",
        "One-Way ANOVA"
    ],
    "Purpose": [
        "Summarize salary distribution",
        "Analyze salary distribution shape",
        "Measure relationship between Skill Count and Salary",
        "Compare salaries across Experience Levels"
    ]
})

st.dataframe(
    methods,
    hide_index=True,
    width="stretch"
)

st.markdown("---")

# =====================================================
# SALARY DISTRIBUTION
# =====================================================

st.subheader("💰 Salary Distribution")

left, right = st.columns(2)

with left:

    fig = px.box(
        df,
        y="Salary_LPA",
        points="outliers",
        title="Salary Spread"
    )

    fig.update_layout(
        yaxis_title="Salary (LPA)"
    )

    st.plotly_chart(fig, width="stretch")

with right:

    fig = px.histogram(
        df,
        x="Salary_LPA",
        nbins=25,
        marginal="box",
        title="Salary Frequency Distribution"
    )

    fig.update_layout(
        xaxis_title="Salary (LPA)",
        yaxis_title="Number of Jobs"
    )

    st.plotly_chart(fig, width="stretch")

st.info(f"""
### Distribution Summary

**Mean Salary:** **{mean_salary:.2f} LPA**

**Median Salary:** **{median_salary:.2f} LPA**

**Standard Deviation:** **{std_salary:.2f}**

The salary distribution indicates the overall compensation pattern of AI jobs, while the box plot highlights the spread and potential high-paying outliers.
""")

st.markdown("---")

# =====================================================
# DISTRIBUTION METRICS
# =====================================================

st.subheader("📈 Distribution Metrics")

skewness = skew(salary)
kurt = kurtosis(salary)

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Skewness",
        f"{skewness:.2f}"
    )

with col2:

    st.metric(
        "Kurtosis",
        f"{kurt:.2f}"
    )

st.markdown("#### Statistical Formula")

st.latex(r"Skewness=\frac{E[(X-\mu)^3]}{\sigma^3}")

st.latex(r"Kurtosis=\frac{E[(X-\mu)^4]}{\sigma^4}-3")

if skewness > 0:
    skew_text = "Right-skewed"
else:
    skew_text = "Left-skewed"

st.success(f"""
### Interpretation

**Calculated Skewness:** **{skewness:.2f}**

**Calculated Kurtosis:** **{kurt:.2f}**

**Distribution:** **{skew_text}**

The salary distribution contains a small number of premium-paying AI jobs that influence the overall distribution.
""")

st.markdown("---")
# =====================================================
# CORRELATION ANALYSIS
# =====================================================

st.subheader("📈 Correlation Analysis: Skill Count vs Salary")

fig = px.scatter(
    df,
    x="Skill_Count",
    y="Salary_LPA",
    trendline="ols",
    opacity=0.75,
    title="Skill Count vs Salary"
)

fig.update_layout(
    xaxis_title="Number of Skills Required",
    yaxis_title="Salary (LPA)"
)

st.plotly_chart(fig, width="stretch")

corr, p_value = pearsonr(
    df["Skill_Count"],
    df["Salary_LPA"]
)

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Pearson Correlation (r)",
        f"{corr:.3f}"
    )

with col2:
    st.metric(
        "P-value",
        f"{p_value:.5f}"
    )

st.markdown("#### Pearson Correlation Formula")

st.latex(r"r=\frac{\sum (x-\bar{x})(y-\bar{y})}{\sqrt{\sum(x-\bar{x})^2\sum(y-\bar{y})^2}}")

if abs(corr) < 0.30:
    strength = "Weak"
elif abs(corr) < 0.70:
    strength = "Moderate"
else:
    strength = "Strong"

decision = "Reject H₀" if p_value < 0.05 else "Fail to Reject H₀"

st.success(f"""
### Hypothesis Test

**H₀:** Skill Count and Salary are not significantly related.

**H₁:** Skill Count and Salary are significantly related.

---

**Calculated r:** **{corr:.3f}**

**Calculated p-value:** **{p_value:.5f}**

**Relationship:** **{strength} Positive Correlation**

**Decision:** **{decision}**

**Conclusion:** Jobs requiring more skills generally tend to offer higher salaries.
""")

st.markdown("---")

# =====================================================
# ANOVA
# =====================================================

st.subheader("🧪 ANOVA: Experience Level vs Salary")

fig = px.box(
    df,
    x="Experience_Level",
    y="Salary_LPA",
    color="Experience_Level",
    title="Salary Distribution by Experience Level"
)

fig.update_layout(
    showlegend=False,
    xaxis_title="Experience Level",
    yaxis_title="Salary (LPA)"
)

st.plotly_chart(fig, width="stretch")

groups = [
    g["Salary_LPA"].values
    for _, g in df.groupby("Experience_Level")
]

f_stat, p_anova = f_oneway(*groups)

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "F Statistic",
        f"{f_stat:.2f}"
    )

with col2:
    st.metric(
        "P-value",
        f"{p_anova:.5f}"
    )

st.markdown("#### ANOVA Test Formula")

st.latex(r"F=\frac{\mathrm{Variance\ Between\ Groups}}{\mathrm{Variance\ Within\ Groups}}")

decision = "Reject H₀" if p_anova < 0.05 else "Fail to Reject H₀"

st.success(f"""
### Hypothesis Test

**H₀:** Mean salaries are equal across all experience levels.

**H₁:** At least one experience level has a different mean salary.

---

**Calculated F:** **{f_stat:.2f}**

**Calculated p-value:** **{p_anova:.5f}**

**Decision:** **{decision}**

**Conclusion:** Experience level has a statistically significant impact on salary.
""")

st.markdown("---")

# =====================================================
# KEY STATISTICAL FINDINGS
# =====================================================

st.subheader("📌 Key Statistical Findings")

st.success(f"""
✔ **Average Salary:** {mean_salary:.2f} LPA

✔ Salary distribution is **{skew_text.lower()}** with a few premium-paying AI jobs.

✔ Pearson Correlation = **{corr:.3f}**, indicating a **{strength.lower()} positive relationship** between Skill Count and Salary.

✔ ANOVA confirms that salary differs significantly across experience levels.

✔ The results suggest that both **technical skill diversity** and **professional experience** contribute to higher salaries in the AI job market.
""")

st.caption("Statistical Analysis | AI Job Market Intelligence Dashboard")