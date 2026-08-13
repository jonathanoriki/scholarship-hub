import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Global Master's Scholarship & Prep Hub",
    page_icon="🎓",
    layout="wide"
)

# Header
st.title("🎓 Global Master's Scholarship Intelligence & IELTS Hub")
st.caption("Your all-in-one platform for tracking funding, verifying eligibility, reviewing SOPs, and practicing IELTS.")

# Mock Database of Master's Scholarships
SCHOLARSHIPS = [
    {
        "name": "Chevening Scholarship",
        "country": "United Kingdom",
        "funding": "Full Funding",
        "deadline": "2026-11-03",
        "min_gpa": 3.0,
        "work_exp_years": 2,
        "ielts_req": 6.5,
        "link": "https://www.chevening.org"
    },
    {
        "name": "Mastercard Foundation Scholars Program",
        "country": "Global / Africa",
        "funding": "Full Funding + Living Allowance",
        "deadline": "2026-12-15",
        "min_gpa": 3.2,
        "work_exp_years": 0,
        "ielts_req": 6.5,
        "link": "https://mastercardfdn.org"
    },
    {
        "name": "DAAD Development-Related Postgraduate Courses",
        "country": "Germany",
        "funding": "Monthly Stipend + Travel",
        "deadline": "2026-10-31",
        "min_gpa": 2.8,
        "work_exp_years": 2,
        "ielts_req": 6.0,
        "link": "https://www.daad.de"
    },
    {
        "name": "Erasmus Mundus Joint Master Degrees",
        "country": "Europe (Multiple)",
        "funding": "Full Tuition + Monthly Allowance",
        "deadline": "2027-01-15",
        "min_gpa": 3.0,
        "work_exp_years": 0,
        "ielts_req": 6.5,
        "link": "https://erasmus-plus.ec.europa.eu"
    }
]

# Tabs Definition
tab1, tab2, tab3, tab4 = st.tabs([
    "🔍 Open Scholarships", 
    "📊 Eligibility Checker", 
    "📄 Document & SOP Reviewer", 
    "🎙️ IELTS Prep Engine"
])

# ---------------------------------------------------------
# TAB 1: SCHOLARSHIP MONITOR
# ---------------------------------------------------------
with tab1:
    st.header("Active Global Master's Scholarships")
    df = pd.DataFrame(SCHOLARSHIPS)
    
    # Filter
    funding_filter = st.multiselect("Filter by Funding Type", options=df["funding"].unique(), default=df["funding"].unique())
    filtered_df = df[df["funding"].isin(funding_filter)]
    
    st.dataframe(
        filtered_df[["name", "country", "funding", "deadline", "ielts_req"]],
        use_container_width=True
    )
    
    st.subheader("Quick Links")
    for item in SCHOLARSHIPS:
        st.markdown(f"- **[{item['name']}]({item['link']})** | Country: {item['country']} | Deadline: `{item['deadline']}`")

# ---------------------------------------------------------
# TAB 2: ELIGIBILITY CHECKER
# ---------------------------------------------------------
with tab2:
    st.header("Check Your Eligibility")
    st.write("Enter your profile metrics to instantly see which scholarships you qualify for.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        user_gpa = st.number_input("Your Bachelor's GPA (4.0 Scale)", min_value=0.0, max_value=4.0, value=3.2, step=0.1)
    with col2:
        user_exp = st.number_input("Years of Work Experience", min_value=0, max_value=20, value=2)
    with col3:
        user_ielts = st.number_input("Your IELTS Band Score (or estimated)", min_value=0.0, max_value=9.0, value=6.5, step=0.5)
        
    if st.button("Evaluate Matches"):
        st.subheader("Your Eligibility Results")
        matches = 0
        for item in SCHOLARSHIPS:
            reasons = []
            if user_gpa < item["min_gpa"]:
                reasons.append(f"GPA lower than required minimum ({item['min_gpa']})")
            if user_exp < item["work_exp_years"]:
                reasons.append(f"Requires at least {item['work_exp_years']} years experience")
            if user_ielts < item["ielts_req"]:
                reasons.append(f"Requires minimum IELTS Band {item['ielts_req']}")
                
            if not reasons:
                st.success(f"✅ **Eligible:** {item['name']} ({item['country']})")
                matches += 1
            else:
                st.error(f"❌ **Not Eligible for {item['name']}:** " + ", ".join(reasons))
        st.info(f"Summary: You qualify for {matches} out of {len(SCHOLARSHIPS)} monitored scholarships.")

# ---------------------------------------------------------
# TAB 3: SOP & DOCUMENT REVIEWER
# ---------------------------------------------------------
with tab3:
    st.header("Statement of Purpose (SOP) Analyzer")
    st.write("Paste your Statement of Purpose or Motivation Letter below for instant structural evaluation.")
    
    sop_text = st.text_area("Paste your SOP draft here (minimum 100 words):", height=250)
    
    if st.button("Analyze Statement"):
        words = len(sop_text.split())
        st.subheader("Analysis Feedback")
        
        # Simple rule-based rubric evaluation
        if words < 100:
            st.warning("⚠️ Statement is too short. Most Master's SOPs require 500–800 words.")
        else:
            st.success(f"✅ Word Count: **{words} words** (Good length)")
            
            # Key section checks
            has_leadership = any(w in sop_text.lower() for w in ["lead", "leadership", "project", "initiative", "managed"])
            has_future = any(w in sop_text.lower() for w in ["goal", "future", "career", "vision", "impact", "return"])
            has_academic = any(w in sop_text.lower() for w in ["bachelor", "degree", "research", "study", "thesis"])
            
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                st.metric("Academic Background Focus", "Detected" if has_academic else "Missing")
            with col_b:
                st.metric("Leadership & Action Proof", "Detected" if has_leadership else "Needs Enhancement")
            with col_c:
                st.metric("Career Vision & Impact", "Detected" if has_future else "Needs Enhancement")

# ---------------------------------------------------------
# TAB 4: IELTS PREP ENGINE
# ---------------------------------------------------------
with tab4:
    st.header("IELTS Prep Center")
    prep_mode = st.radio("Choose Practice Module:", ["Writing Task 2 Essay Criteria", "Speaking Prompt Generator"])
    
    if prep_mode == "Writing Task 2 Essay Criteria":
        st.subheader("Writing Task 2 Rubric Checklist")
        st.markdown("""
        Ensure your essay covers these core scoring pillars before submitting:
        - [ ] **Task Achievement:** Fully answers all parts of the prompt with clear position throughout.
        - [ ] **Coherence & Cohesion:** Clear paragraphing with transition words (e.g., *Furthermore, Consequently*).
        - [ ] **Lexical Resource:** Uses varied, high-level vocabulary without repetition.
        - [ ] **Grammatical Range & Accuracy:** Mix of simple, compound, and complex sentences.
        """)
    else:
        st.subheader("Randomized IELTS Speaking Part 2 Card")
        if st.button("Generate Topic Card"):
            st.info("""
            **Topic:** Describe a community initiative or project you participated in that had a positive outcome.
            
            **You should say:**
            - What the initiative was
            - Who was involved
            - What your specific role was
            - And explain why you feel this project was successful.
            
            *Preparation time: 1 minute | Speaking time: 1–2 minutes*
            """)