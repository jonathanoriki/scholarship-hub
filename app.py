import streamlit as st
import pandas as pd
from datetime import date, datetime

# Page Setup
st.set_page_config(
    page_title="Global Scholarship Command & IELTS Hub",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom High-End Styling
st.markdown("""
<style>
    /* Theme Setup */
    .main { background-color: #f4f6f9; }
    
    /* Header Banner */
    .hero-banner {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%);
        padding: 3rem 2rem;
        border-radius: 16px;
        color: #ffffff;
        margin-bottom: 2rem;
        box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    }
    .hero-title { font-size: 2.8rem; font-weight: 800; letter-spacing: -0.5px; }
    .hero-sub { font-size: 1.15rem; color: #cbd5e1; margin-top: 0.5rem; }
    
    /* Metric Cards & Boxes */
    .card-box {
        background: #ffffff;
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 5px solid #2563eb;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
        margin-bottom: 1.25rem;
    }
    .guide-box {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        padding: 1.25rem;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# HERO BANNER
# ---------------------------------------------------------
st.markdown("""
<div class="hero-banner">
    <div class="hero-title">🎓 Global Scholarship & IELTS Command Center</div>
    <div class="hero-sub">Your all-in-one portal for funding databases, application milestone tracking, essay breakdowns, and IELTS mastery.</div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# EXPANDED SCHOLARSHIP DATABASE
# ---------------------------------------------------------
SCHOLARSHIPS_DATA = [
    {
        "Name": "Chevening Scholarship",
        "Host Country": "United Kingdom",
        "Funding Type": "Fully Funded",
        "Coverage": "Tuition, monthly stipend, flights, visa fees",
        "Deadline": "2026-11-03",
        "Min GPA (4.0 Scale)": 3.0,
        "Min Experience (Yrs)": 2,
        "IELTS Req": 6.5,
        "Target Fields": "Leadership, Governance, Public Health, STEM, Policy",
        "Link": "https://www.chevening.org"
    },
    {
        "Name": "Erasmus Mundus Joint Master Degrees",
        "Host Country": "Europe (Multiple)",
        "Funding Type": "Fully Funded",
        "Coverage": "Full tuition, €1,400/month stipend, travel allowance",
        "Deadline": "2027-01-15",
        "Min GPA (4.0 Scale)": 3.2,
        "Min Experience (Yrs)": 0,
        "IELTS Req": 6.5,
        "Target Fields": "Urban Planning, Health Sciences, Sustainability, Engineering",
        "Link": "https://erasmus-plus.ec.europa.eu"
    },
    {
        "Name": "DAAD Development-Related Courses (EPOS)",
        "Host Country": "Germany",
        "Funding Type": "Fully Funded",
        "Coverage": "€934/month, health insurance, travel allowance",
        "Deadline": "2026-10-31",
        "Min GPA (4.0 Scale)": 2.8,
        "Min Experience (Yrs)": 2,
        "IELTS Req": 6.0,
        "Target Fields": "Development Studies, Clinical Medicine, Public Health",
        "Link": "https://www.daad.de"
    },
    {
        "Name": "Mastercard Foundation Scholars Program",
        "Host Country": "Global / Africa Focus",
        "Funding Type": "Fully Funded",
        "Coverage": "Tuition, housing, laptop, flight, living stipend, mentoring",
        "Deadline": "2026-12-15",
        "Min GPA (4.0 Scale)": 3.0,
        "Min Experience (Yrs)": 0,
        "IELTS Req": 6.5,
        "Target Fields": "All disciplines (Emphasis on social impact & youth)",
        "Link": "https://mastercardfdn.org"
    },
    {
        "Name": "Commonwealth Master's Scholarships",
        "Host Country": "United Kingdom",
        "Funding Type": "Fully Funded",
        "Coverage": "Approved tuition fees, stipend (~£1,347/month), airfare",
        "Deadline": "2026-10-18",
        "Min GPA (4.0 Scale)": 3.3,
        "Min Experience (Yrs)": 0,
        "IELTS Req": 6.5,
        "Target Fields": "Sustainable Development, Science & Tech, Health",
        "Link": "https://cscuk.fcdo.gov.uk"
    },
    {
        "Name": "Fulbright Foreign Student Program",
        "Host Country": "United States",
        "Funding Type": "Fully Funded",
        "Coverage": "Full tuition, living stipend, health insurance, airfare",
        "Deadline": "2026-09-30",
        "Min GPA (4.0 Scale)": 3.2,
        "Min Experience (Yrs)": 1,
        "IELTS Req": 7.0,
        "Target Fields": "Public Health, Humanities, STEM, Social Sciences",
        "Link": "https://fulbrightprogram.org"
    },
    {
        "Name": "Türkiye Scholarships (Türkiye Bursları)",
        "Host Country": "Turkey",
        "Funding Type": "Fully Funded",
        "Coverage": "University placement, tuition, accommodation, stipend, flight",
        "Deadline": "2027-02-20",
        "Min GPA (4.0 Scale)": 3.0,
        "Min Experience (Yrs)": 0,
        "IELTS Req": 6.0,
        "Target Fields": "All Master's & PhD specializations",
        "Link": "https://www.turkiyeburslari.gov.tr"
    },
    {
        "Name": "Joint Japan/World Bank Graduate Scholarship",
        "Host Country": "Japan / US / Europe",
        "Funding Type": "Fully Funded",
        "Coverage": "Tuition, monthly stipend, round-trip airfare, medical insurance",
        "Deadline": "2027-03-25",
        "Min GPA (4.0 Scale)": 3.0,
        "Min Experience (Yrs)": 3,
        "IELTS Req": 6.5,
        "Target Fields": "Development, Health Policy, Infrastructure, Public Finance",
        "Link": "https://www.worldbank.org"
    }
]

# Sidebar Overview & Contact
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1523240795612-9a054b0db644?auto=format&fit=crop&w=500&q=80")
    st.markdown("### 📌 Command Navigation")
    st.info("Manage deadlines, generate essay outlines, run IELTS mock sessions, and track application milestones.")
    st.markdown("---")
    st.markdown("### 📬 Support & Inquiries")
    st.markdown("""
    * **Desk:** Application Advisory Desk
    * **Email:** support@scholarshiphub.org
    * **Coverage:** UK, EU, USA, Asia, & Global
    """)

# Main Tabs
tab_db, tab_tracker, tab_essays, tab_ielts, tab_eval = st.tabs([
    "🌐 Scholarship Database", 
    "📅 Interactive Application Calendar", 
    "✍️ Essay Masterclass & Outlines", 
    "🎙️ IELTS Preparation Suite",
    "📊 Profile Match Engine"
])

# ---------------------------------------------------------
# TAB 1: SCHOLARSHIP DATABASE
# ---------------------------------------------------------
with tab_db:
    st.subheader("🔍 Comprehensive Master's Scholarship Database")
    st.write("Filter through major funding options by country, requirements, and study field.")
    
    df_scholarships = pd.DataFrame(SCHOLARSHIPS_DATA)
    
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        countries = ["All"] + list(df_scholarships["Host Country"].unique())
        selected_country = st.selectbox("Filter by Host Country", countries)
    with col_f2:
        max_ielts = st.slider("Filter by Max IELTS Required", 6.0, 7.5, 7.5, 0.5)
        
    filtered_df = df_scholarships[df_scholarships["IELTS Req"] <= max_ielts]
    if selected_country != "All":
        filtered_df = filtered_df[filtered_df["Host Country"] == selected_country]
        
    st.dataframe(
        filtered_df[["Name", "Host Country", "Funding Type", "Coverage", "Deadline", "IELTS Req"]],
        use_container_width=True
    )
    
    st.markdown("---")
    st.subheader("📌 Quick Access Links & Key Highlights")
    for row in filtered_df.to_dict(orient="records"):
        with st.expander(f"📖 {row['Name']} ({row['Host Country']}) - Deadline: {row['Deadline']}"):
            st.write(f"**Coverage Details:** {row['Coverage']}")
            st.write(f"**Target Disciplines:** {row['Target Fields']}")
            st.write(f"**Prerequisites:** Minimum GPA: {row['Min GPA (4.0 Scale)']}, Work Experience: {row['Min Experience (Yrs)']} Yrs, IELTS: Band {row['IELTS Req']}")
            st.markdown(f"👉 **[Official Application Portal]({row['Link']})**")

# ---------------------------------------------------------
# TAB 2: INTERACTIVE APPLICATION CALENDAR & TRACKER
# ---------------------------------------------------------
with tab_tracker:
    st.subheader("📅 Your Personal Application Milestone Tracker")
    st.write("Map out your deadlines, set task status, and track your progress live.")
    
    # Session state for application milestones (FIXED)
    if "app_tasks" not in st.session_state:
        st.session_state.app_tasks = [
            {"Task": "Order Official Academic Transcripts", "Target Date": date(2026, 8, 30), "Status": "In Progress"},
            {"Task": "Request 2 Academic/Professional Recommendation Letters", "Target Date": date(2026, 9, 15), "Status": "Not Started"},
            {"Task": "Draft Chevening Leadership Essay", "Target Date": date(2026, 9, 30), "Status": "Not Started"},
            {"Task": "Take IELTS Academic Exam", "Target Date": date(2026, 10, 10), "Status": "Planned"},
            {"Task": "Finalize Erasmus Mundus Motivation Letter", "Target Date": date(2026, 11, 20), "Status": "Planned"},
        ]

    # Form to add custom application task
    st.markdown("#### ➕ Add New Milestone or Deadline")
    with st.form("add_task_form"):
        col_t1, col_t2, col_t3 = st.columns([2, 1, 1])
        with col_t1:
            new_task = st.text_input("Task Description (e.g., 'Submit DAAD Application')")
        with col_t2:
            new_date = st.date_input("Target Date", date.today())
        with col_t3:
            new_status = st.selectbox("Status", ["Not Started", "In Progress", "Completed", "Planned"])
        
        submit_task = st.form_submit_button("Add Milestone")
        if submit_task and new_task:
            st.session_state.app_tasks.append({"Task": new_task, "Target Date": new_date, "Status": new_status})
            st.success(f"Added task: '{new_task}'")

    st.markdown("---")
    st.markdown("#### 📋 Current Milestone Checklist")
    
    # Display tasks in interactive table format
    tasks_df = pd.DataFrame(st.session_state.app_tasks)
    st.dataframe(tasks_df, use_container_width=True)

# ---------------------------------------------------------
# TAB 3: ESSAY MASTERCLASS & GUIDES
# ---------------------------------------------------------
with tab_essays:
    st.subheader("✍️ Major Scholarship Essay Masterclass")
    st.write("Detailed structural blueprints and guides for drafting winning essays.")
    
    essay_choice = st.selectbox("Choose Essay Blueprint", [
        "Chevening: Leadership & Influence Essay",
        "Chevening: Networking & Relationship Building",
        "Erasmus Mundus: Motivation Statement",
        "DAAD: Letter of Motivation Structure",
        "General Statement of Purpose (SOP) Framework"
    ])
    
    if essay_choice == "Chevening: Leadership & Influence Essay":
        st.markdown("""
        <div class="card-box">
            <h3>🇬🇧 Chevening Leadership Essay Blueprint (500 words)</h3>
            <p><b>Goal:</b> Prove you are a future global leader who can influence change.</p>
            <hr>
            <h4>Recommended 4-Paragraph Structure:</h4>
            <ol>
                <li><b>Paragraph 1: Your Personal Leadership Philosophy (approx. 75 words)</b>
                    <br>Define what leadership means in your professional domain (e.g., public health, youth governance, clinical management). State your key leadership trait.</li>
                <li><b>Paragraph 2: Primary STAR Example (approx. 200 words)</b>
                    <br>Use a specific high-impact story.
                    <br>• <b>Situation:</b> Context of the project or clinical challenge.
                    <br>• <b>Task:</b> What needed to be solved or managed.
                    <br>• <b>Action:</b> What <i>you specifically</i> initiated, led, or negotiated.
                    <br>• <b>Result:</b> Tangible outcomes (e.g., "Trained 45 health workers", "Increased community reach by 40%").</li>
                <li><b>Paragraph 3: Secondary STAR Example or Advocacy Context (approx. 150 words)</b>
                    <br>Highlight institutional, community, or youth policy impact. Emphasize team mobilization and decision-making under pressure.</li>
                <li><b>Paragraph 4: Conclusion & Chevening Alignment (approx. 75 words)</b>
                    <br>Connect your leadership trajectory directly to how you will leverage the Chevening scholarship network.</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)
        
    elif essay_choice == "Chevening: Networking & Relationship Building":
        st.markdown("""
        <div class="card-box">
            <h3>🇬🇧 Chevening Networking Essay Blueprint (500 words)</h3>
            <p><b>Goal:</b> Demonstrate how you build, maintain, and leverage professional relationships to achieve impactful goals.</p>
            <hr>
            <h4>Key Elements:</h4>
            <ul>
                <li>Show how you forged professional connections across organizations, health systems, or youth platforms.</li>
                <li>Give a concrete example where your network directly helped solve a problem or scale an initiative.</li>
                <li>Explain how you plan to contribute to and benefit from the global Chevening alumni network.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    elif essay_choice == "Erasmus Mundus: Motivation Statement":
        st.markdown("""
        <div class="card-box">
            <h3>🇪🇺 Erasmus Mundus Statement of Purpose Blueprint</h3>
            <p><b>Goal:</b> Explain why this multi-university consortium aligns with your exact research and career objectives.</p>
            <hr>
            <h4>Core Sections Required:</h4>
            <ul>
                <li><b>Academic & Professional Background:</b> Ground your interest in past degree work, internships, or clinical roles.</li>
                <li><b>Consortium Alignment:</b> Explain why studying across specific universities in Europe adds unique technical value to your specialization.</li>
                <li><b>Mobility Track Motivation:</b> Address why moving between different countries during the program benefits your global perspective.</li>
                <li><b>Future Reintegration Plan:</b> Detail how you will apply the acquired Master's knowledge back in your home country or region.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    elif essay_choice == "DAAD: Letter of Motivation Structure":
        st.markdown("""
        <div class="card-box">
            <h3>🇩🇪 DAAD Letter of Motivation Blueprint</h3>
            <p><b>Goal:</b> Convince the German selection committee of your academic rigor and commitment to developmental goals.</p>
            <hr>
            <ul>
                <li>Focus heavily on the development relevance of your chosen course (e.g., public health systems, clinical research, urban policy).</li>
                <li>Highlight your minimum 2 years of professional experience after your Bachelor's degree.</li>
                <li>Provide a clear 5-year career roadmap showing your planned contributions after returning home.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    elif essay_choice == "General Statement of Purpose (SOP) Framework":
        st.markdown("""
        <div class="card-box">
            <h3>🌐 Standard Master's Statement of Purpose Framework</h3>
            <p><b>Goal:</b> A universal structure for US, European, UK, and Australian university admissions.</p>
            <hr>
            <ol>
                <li><b>Hook & Academic Focus:</b> Introduce your specific field of passion clearly without generic clichés.</li>
                <li><b>Academic Foundation:</b> Highlight key research projects, thesis work, or clinical distinctions.</li>
                <li><b>Professional & Field Experience:</b> Detail impactful projects, leadership roles, and community achievements.</li>
                <li><b>Why This Program:</b> Name specific modules, professors, labs, or university initiatives.</li>
                <li><b>Long-Term Goals:</b> Connect the degree directly to your 5-to-10-year professional trajectory.</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)

# ---------------------------------------------------------
# TAB 4: IELTS PREPARATION SUITE
# ---------------------------------------------------------
with tab_ielts:
    st.subheader("🎙️ Complete IELTS Preparation & Practice Suite")
    st.write("Comprehensive practice modules covering Writing, Speaking, Reading, and Listening strategies.")
    
    ielts_tab1, ielts_tab2, ielts_tab3 = st.tabs([
        "✍️ Task 2 Writing Engine", 
        "🗣️ Speaking Part 2 Simulator", 
        "📚 Vocabulary & Connectors Bank"
    ])
    
    with ielts_tab1:
        st.markdown("### IELTS Writing Task 2 Topic Prompts & Outlines")
        prompt_type = st.selectbox("Select Essay Type", ["Opinion (Agree/Disagree)", "Discussion (Both Views)", "Problem & Solution"])
        
        if prompt_type == "Opinion (Agree/Disagree)":
            st.info("""
            **Sample Prompt:** *Some people believe that governments should prioritize funding for medical research over arts and sports. To what extent do you agree or disagree?*
            
            **Recommended 4-Paragraph Outline:**
            - **Introduction:** Paraphrase prompt + State explicit thesis statement (e.g., *I completely agree because public health directly drives economic stability*).
            - **Body Paragraph 1:** Reason 1 - Direct societal impact of medical advances (e.g., disease mitigation, clinical innovation).
            - **Body Paragraph 2:** Reason 2 - Economic burden reduction on healthcare systems.
            - **Conclusion:** Restate thesis using varied vocabulary + Final outlook statement.
            """)
        elif prompt_type == "Discussion (Both Views)":
            st.info("""
            **Sample Prompt:** *Some think high school graduates should take a gap year to work or travel, while others think they should go straight to university. Discuss both views and give your opinion.*
            
            **Recommended Structure:**
            - **Intro:** Paraphrase prompt + Give outline statement.
            - **Body 1:** Discuss View A (Gaining real-world experience & financial independence).
            - **Body 2:** Discuss View B (Maintaining academic momentum and graduating earlier).
            - **Conclusion:** Reiterate your perspective with strong supporting logic.
            """)
        elif prompt_type == "Problem & Solution":
            st.info("""
            **Sample Prompt:** *Rapid urbanization is causing overcrowding and healthcare strain in major cities. What problems does this cause, and what solutions can be implemented?*
            
            **Recommended Structure:**
            - **Body 1:** Identify 2 main issues (Infrastructure overload & disease transmission risks).
            - **Body 2:** Propose 2 direct solutions (Urban decentralization policies & boosted primary health funding).
            """)
            
    with ielts_tab2:
        st.markdown("### Interactive Speaking Part 2 Cue Cards")
        if st.button("Generate Random IELTS Speaking Card"):
            st.success("""
            🎯 **Cue Card Prompt:**
            
            **Describe a complex problem you solved at work, university, or in a community project.**
            
            *You should say:*
            - What the problem was and where it occurred
            - What steps you took to address it
            - Who assisted you in the process
            - And explain why this experience was significant to your personal development.
            
            ⏱️ *Preparation Time: 1 minute | Speaking Target: 2 minutes*
            """)

    with ielts_tab3:
        st.markdown("### 📖 High-Scoring Academic Connectors & Lexicon")
        
        c_col1, c_col2 = st.columns(2)
        with c_col1:
            st.markdown("""
            **Transition & Cohesion Devices:**
            * *To add information:* Furthermore, In addition, Consequently
            * *To contrast:* Conversely, On the other hand, Nevertheless
            * *To illustrate:* For instance, To exemplify, A pertinent example is
            """)
        with c_col2:
            st.markdown("""
            **Band 8+ Academic Vocabulary:**
            * *Substantial:* Large, significant amount
            * *Mitigate:* Make less severe or reduce risk
            * *Imperative:* Crucial or essential requirement
            * *Spearhead:* Lead an initiative or movement
            """)

# ---------------------------------------------------------
# TAB 5: PROFILE MATCH ENGINE
# ---------------------------------------------------------
with tab_eval:
    st.subheader("📊 Profile Qualification Evaluator")
    st.write("Analyze your current profile metrics against global scholarship threshold indicators.")
    
    p_col1, p_col2, p_col3 = st.columns(3)
    with p_col1:
        eval_gpa = st.number_input("Your Bachelor's GPA (4.0 Scale)", 0.0, 4.0, 3.2, 0.1)
    with p_col2:
        eval_exp = st.number_input("Years of Full-Time/Internship Work", 0, 20, 2)
    with p_col3:
        eval_ielts = st.number_input("Your IELTS Band Score", 0.0, 9.0, 6.5, 0.5)
        
    if st.button("Run Profile Evaluation", type="primary"):
        st.markdown("### 📋 Matching Breakdown")
        
        matches = 0
        for item in SCHOLARSHIPS_DATA:
            reasons = []
            if eval_gpa < item["Min GPA (4.0 Scale)"]:
                reasons.append(f"GPA under {item['Min GPA (4.0 Scale)']}")
            if eval_exp < item["Min Experience (Yrs)"]:
                reasons.append(f"Needs {item['Min Experience (Yrs)']} yrs experience")
            if eval_ielts < item["IELTS Req"]:
                reasons.append(f"Needs Band {item['IELTS Req']}")
                
            if not reasons:
                st.success(f"✅ **{item['Name']}** ({item['Host Country']}): Strong Match!")
                matches += 1
            else:
                st.warning(f"⚠️ **{item['Name']}**: " + ", ".join(reasons))
                
        st.info(f"Summary: You meet the preliminary requirements for {matches} out of {len(SCHOLARSHIPS_DATA)} database entries.")