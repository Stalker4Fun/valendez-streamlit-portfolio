# CSIT 349 • Applied AI
## Activity: Autobiography and Portfolio App

**Student:** Denzel B. Valendez  
**Course:** CSIT 349 — Applied AI  
**Section:** GO1 (TeamBangan)  
**Program:** BS Information Technology (3rd Year)  

---

## 🌟 Application Overview

This project is a personal autobiography and portfolio web application built with [Streamlit](https://streamlit.io/). It showcases academic background, technical skills, machine learning projects, and an interactive feedback system.

### Key Sections:
1. **Header & Hero:** High-level metrics, academic standing, and introduction.
2. **About Me & Autobiography:** 
   - 📖 Personal Background
   - 🎓 Education Journey
   - 💡 Passions & Interests
   - 🏆 Interactive Milestones Timeline (with year slider)
3. **Skills & Competencies:**
   - Interactive filtering by category and minimum proficiency slider
   - Visualized using both dynamic **Bar Charts** and rich **DataTables** with progress bars
   - Overall competency readiness indicator
4. **Featured Projects Showcase:**
   - **Philippine Family Income & Expenditure (FIES 2015–2023) Analysis:** In-sample linear regression model ($R^2 = 0.924$, $MAE \approx ₱12,300$) analyzing 17 regions.
   - **Iris Flower K-Means Clustering:** Unsupervised clustering with WCSS elbow curve analysis.
   - **Market Basket Analysis (Apriori Algorithm):** Transaction mining with Support, Confidence, and Lift metrics.
   - **Interactive Streamlit Hub:** Live web application with custom styling and session state.
5. **Interactive Contact & Feedback Form:**
   - Name, email, feedback category, rating slider, and message
   - Live session state logging with balloons, toast alerts, and history view.

---

## 🧩 Streamlit Components Checklist

Every required and extra component has been fully utilized:
- **Text & Structure:** `st.title`, `st.header`, `st.subheader`, `st.write`, `st.markdown`, `st.caption`, `st.divider`
- **Data Display:** `st.dataframe` (with progress column), `st.table`
- **Visualizations:** `st.bar_chart`, `st.line_chart`
- **Interactive Controls:**
  - `st.button` (kudos counter, celebration trigger)
  - `st.slider` (milestone year selector, proficiency filter, rating)
  - `st.selectbox` (category filters, project domain filter)
  - `st.checkbox` (detailed bio toggle, code inspection toggle, follow-up check)
  - `st.text_input` & `st.text_area`
  - `st.radio` (sidebar navigation, feedback category)
- **Layout & Organization:**
  - `st.sidebar` (profile card, navigation, kudos, CV download)
  - `st.columns` (responsive multi-column layouts)
- **Extra Features:**
  - `st.image` (profile photo / stand-in)
  - `st.tabs` (autobiography tabs)
  - `st.metric` (key performance indicator cards)
  - `st.form` & `st.form_submit_button` (feedback submission)
  - `st.session_state` (real-time feedback log and cheer counter)
  - `st.download_button` (downloading CV summary text)
  - `st.expander` (collapsible feedback logs)
  - `st.code` (Python code snippets)
  - `st.progress` (competency readiness progress bar)
  - `st.balloons` & `st.toast` (feedback and celebration effects)

---

## 🚀 How to Run Locally

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *(or `pip install streamlit pandas numpy`)*

2. **Run the Streamlit application:**
   ```bash
   streamlit run app.py
   ```

3. Open your browser at `http://localhost:8501`.

---

## ☁️ How to Deploy to Streamlit Community Cloud (Bonus Points)

1. Create a public repository on GitHub (e.g. `valendez-streamlit-portfolio`).
2. Push `app.py`, `requirements.txt`, `assets/`, and `.streamlit/` to the repository.
3. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
4. Click **New app**, select your repository, branch (`main`), and set the main file path to `app.py`.
5. Click **Deploy!** Streamlit Cloud will build and host your app with a public URL to submit.

---

## 📦 Option A Submission Files
- `app.py`
- `requirements.txt`
- `assets/profile.png`
- `Valendez_Denzel_Portfolio.zip` (ready to submit)

