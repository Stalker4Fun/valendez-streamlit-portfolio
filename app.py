import streamlit as st
import pandas as pd
import numpy as np
import datetime
import os

# ==============================================================================
# 1. PAGE CONFIGURATION & THEME
# ==============================================================================
st.set_page_config(
    page_title="Denzel B. Valendez | Portfolio & Autobiography",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced Modern Styling (Glassmorphism, Gradients, Polished Cards)
st.markdown("""
<style>
    /* Global Typography & Transitions */
    html, body, [class*="css"] {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    }
    
    /* Hero Header Container */
    .hero-container {
        padding: 1.8rem 2.2rem;
        border-radius: 18px;
        background: linear-gradient(135deg, rgba(2, 132, 199, 0.12) 0%, rgba(99, 102, 241, 0.08) 50%, rgba(14, 165, 233, 0.04) 100%);
        border: 1px solid rgba(2, 132, 199, 0.28);
        box-shadow: 0 10px 30px -10px rgba(2, 132, 199, 0.12);
        margin-bottom: 1.5rem;
        backdrop-filter: blur(12px);
    }
    
    .hero-title {
        margin: 0.3rem 0;
        font-size: 2.5rem;
        font-weight: 800;
        letter-spacing: -0.03em;
        background: linear-gradient(135deg, #0284c7 0%, #1e40af 50%, #4338ca 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .hero-subtitle {
        margin: 0;
        color: #475569;
        font-size: 1.15rem;
        font-weight: 500;
    }
    
    /* Solid Brand Pill Badges */
    .badge {
        display: inline-block;
        padding: 0.32rem 0.85rem;
        border-radius: 9999px;
        font-size: 0.82rem;
        font-weight: 700;
        letter-spacing: 0.02em;
        background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
        color: #ffffff !important;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
        box-shadow: 0 2px 8px rgba(2, 132, 199, 0.35);
        border: none;
    }
    
    /* Subtle Pill Badges for Tech Stack */
    .badge-subtle {
        display: inline-block;
        padding: 0.25rem 0.7rem;
        border-radius: 9999px;
        font-size: 0.78rem;
        font-weight: 600;
        background-color: rgba(2, 132, 199, 0.08);
        color: #0284c7 !important;
        margin-right: 0.4rem;
        margin-bottom: 0.4rem;
        border: 1px solid rgba(2, 132, 199, 0.25);
    }
    
    /* KPI Metric Cards */
    div[data-testid="stMetric"] {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.7) 0%, rgba(240, 249, 255, 0.7) 100%);
        padding: 1.1rem 1.3rem;
        border-radius: 14px;
        border: 1px solid rgba(186, 230, 253, 0.7);
        box-shadow: 0 4px 15px -3px rgba(2, 132, 199, 0.06);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    
    div[data-testid="stMetric"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px -3px rgba(2, 132, 199, 0.12);
        border-color: rgba(2, 132, 199, 0.4);
    }
    
    div[data-testid="stMetricValue"] {
        font-size: 1.95rem;
        font-weight: 800;
        color: #0284c7;
        letter-spacing: -0.02em;
    }
    
    /* Project Cards */
    .project-card {
        padding: 1.5rem;
        border-radius: 16px;
        border: 1px solid rgba(226, 232, 240, 0.9);
        background: linear-gradient(180deg, rgba(255, 255, 255, 0.9) 0%, rgba(248, 250, 252, 0.8) 100%);
        box-shadow: 0 4px 20px -4px rgba(0, 0, 0, 0.05);
        margin-bottom: 1.4rem;
        transition: all 0.25s ease;
    }
    
    .project-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 28px -6px rgba(2, 132, 199, 0.14);
        border-color: rgba(2, 132, 199, 0.45);
    }
    
    .project-card h3 {
        margin-top: 0;
        margin-bottom: 0.6rem;
        color: #0f172a;
        font-weight: 700;
    }
    
    /* Tabs Design */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        border-bottom: 2px solid #e2e8f0;
        padding-bottom: 4px;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 10px 10px 0 0;
        padding: 8px 18px;
        font-weight: 600;
        font-size: 0.95rem;
    }
    
    /* Sidebar Profile Card */
    .sidebar-profile {
        padding: 1.2rem;
        border-radius: 14px;
        background: linear-gradient(135deg, rgba(2, 132, 199, 0.06) 0%, rgba(241, 245, 249, 0.6) 100%);
        border: 1px solid rgba(2, 132, 199, 0.2);
        margin-bottom: 1.2rem;
        text-align: center;
    }
    
    /* Active Nav Banner */
    .nav-banner {
        padding: 0.6rem 1rem;
        border-radius: 10px;
        background: rgba(2, 132, 199, 0.08);
        border-left: 4px solid #0284c7;
        margin-bottom: 1.2rem;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# 2. SESSION STATE INITIALIZATION
# ==============================================================================
if "feedbacks" not in st.session_state:
    st.session_state.feedbacks = [
        {
            "name": "Prof. Applied AI",
            "email": "faculty@university.edu.ph",
            "category": "Academic Review",
            "rating": 5,
            "message": "Impressive portfolio showcasing your FIES regression and clustering projects!",
            "time": "2026-10-25 14:30"
        }
    ]

if "cheer_count" not in st.session_state:
    st.session_state.cheer_count = 42

if "nav_section" not in st.session_state:
    st.session_state.nav_section = "🌟 Complete Portfolio (All Sections)"

# ==============================================================================
# 3. SIDEBAR: PROFILE & FUNCTIONAL NAVIGATION
# ==============================================================================
with st.sidebar:
    st.markdown("### 👨‍💻 Student Profile")
    
    # Profile Photo or stand-in
    image_paths = ["assets/profile.png", "../portfolio_app/assets/profile.png"]
    found_img = False
    for p in image_paths:
        if os.path.exists(p):
            st.image(p, caption="Denzel B. Valendez — Profile Stand-in", use_container_width=True)
            found_img = True
            break
    if not found_img:
        st.info("📷 **[Profile Stand-in]** Denzel B. Valendez")

    st.markdown("## **Denzel B. Valendez**")
    st.caption("🎓 **BS Information Technology — 3rd Year**")
    st.markdown("""
    **Course:** CSIT 349 • Applied AI  
    **Section:** `GO1` (TeamBangan)  
    **Specialization:** Data Science & Applied AI  
    **Location:** 🇵🇭 Philippines
    """)
    
    st.divider()
    
    # FULLY FUNCTIONAL QUICK NAVIGATION
    st.markdown("### 🧭 Quick Navigation")
    
    nav_options = [
        "🌟 Complete Portfolio (All Sections)",
        "👤 About & Autobiography",
        "⚡ Skills & Analytics",
        "💼 Featured Projects",
        "📬 Contact & Feedback"
    ]
    
    # Radio navigation that actively switches or focuses sections
    nav_selection = st.radio(
        "Select section to view:",
        nav_options,
        index=nav_options.index(st.session_state.nav_section) if st.session_state.nav_section in nav_options else 0,
        key="nav_radio"
    )
    st.session_state.nav_section = nav_selection
    
    st.divider()

    # Interactive feature: Cheer Button
    st.markdown("### 🌟 Support & Kudos")
    if st.button("👏 Send Kudos / Cheer", use_container_width=True):
        st.session_state.cheer_count += 1
        st.toast(f"Thank you! Total kudos: {st.session_state.cheer_count}", icon="🎉")
    st.caption(f"Total community kudos: **{st.session_state.cheer_count}**")

    st.divider()
    
    # Resume Download Button (Extra Component)
    resume_text = """DENZEL B. VALENDEZ
BS Information Technology - 3rd Year | Section GO1
CSIT 349: Applied AI
Contact: denzelvalendez73@gmail.com

SUMMARY:
Passionate IT undergraduate specializing in Applied AI, data analysis, and machine learning.
Experienced in statistical modeling (PSA FIES regression analysis), clustering (K-Means),
and association rule mining (Apriori algorithm).

CORE SKILLS:
- Languages: Python, SQL, JavaScript, HTML/CSS
- AI/Data: Pandas, NumPy, Scikit-learn, Matplotlib, Streamlit
- Tools: Git, VS Code, Jupyter Notebook, Microsoft Office

PROJECTS:
1. Philippine Regional FIES Analysis (Linear Regression, R² = 0.924)
2. Iris Unsupervised K-Means Clustering & WCSS Analysis
3. Retail Market Basket Association Mining (Apriori Algorithm)
4. Interactive Streamlit Portfolio Dashboard
"""
    st.download_button(
        label="📄 Download Summary CV (.txt)",
        data=resume_text,
        file_name="Denzel_Valendez_CV.txt",
        mime="text/plain",
        use_container_width=True
    )

# Determine what sections to display based on navigation selection
show_all = (st.session_state.nav_section == "🌟 Complete Portfolio (All Sections)")
show_about = show_all or (st.session_state.nav_section == "👤 About & Autobiography")
show_skills = show_all or (st.session_state.nav_section == "⚡ Skills & Analytics")
show_projects = show_all or (st.session_state.nav_section == "💼 Featured Projects")
show_contact = show_all or (st.session_state.nav_section == "📬 Contact & Feedback")

# ==============================================================================
# 4. MAIN CONTENT HEADER & HERO
# ==============================================================================
st.markdown("""
<div class="hero-container">
    <div>
        <span class="badge">CSIT 349 Applied AI</span>
        <span class="badge">Section GO1</span>
    </div>
    <h1 class="hero-title">Denzel B. Valendez</h1>
    <h4 class="hero-subtitle">
        Aspiring AI Engineer • Data Analyst • BSIT 3rd Year Student
    </h4>
</div>
""", unsafe_allow_html=True)

# Navigation status banner when viewing a specific section
if not show_all:
    c_banner1, c_banner2 = st.columns([4, 1])
    with c_banner1:
        st.info(f"🔎 Currently viewing focused section: **{st.session_state.nav_section}**")
    with c_banner2:
        if st.button("👁️ Show All Sections", use_container_width=True):
            st.session_state.nav_section = "🌟 Complete Portfolio (All Sections)"
            st.rerun()

# High-level Metrics Row (st.metric & st.columns)
col_m1, col_m2, col_m3, col_m4 = st.columns(4)
with col_m1:
    st.metric(label="Academic Standing", value="3rd Year", delta="Section GO1")
with col_m2:
    st.metric(label="AI & ML Projects", value="4 Completed", delta="+2 In Progress")
with col_m3:
    st.metric(label="Core Regression R²", value="0.924", delta="FIES 2023 Model")
with col_m4:
    st.metric(label="Skills Mastered", value="10+ Tools", delta="Python Ecosystem")

st.divider()

# ==============================================================================
# 5. SECTION: ABOUT ME & AUTOBIOGRAPHY
# ==============================================================================
if show_about:
    st.header("👤 About Me & Autobiography")
    
    # Interactive bio toggle (st.checkbox)
    show_detailed_bio = st.checkbox("Show extended personal reflections", value=True)

    # Tabs for structured Autobiography (st.tabs)
    tab_story, tab_edu, tab_interests, tab_milestones = st.tabs([
        "📖 Personal Background",
        "🎓 Education Journey",
        "💡 Passions & Interests",
        "🏆 Milestones & Timeline"
    ])

    with tab_story:
        col_bio1, col_bio2 = st.columns([2, 1])
        with col_bio1:
            st.subheader("My Tech Journey")
            st.write("""
            Hello! I'm **Denzel B. Valendez**, an Information Technology student enrolled in **CSIT 349 (Applied AI)**, 
            representing **Section GO1**. My passion for computing started with simple curiosity about how digital systems 
            and automation shape everyday decisions. 
            
            Over the past three years, that curiosity evolved into a dedicated pursuit of **Applied Artificial Intelligence** 
            and **Data Science**. Whether it's wrangling complex national demographic datasets, building predictive 
            linear models, or developing intuitive user interfaces with Streamlit, I enjoy transforming raw information 
            into clear, impactful narratives.
            """)
            if show_detailed_bio:
                st.info("""
                *Philosophy:* "Technology is at its best when it solves tangible human problems — from understanding household 
                economics across regions to streamlining automated intelligence."
                """)
        with col_bio2:
            st.markdown("#### 📌 Quick Highlights")
            st.markdown("""
            - **Full Name:** Denzel B. Valendez
            - **Program:** BS Information Technology
            - **Class Section:** GO1 (TeamBangan)
            - **Focus Areas:** Predictive Modeling, ML, Python
            - **Favorite Framework:** Streamlit & Scikit-learn
            """)
            # Interactive Celebration Button (st.button, st.balloons)
            if st.button("🎉 Celebrate Milestone!"):
                st.balloons()
                st.success("Cheers to lifelong learning and Applied AI!")

    with tab_edu:
        st.subheader("Academic Path & Courses")
        st.write("""
        I am currently in my **3rd year** of the Bachelor of Science in Information Technology (BSIT) program. 
        Throughout my academic coursework, I have built a strong theoretical and practical foundation across:
        """)
        edu_data = {
            "Course Code": ["CSIT 349", "IT 211", "IT 222", "IT 314", "IT 321"],
            "Course Description": [
                "Applied Artificial Intelligence (Machine Learning, Regression & Clustering)",
                "Data Structures and Algorithms",
                "Database Management Systems & Advanced SQL",
                "Web Systems and Technologies",
                "Information Assurance and Security"
            ],
            "Academic Year": ["2026 - Present", "2024 - 2025", "2024 - 2025", "2025 - 2026", "2025 - 2026"],
            "Key Project / Takeaway": [
                "PSA FIES Regression Model, Iris K-Means, Apriori Mining",
                "Algorithmic complexity (Big-O) and efficient data structures",
                "Relational database design, normalization, query optimization",
                "Full-stack web application development and REST APIs",
                "Cybersecurity fundamentals, access controls, risk evaluation"
            ]
        }
        st.table(pd.DataFrame(edu_data))

    with tab_interests:
        st.subheader("What Drives Me")
        col_i1, col_i2 = st.columns(2)
        with col_i1:
            st.markdown("#### 🤖 Artificial Intelligence & Analytics")
            st.write("""
            - **Predictive Analytics:** Discovering mathematical relationships in real-world socioeconomic data.
            - **Unsupervised Learning:** Pattern detection via clustering algorithms (K-Means, Hierarchical).
            - **Association Rule Learning:** Exploring transaction behavior through Apriori principles.
            """)
        with col_i2:
            st.markdown("#### 💻 Software & Creative Pursuits")
            st.write("""
            - **Interactive Web Dashboards:** Rapid prototyping using modern Python libraries like Streamlit.
            - **Continuous Growth:** Exploring open-source tools, Kaggle challenges, and developer forums.
            - **Recreation:** Casual tech podcasts, strategic gaming, and staying updated with AI breakthroughs.
            """)

    with tab_milestones:
        st.subheader("Milestones Timeline")
        st.write("Use the slider below to step through each phase of my academic and technical journey:")
        
        # Milestone slider component (st.slider)
        selected_year = st.slider("Select Timeline Year:", min_value=2023, max_value=2026, value=2026, step=1)
        
        milestone_dict = {
            2023: {
                "title": "🌱 Foundations in Computing",
                "desc": "Began undergraduate journey in Information Technology. Mastered programming fundamentals in Python and object-oriented paradigms."
            },
            2024: {
                "title": "⚙️ Data Structures & Relational Databases",
                "desc": "Built foundational understanding of algorithmic complexity, database schema design, and advanced SQL querying."
            },
            2025: {
                "title": "📊 Data Analysis & Machine Learning Fundamentals",
                "desc": "Dove into Pandas, NumPy, and Scikit-learn. Completed unsupervised clustering models (Iris dataset) and transaction mining."
            },
            2026: {
                "title": "🚀 Applied AI & Regional Socioeconomic Modeling",
                "desc": "Enrolled in CSIT 349 (Section GO1). Formulated the Philippine FIES linear regression model (R² = 0.924) and published this interactive Streamlit autobiography!"
            }
        }
        
        m = milestone_dict[selected_year]
        st.markdown(f"### {m['title']} ({selected_year})")
        st.info(m['desc'])

    if show_all:
        st.divider()

# ==============================================================================
# 6. SECTION: SKILLS & TECHNICAL COMPETENCIES
# ==============================================================================
if show_skills:
    st.header("⚡ Skills & Technical Competencies")
    st.write("""
    Here is a comprehensive breakdown of my current skill set, quantified by proficiency level and practical experience.
    Use the interactive filters below to explore specific domains.
    """)

    # Sample skills dataset
    skills_data = [
        {"Skill": "Python Programming", "Category": "Languages", "Proficiency": 92, "Years Experience": 3.0},
        {"Skill": "Pandas & Data Wrangling", "Category": "Data Science", "Proficiency": 88, "Years Experience": 2.5},
        {"Skill": "NumPy & Numerical Computing", "Category": "Data Science", "Proficiency": 85, "Years Experience": 2.0},
        {"Skill": "Scikit-Learn (ML Models)", "Category": "Machine Learning", "Proficiency": 82, "Years Experience": 1.5},
        {"Skill": "Streamlit App Development", "Category": "Web & Deployment", "Proficiency": 90, "Years Experience": 1.5},
        {"Skill": "Matplotlib & Seaborn", "Category": "Data Science", "Proficiency": 84, "Years Experience": 2.0},
        {"Skill": "SQL & Relational Databases", "Category": "Databases", "Proficiency": 80, "Years Experience": 2.0},
        {"Skill": "Git & GitHub Version Control", "Category": "Developer Tools", "Proficiency": 86, "Years Experience": 2.5},
        {"Skill": "Data Cleaning & Preprocessing", "Category": "Data Science", "Proficiency": 89, "Years Experience": 2.0},
        {"Skill": "HTML5 / CSS3 Styling", "Category": "Web & Deployment", "Proficiency": 78, "Years Experience": 2.5},
    ]
    df_skills = pd.DataFrame(skills_data)

    # Interactive controls for skills: selectbox & slider
    col_ctrl1, col_ctrl2 = st.columns([2, 2])
    with col_ctrl1:
        categories = ["All"] + sorted(list(df_skills["Category"].unique()))
        selected_cat = st.selectbox("Filter by Category:", categories, index=0)
    with col_ctrl2:
        min_prof = st.slider("Filter Minimum Proficiency (%):", min_value=50, max_value=95, value=75, step=5)

    # Filter dataframe
    filtered_df = df_skills.copy()
    if selected_cat != "All":
        filtered_df = filtered_df[filtered_df["Category"] == selected_cat]
    filtered_df = filtered_df[filtered_df["Proficiency"] >= min_prof]

    col_sk1, col_sk2 = st.columns([3, 2])

    with col_sk1:
        st.subheader("📊 Proficiency Chart")
        if not filtered_df.empty:
            # Chart component (st.bar_chart)
            chart_data = filtered_df.set_index("Skill")[["Proficiency"]]
            st.bar_chart(chart_data, color="#0284c7")
        else:
            st.warning("No skills match the selected filter criteria. Try lowering the proficiency slider.")

    with col_sk2:
        st.subheader("📋 Skills Data Table")
        # Table / Dataframe component (st.dataframe)
        st.dataframe(
            filtered_df,
            column_config={
                "Proficiency": st.column_config.ProgressColumn(
                    "Proficiency Level",
                    help="Estimated mastery based on completed projects and course assessments",
                    format="%d%%",
                    min_value=0,
                    max_value=100,
                ),
                "Years Experience": st.column_config.NumberColumn(
                    "Experience",
                    format="%.1f yrs"
                )
            },
            use_container_width=True,
            hide_index=True
        )

    # Overall Readiness Indicator (st.progress)
    st.caption("Overall Applied AI & IT Competency Progress:")
    st.progress(0.86, text="Current Competency Benchmark: 86% (Senior Undergraduate Standing)")

    if show_all:
        st.divider()

# ==============================================================================
# 7. SECTION: FEATURED PROJECTS PORTFOLIO
# ==============================================================================
if show_projects:
    st.header("💼 Featured Projects Portfolio")
    st.write("A curated showcase of academic and practical projects developed for **CSIT 349 (Applied AI)** and beyond.")

    # Interactive Filter by Project Focus (st.selectbox)
    project_filter = st.selectbox(
        "Filter projects by domain:",
        ["All Projects", "Supervised Learning & Regression", "Unsupervised Clustering", "Data Mining & Association Rules"]
    )

    # Show code snippets toggle (st.checkbox)
    show_code = st.checkbox("Enable Code Inspection Snippets", value=False)

    # Project 1: PSA FIES Analysis
    if project_filter in ["All Projects", "Supervised Learning & Regression"]:
        with st.container():
            st.markdown("""
            <div class="project-card">
                <h3>📈 1. Philippine Family Income & Expenditure (FIES) Regional Analysis</h3>
                <span class="badge-subtle">Applied AI</span>
                <span class="badge-subtle">Linear Regression</span>
                <span class="badge-subtle">Pandas</span>
                <span class="badge-subtle">Scikit-Learn</span>
            </div>
            """, unsafe_allow_html=True)
            
            c1, c2 = st.columns([3, 2])
            with c1:
                st.write("""
                - **Role:** Lead Data Analyst & Model Developer (Group *TeamBangan*)
                - **Tools & Libraries:** Python, Pandas, Scikit-learn, Matplotlib, PSA OpenSTAT FIES Table 2.2
                - **Dataset:** 17 Philippine regions across 4 survey rounds (2015, 2018, 2021, and 2023).
                - **Key Findings & Outcomes:**
                    - Nominally, average national income rose **+31.7%** (₱268k to ₱353k) while expenditure grew **+19.4%** (₱216k to ₱258k).
                    - Fitted descriptive least-squares linear regression for 2023: $R^2 = 0.924$, slope = $0.724$, and in-sample $MAE \approx ₱12,300$.
                    - Prepared automated 7-slide presentation deck and individualized academic progress reports.
                """)
            with c2:
                st.markdown("##### 📌 Regional Model Snapshot (2023)")
                fies_sample = pd.DataFrame({
                    "Region": ["NCR", "CALABARZON", "Central Luzon", "Davao Region", "BARMM"],
                    "Avg Income (₱k)": [514.0, 396.0, 375.0, 335.0, 207.0],
                    "Avg Exp (₱k)": [386.0, 298.0, 277.0, 214.0, 169.0],
                    "Savings Rate (%)": [24.9, 24.7, 26.1, 36.1, 18.4]
                })
                st.dataframe(fies_sample, hide_index=True, use_container_width=True)

            if show_code:
                st.code("""
# PSA FIES 2023 Linear Regression Model Snippet
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

X = df_2023[['income_thousand']]
y = df_2023['expenditure_thousand']

model = LinearRegression().fit(X, y)
predictions = model.predict(X)

print(f"R-squared: {r2_score(y, predictions):.3f}")  # 0.924
print(f"MAE: ₱{mean_absolute_error(y, predictions)*1000:,.0f}")
                """, language="python")

    # Project 2: Iris K-Means Clustering
    if project_filter in ["All Projects", "Unsupervised Clustering"]:
        with st.container():
            st.markdown("""
            <div class="project-card">
                <h3>🌸 2. Iris Flower Morphological K-Means Clustering</h3>
                <span class="badge-subtle">Unsupervised ML</span>
                <span class="badge-subtle">K-Means</span>
                <span class="badge-subtle">NumPy</span>
                <span class="badge-subtle">WCSS Elbow Method</span>
            </div>
            """, unsafe_allow_html=True)
            
            c1, c2 = st.columns([3, 2])
            with c1:
                st.write("""
                - **Role:** Machine Learning Engineer & Experimenter
                - **Tools & Libraries:** Python, NumPy, Scikit-learn, Matplotlib, Jupyter Notebook
                - **Summary:**
                    - Implemented K-Means unsupervised clustering on the 4-dimensional Iris dataset (sepal length/width, petal length/width).
                    - Computed Within-Cluster Sum of Squares (WCSS) across cluster counts $K=1$ to $10$ to detect the optimal "elbow" inflection point.
                    - Projected clusters onto 2D feature spaces to evaluate separation between Setosa, Versicolor, and Virginica.
                """)
            with c2:
                st.markdown("##### 📉 WCSS Elbow Curve Simulation")
                elbow_data = pd.DataFrame({
                    "Clusters (K)": [1, 2, 3, 4, 5, 6],
                    "WCSS": [681.4, 152.3, 78.8, 57.2, 46.4, 39.0]
                }).set_index("Clusters (K)")
                st.line_chart(elbow_data)

            if show_code:
                st.code("""
# Iris K-Means Clustering Snippet
from sklearn.cluster import KMeans

wcss = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42)
    kmeans.fit(X_iris)
    wcss.append(kmeans.inertia_)
                """, language="python")

    # Project 3: Apriori Association Rule Mining
    if project_filter in ["All Projects", "Data Mining & Association Rules"]:
        with st.container():
            st.markdown("""
            <div class="project-card">
                <h3>🛒 3. Market Basket Analysis Using Apriori Algorithm</h3>
                <span class="badge-subtle">Data Mining</span>
                <span class="badge-subtle">Apriori</span>
                <span class="badge-subtle">Association Rules</span>
                <span class="badge-subtle">Retail Analytics</span>
            </div>
            """, unsafe_allow_html=True)
            
            c1, c2 = st.columns([3, 2])
            with c1:
                st.write("""
                - **Role:** Data Mining Analyst
                - **Tools & Libraries:** Python, Pandas, Association Rule Mining (Support, Confidence, Lift)
                - **Summary:**
                    - Uncovered co-occurrence patterns in retail transactions to optimize aisle layout and bundle promotions.
                    - Filtered frequent itemsets using minimum support thresholds, then generated high-confidence decision rules.
                    - Interpreted Lift metrics ($> 1.0$) to distinguish meaningful product associations from coincidental purchases.
                """)
            with c2:
                st.markdown("##### 📌 Sample Extracted Association Rules")
                apriori_sample = pd.DataFrame({
                    "Antecedent": ["Bread & Butter", "Milk", "Diapers"],
                    "Consequent": ["Jam", "Cereal", "Beer"],
                    "Support": ["12.5%", "18.2%", "8.4%"],
                    "Confidence": ["78.4%", "65.0%", "72.1%"],
                    "Lift": [2.35, 1.84, 2.10]
                })
                st.table(apriori_sample)

    # Project 4: CSIT 349 Interactive Portfolio
    if project_filter in ["All Projects"]:
        with st.container():
            st.markdown("""
            <div class="project-card">
                <h3>🌐 4. Interactive Streamlit Portfolio & Applied AI Hub</h3>
                <span class="badge-subtle">Streamlit Web App</span>
                <span class="badge-subtle">UI/UX</span>
                <span class="badge-subtle">Session State</span>
                <span class="badge-subtle">Cloud Deployment</span>
            </div>
            """, unsafe_allow_html=True)
            st.write("""
            - **Role:** Frontend & Python Application Developer
            - **Tools & Libraries:** Streamlit, Pandas, NumPy, HTML/CSS custom styling
            - **Outcome:** Designed and engineered a multi-component interactive portfolio meeting all CSIT 349 specifications:
              sidebar controls, tabs, dynamic data filters, feedback form with session state, custom visualizations, and downloadable resume.
            """)

    if show_all:
        st.divider()

# ==============================================================================
# 8. SECTION: CONTACT & FEEDBACK FORM
# ==============================================================================
if show_contact:
    st.header("📬 Contact & Interactive Feedback")
    st.write("""
    Have a question, feedback, or collaborative opportunity? 
    Fill out the interactive form below. Your submission will immediately register in the session state!
    """)

    col_form, col_history = st.columns([3, 2])

    with col_form:
        # Form component (st.form, st.form_submit_button)
        with st.form(key="feedback_form", clear_on_submit=True):
            st.markdown("#### ✍️ Send a Message / Review")
            
            name_input = st.text_input("Your Full Name *", placeholder="e.g. Dr. Jane Doe")
            email_input = st.text_input("Your Email Address *", placeholder="jane.doe@example.com")
            
            col_f1, col_f2 = st.columns(2)
            with col_f1:
                # Radio component (st.radio)
                category_input = st.radio(
                    "Feedback Category:",
                    ["Project Feedback", "Collaboration Inquiry", "Academic Question", "General Hello"]
                )
            with col_f2:
                # Slider component (st.slider)
                rating_input = st.slider("Portfolio Rating / Impression:", 1, 5, 5)
            
            # Text area component (st.text_area)
            message_input = st.text_area("Your Message / Comments *", placeholder="Type your constructive feedback or message here...")
            
            # Checkbox component (st.checkbox)
            collab_check = st.checkbox("I would like to receive a follow-up response", value=True)
            
            submitted = st.form_submit_button("🚀 Submit Feedback", use_container_width=True)
            
            if submitted:
                if not name_input.strip() or not message_input.strip():
                    st.error("Please fill in both your name and message before submitting.")
                else:
                    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                    new_entry = {
                        "name": name_input,
                        "email": email_input if email_input.strip() else "Not provided",
                        "category": category_input,
                        "rating": rating_input,
                        "message": message_input,
                        "time": timestamp
                    }
                    st.session_state.feedbacks.insert(0, new_entry)
                    st.balloons()
                    st.success(f"Thank you, **{name_input}**! Your feedback has been received and logged.")
                    st.toast("Feedback registered successfully!", icon="✅")

    with col_history:
        st.markdown("#### 💬 Recent Feedback Log")
        st.caption("Entries stored in current application session state:")
        
        if st.session_state.feedbacks:
            for idx, fb in enumerate(st.session_state.feedbacks):
                with st.expander(f"⭐ {fb['rating']}/5 from {fb['name']} ({fb['category']})", expanded=(idx == 0)):
                    st.markdown(f"**From:** {fb['name']} `({fb['email']})`")
                    st.markdown(f"**Submitted at:** {fb['time']}")
                    st.info(f"\"{fb['message']}\"")
        else:
            st.write("No feedback entries yet. Be the first to leave one!")

    if show_all:
        st.divider()

# ==============================================================================
# 9. FOOTER & ACADEMIC INTEGRITY NOTICE
# ==============================================================================
st.markdown("<br>", unsafe_allow_html=True)
col_foot1, col_foot2, col_foot3 = st.columns([2, 2, 2])

with col_foot1:
    st.markdown("##### 📌 Identification")
    st.markdown("""
    **Student:** Denzel B. Valendez  
    **Section:** GO1 (TeamBangan)  
    **Course:** CSIT 349 • Applied AI
    """)

with col_foot2:
    st.markdown("##### 🛠️ Tech Stack Used")
    st.markdown("""
    - Streamlit Framework
    - Pandas & NumPy
    - Scikit-learn
    - Python 3.12
    """)

with col_foot3:
    st.markdown("##### 🌐 Connect")
    st.markdown("""
    - [GitHub Profile](https://github.com)
    - [LinkedIn Profile](https://linkedin.com)
    - Email: `denzelvalendez73@gmail.com`
    """)

st.caption("© 2026 Denzel B. Valendez | CSIT 349 Applied AI | Built with Streamlit")
