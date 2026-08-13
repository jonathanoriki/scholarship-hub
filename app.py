import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Global Master's & Public Health Leadership Portal",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Modern UI, Custom Colors, and Card Styling
st.markdown("""
<style>
    /* Main Theme Overrides */
    .stApp {
        background-color: #f8f9fa;
    }
    
    /* Hero Banner Styling */
    .hero-container {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        padding: 2.5rem 2rem;
        border-radius: 12px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .hero-title {
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }
    
    .hero-subtitle {
        font-size: 1.1rem;
        opacity: 0.9;
    }

    /* Metric & Card Components */
    .feature-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #2a5298;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        margin-bottom: 1rem;
    }
    
    /* Footer Styling */
    .footer {
        text-align: center;
        padding: 2rem 0 1rem 0;
        color: #6c757d;
        font-size: 0.9rem;
        border-top: 1px solid #e9ecef;
        margin-top: 3rem;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# HERO SECTION
# ---------------------------------------------------------
st.markdown("""
<div class="hero-container">
    <div class="hero-title">🎓 Global Master's & Youth Leadership Hub</div>
    <div class="hero-subtitle">Empowering young professionals with scholarship intelligence, SOP review tools, IELTS preparation resources, and advocacy insights.</div>
</div>
""", unsafe_allow_html=True)

# Sidebar - Quick Profile & Contact Details
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1523240795612-9a054b0db644?auto=format&fit=crop&w=500&q=80", caption="Global Opportunity Engine")
    
    st.markdown("### 📌 Navigation & Info")
    st.info("Welcome! This platform provides curated data and tools for Master's applications in Clinical Sciences, Public Health, Urban Governance, and Public Policy.")
    
    st.markdown("---")
    st.markdown("### 📬 Contact & Support")
    st.markdown("""
    * **Email:** support@globalopportunityhub.org
    * **Location:** Nairobi / Eldoret, Kenya
    * **Advocacy Desk:** Youth Leadership & Advisory Initiatives
    """)
    st.markdown("---")
    st.caption("© 2026 Global Leadership Portal. All rights reserved.")

# ---------------------------------------------------------
# MAIN TAB NAVIGATION
# ---------------------------------------------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🔍 Open Scholarships", 
    "📊 Profile Eligibility Evaluator", 
    "📄 SOP & Essay Analyzer", 
    "🎙️ IELTS Prep Suite",
    "📚 Resource Library & Downloads"
])

# ---------------------------------------------------------
# TAB 1: ENHANCED SCHOLARSHIP MONITOR
# ---------------------------------------------------------
with tab1:
    st.subheader("🌐 Curated Global Master's Opportunities")
    st.write("Browse fully funded and prestigious partially funded opportunities aligned with health, leadership, and international development.")
    
    # Visual cards for featured opportunities
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown("""
        <div class="feature-card">
            <h4>🇬🇧 Chevening Master's Scholarship</h4>
            <p><b>Coverage:</b> Full Tuition + Monthly Living Allowance + Airfare</p>
            <p><b>Target Fields:</b> Global Health, Leadership, Public Policy, Governance</p>
            <p><b>Key Requirement:</b> 2+ years professional work experience</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("Apply on Chevening Official Portal", "https://www.chevening.org")
        
        st.markdown("""
        <div class="feature-card">
            <h4>🇩🇪 DAAD EPOS Postgraduate Scholarship</h4>
            <p><b>Coverage:</b> Monthly Stipend (€934) + Health Insurance + Travel Grant</p>
            <p><b>Target Fields:</b> Development Studies, Clinical Medicine, Health Economics</p>
            <p><b>Key Requirement:</b> Bachelor's degree + 2 years relevant experience</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("Explore DAAD EPOS Courses", "https://www.daad.de")

    with col_b:
        st.markdown("""
        <div class="feature-card">
            <h4>🌍 Mastercard Foundation Scholars Program</h4>
            <p><b>Coverage:</b> Full Tuition + Accommodation + Laptop + Mentorship</p>
            <p><b>Target Fields:</b> All Disciplines (Emphasis on African Youth & Social Impact)</p>
            <p><b>Key Requirement:</b> Demonstrated leadership and community service record</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("Mastercard Foundation Portal", "https://mastercardfdn.org")

        st.markdown("""
        <div class="feature-card">
            <h4>🇪🇺 Erasmus Mundus Joint Master Degrees (EMJMD)</h4>
            <p><b>Coverage:</b> Full Fee Coverage + €1,400/month stipend</p>
            <p><b>Target Fields:</b> Public Health, Urban Planning, Sustainability</p>
            <p><b>Key Requirement:</b> High Academic Standing + Strong Motivation Statement</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("Browse Erasmus Master Catalog", "https://erasmus-plus.ec.europa.eu")

# ---------------------------------------------------------
# TAB 2: ELIGIBILITY EVALUATOR
# ---------------------------------------------------------
with tab2:
    st.subheader("📊 Interactive Profile Eligibility Checker")
    st.write("Input your academic and professional qualifications to check instant alignment with major funding schemes.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        user_gpa = st.slider("Bachelor's GPA / Degree Class", 2.0, 4.0, 3.4, 0.1)
    with col2:
        user_exp = st.number_input("Years of Professional/Internship Experience", 0, 15, 2)
    with col3:
        user_ielts = st.selectbox("Target or Achieved IELTS Band", [6.0, 6.5, 7.0, 7.5, 8.0, 8.5])
        
    st.markdown("---")
    
    if st.button("Evaluate Qualification Alignment", type="primary"):
        st.write("### Evaluation Breakdown:")
        
        # Chevening Check
        if user_exp >= 2 and user_ielts >= 6.5:
            st.success("✅ **Chevening Scholarship:** High Eligibility. You meet experience and language prerequisites.")
        else:
            st.warning("⚠️ **Chevening Scholarship:** Requires at least 2 years of work experience and an IELTS of 6.5+.")
            
        # DAAD Check
        if user_exp >= 2 and user_gpa >= 2.8:
            st.success("✅ **DAAD EPOS:** Strong Match. Meets academic threshold and work experience baseline.")
        else:
            st.error("❌ **DAAD EPOS:** Recommended 2 years minimum post-graduation experience.")
            
        # Mastercard Foundation
        if user_gpa >= 3.0:
            st.success("✅ **Mastercard Foundation:** Excellent Fit. Focus heavy emphasis in your SOP on youth advocacy & community impact.")

# ---------------------------------------------------------
# TAB 3: DOCUMENT & SOP ANALYZER
# ---------------------------------------------------------
with tab3:
    st.subheader("📄 Statement of Purpose (SOP) & Essay Audit")
    st.write("Paste your motivation statement or personal response below for automated structural feedback.")
    
    sop_text = st.text_area("Paste draft here:", height=200, placeholder="Start typing or paste your Statement of Purpose draft...")
    
    if st.button("Run SOP Structural Audit", type="primary"):
        words = len(sop_text.split())
        
        st.markdown("#### Audit Results:")
        m1, m2, m3 = st.columns(3)
        m1.metric("Word Count", f"{words} Words", "Ideal: 500-800" if 500 <= words <= 800 else "Adjust Length")
        
        # Pillar Analysis
        leadership_words = ["lead", "managed", "initiative", "project", "advocacy", "spearheaded", "community", "clinical"]
        future_words = ["goal", "vision", "impact", "return", "policy", "development", "master"]
        
        has_lead = sum(sop_text.lower().count(w) for w in leadership_words)
        has_future = sum(sop_text.lower().count(w) for w in future_words)
        
        m2.metric("Leadership & Action Focus", f"{has_lead} Mention(s)", "Strong" if has_lead >= 3 else "Add Action Verbs")
        m3.metric("Career Vision & Impact", f"{has_future} Mention(s)", "Clear" if has_future >= 2 else "Expand Future Goals")

# ---------------------------------------------------------
# TAB 4: IELTS PREPARATION SUITE
# ---------------------------------------------------------
with tab4:
    st.subheader("🎙️ IELTS Preparation Suite")
    
    col_i1, col_i2 = st.columns([1, 1])
    
    with col_i1:
        st.markdown("### ✍️ Writing Task 2 Checklist")
        st.checkbox("Task Response: Answered all parts of the essay prompt clearly.")
        st.checkbox("Coherence: Clear paragraph structure with transitions (However, Furthermore, Consequently).")
        st.checkbox("Lexical Resource: Used high-level academic vocabulary (e.g., *implement, systemic, substantial*).")
        st.checkbox("Grammar: Mixed complex and compound sentence structures correctly.")

    with col_i2:
        st.markdown("### 🗣️ Speaking Part 2 Prompt Engine")
        if st.button("Generate Random Speaking Prompt"):
            st.info("""
            **Topic:** Describe a community initiative or healthcare project you led or participated in.
            
            **Include in your talk:**
            - What the initiative was and who benefited
            - Your specific responsibilities
            - The challenges faced and how they were resolved
            - Why this experience shaped your professional goals
            """)

# ---------------------------------------------------------
# TAB 5: RESOURCE LIBRARY & DOWNLOADS
# ---------------------------------------------------------
with tab5:
    st.subheader("📚 Free Downloads & Templates")
    st.write("Download reference materials and guides directly to assist your application journey.")
    
    r1, r2, r3 = st.columns(3)
    
    with r1:
        st.markdown("#### 📝 Standard SOP Template")
        st.write("A structured outline following standard international university formats.")
        st.download_button("Download SOP Template (.txt)", data="1. Introduction & Background\n2. Academic Achievements\n3. Leadership Experience\n4. Why this University\n5. Future Goals", file_name="SOP_Template.txt")

    with r2:
        st.markdown("#### 🌟 Action Verbs Guide")
        st.write("A curated list of impactful verbs for resumes and recommendation letters.")
        st.download_button("Download Verbs Guide (.txt)", data="Spearheaded, Coordinated, Implemented, Orchestrated, Evaluated, Pioneered", file_name="Action_Verbs.txt")

    with r3:
        st.markdown("#### 📑 IELTS Writing Rubric")
        st.write("Official scoring breakdown for Band 7+ Task 2 response criteria.")
        st.download_button("Download Rubric Summary (.txt)", data="Band 7 Requirements: Flexible use of cohesive devices, clear main ideas, varied vocabulary.", file_name="IELTS_Band7_Guide.txt")

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.markdown("""
<div class="footer">
    Global Master's Scholarship & Youth Leadership Hub • Built with Python & Streamlit
</div>
""", unsafe_allow_html=True)