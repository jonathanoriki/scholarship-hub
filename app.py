import streamlit as st
import pandas as pd
if "saved_scholarships" not in st.session_state:
    st.session_state.saved_scholarships = []
if "saved_scholarships" not in st.session_state:
    st.session_state.saved_scholarships = []

if "applications" not in st.session_state:
    st.session_state.applications = []
from datetime import date, datetime, timedelta
# LOAD CSV DATABASES

try:
    scholarships_csv = pd.read_csv("data/scholarships.csv")
except:
    scholarships_csv = pd.DataFrame()

try:
    universities_csv = pd.read_csv("data/universities.csv")
except:
    universities_csv = pd.DataFrame()

try:
    countries_csv = pd.read_csv("data/countries.csv")
except:
    countries_csv = pd.DataFrame()
# ---------------------------------------------------------
# PAGE CONFIGURATION & METADATA
# ---------------------------------------------------------
st.set_page_config(
    page_title="Global Scholarship Intelligence Platform",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# CUSTOM HIGH-END UI STYLING & CSS
# ---------------------------------------------------------
st.markdown("""
<style>
    /* Main Background & Fonts */
    .stApp {
        background-color: #0f172a;
        color: #f8fafc;
    }
    
    /* Hero Banner Styling */
    .hero-container {
        background: linear-gradient(135deg, #1e1b4b 0%, #312e81 50%, #1e3a8a 100%);
        padding: 3rem 2rem;
        border-radius: 16px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        border: 1px solid #3730a3;
    }
    
    .hero-title {
        font-size: 3rem;
        font-weight: 900;
        letter-spacing: -1px;
        background: linear-gradient(90deg, #60a5fa, #a78bfa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .hero-sub {
        font-size: 1.25rem;
        color: #cbd5e1;
        margin-top: 0.5rem;
    }

    /* Metric Cards & Badges */
    .metric-card {
        background: #1e293b;
        border: 1px solid #334155;
        padding: 1.25rem;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }
    
    .card-box {
        background: #1e293b;
        border: 1px solid #334155;
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 1.25rem;
        border-left: 5px solid #3b82f6;
    }

    /* Urgency Badges */
    .badge-urgent {
        background-color: #ef4444;
        color: white;
        padding: 0.25rem 0.6rem;
        border-radius: 6px;
        font-weight: bold;
        font-size: 0.85rem;
    }
    .badge-approaching {
        background-color: #f59e0b;
        color: white;
        padding: 0.25rem 0.6rem;
        border-radius: 6px;
        font-weight: bold;
        font-size: 0.85rem;
    }
    .badge-open {
        background-color: #10b981;
        color: white;
        padding: 0.25rem 0.6rem;
        border-radius: 6px;
        font-weight: bold;
        font-size: 0.85rem;
    }

    /* Tab Custom Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #1e293b;
        border-radius: 8px;
        color: #94a3b8;
        padding: 8px 16px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #2563eb !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# MASTER SCHOLARSHIPS DATABASE (EXTENDED ARCHITECTURE)
# ---------------------------------------------------------
MASTER_SCHOLARSHIPS = [
    {
        "Name": "Chevening Scholarship",
        "Level": "Master's",
        "Host Country": "UK",
        "Funding Type": "Fully Funded",
        "Field": "Public Health, Governance, STEM, Leadership, Clinical Medicine",
        "Min GPA": 3.0,
        "Min Exp (Yrs)": 2,
        "IELTS": 6.5,
        "Deadline": "2026-11-03",
        "Accepts African Students": True,
        "Link": "https://www.chevening.org"
    },
    {
        "Name": "Erasmus Mundus Joint Master Degrees (EMJMD)",
        "Level": "Master's",
        "Host Country": "Europe (Multiple)",
        "Funding Type": "Fully Funded",
        "Field": "Urban Planning, Biomedical Sciences, Data Science, Public Health",
        "Min GPA": 3.2,
        "Min Exp (Yrs)": 0,
        "IELTS": 6.5,
        "Deadline": "2027-01-15",
        "Accepts African Students": True,
        "Link": "https://erasmus-plus.ec.europa.eu"
    },
    {
        "Name": "DAAD Development-Related Courses (EPOS)",
        "Level": "Master's",
        "Host Country": "Germany",
        "Funding Type": "Fully Funded",
        "Field": "Development Studies, Clinical Medicine, Public Health, Agriculture",
        "Min GPA": 2.8,
        "Min Exp (Yrs)": 2,
        "IELTS": 6.0,
        "Deadline": "2026-10-31",
        "Accepts African Students": True,
        "Link": "https://www.daad.de"
    },
    {
        "Name": "Mastercard Foundation Scholars Program",
        "Level": "Master's",
        "Host Country": "Canada",
        "Funding Type": "Fully Funded",
        "Field": "Public Health, Engineering, AI, Agriculture, Nursing",
        "Min GPA": 3.0,
        "Min Exp (Yrs)": 0,
        "IELTS": 6.5,
        "Deadline": "2026-12-15",
        "Accepts African Students": True,
        "Link": "https://mastercardfdn.org"
    },
    {
        "Name": "Commonwealth Master's & PhD Scholarships",
        "Level": "Master's",
        "Host Country": "UK",
        "Funding Type": "Fully Funded",
        "Field": "Climate Change, Economics, Health, Engineering, Law",
        "Min GPA": 3.3,
        "Min Exp (Yrs)": 0,
        "IELTS": 6.5,
        "Deadline": "2026-10-18",
        "Accepts African Students": True,
        "Link": "https://cscuk.fcdo.gov.uk"
    },
    {
        "Name": "Fulbright Foreign Student Program",
        "Level": "Master's",
        "Host Country": "USA",
        "Funding Type": "Fully Funded",
        "Field": "All Fields",
        "Min GPA": 3.2,
        "Min Exp (Yrs)": 1,
        "IELTS": 7.0,
        "Deadline": "2026-09-30",
        "Accepts African Students": True,
        "Link": "https://fulbrightprogram.org"
    },
    {
        "Name": "Türkiye Scholarships (Türkiye Bursları)",
        "Level": "Bachelor's",
        "Host Country": "Turkey",
        "Funding Type": "Fully Funded",
        "Field": "Medicine, Engineering, Law, Data Science",
        "Min GPA": 3.0,
        "Min Exp (Yrs)": 0,
        "IELTS": 6.0,
        "Deadline": "2027-02-20",
        "Accepts African Students": True,
        "Link": "https://www.turkiyeburslari.gov.tr"
    },
    {
        "Name": "Joint Japan/World Bank Graduate Scholarship",
        "Level": "Master's",
        "Host Country": "Japan",
        "Funding Type": "Fully Funded",
        "Field": "Economics, Health Policy, Infrastructure, Agriculture",
        "Min GPA": 3.0,
        "Min Exp (Yrs)": 3,
        "IELTS": 6.5,
        "Deadline": "2027-03-25",
        "Accepts African Students": True,
        "Link": "https://www.worldbank.org"
    },
    {
        "Name": "MEXT Japanese Government Scholarship",
        "Level": "PhD",
        "Host Country": "Japan",
        "Funding Type": "Fully Funded",
        "Field": "Biomedical Sciences, AI, Robotics, Medicine",
        "Min GPA": 3.2,
        "Min Exp (Yrs)": 0,
        "IELTS": 6.5,
        "Deadline": "2026-09-10",
        "Accepts African Students": True,
        "Link": "https://www.mext.go.jp"
    },
    {
        "Name": "Mandela Rhodes Scholarship",
        "Level": "Postdoctoral",
        "Host Country": "South Africa",
        "Funding Type": "Fully Funded",
        "Field": "Leadership, Health, Public Policy, Humanities",
        "Min GPA": 3.4,
        "Min Exp (Yrs)": 0,
        "IELTS": 6.5,
        "Deadline": "2026-08-21",
        "Accepts African Students": True,
        "Link": "https://mandelarhodes.org"
    }
]

# ---------------------------------------------------------
# HERO LANDING SECTION
# ---------------------------------------------------------
st.markdown("""
<div class="hero-container">
    <div class="hero-title">🎓 Global Scholarship Intelligence Platform</div>
    <div class="hero-sub">The Bloomberg Terminal of International Scholarships & Youth Leadership Grants</div>
    <p style="margin-top: 1rem; color: #94a3b8;">Find Your Next Fully Funded Opportunity in Under 60 Seconds.</p>
</div>
""", unsafe_allow_html=True)

# High Impact Counter Bar
m1, m2, m3, m4 = st.columns(4)
m1.markdown("<div class='metric-card'><h3>1,000+</h3><p>Active Scholarships</p></div>", unsafe_allow_html=True)
m2.markdown("<div class='metric-card'><h3>100+</h3><p>Countries Covered</p></div>", unsafe_allow_html=True)
m3.markdown("<div class='metric-card'><h3>500+</h3><p>Top Universities</p></div>", unsafe_allow_html=True)
m4.markdown("<div class='metric-card'><h3>$500M+</h3><p>Funding Opportunities</p></div>", unsafe_allow_html=True)
# Scholarship Statistics Dashboard

st.markdown("## 📊 Scholarship Statistics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🎓 Scholarships", len(scholarships_csv))

with col2:
    st.metric(
        "💰 Fully Funded",
        len(
            scholarships_csv[
                scholarships_csv["Funding Type"].str.contains(
                    "Fully",
                    case=False,
                    na=False
                )
            ]
        )
    )

with col3:
    st.metric(
        "🌍 Countries",
        scholarships_csv["Host Country"].nunique()
    )

with col4:
    st.metric(
        "📅 Deadlines",
        scholarships_csv["Deadline"].count()
    )
st.markdown("<br>", unsafe_allow_html=True)

# ---------------------------------------------------------
# NAVIGATION TABS
# ---------------------------------------------------------
tabs = st.tabs([
    "🔍 Search Engine", 
    "🤖 Match Engine", 
    "⏰ Deadline Center", 
    "🌍 Country Hub", 
    "🏛️ University Finder", 
    "✍️ Essay Library", 
    "📄 CV Masterclass", 
    "✉️ Referees Toolkit", 
    "🎙️ IELTS Command", 
    "📊 Readiness Score", 
    "🌍 Africa Opportunities", 
    "🌟 Fellowships", 
    "🔬 Research Grants", 
    "🏆 Success Stories", 
    "💬 AI Coach",
    "⭐ Saved Scholarships",
    "📋 Application Tracker",
    "💬 Community Forum"
])

# ---------------------------------------------------------
# TAB 1: MASSIVE SEARCH ENGINE
# ---------------------------------------------------------
with tabs[0]:
    st.subheader("🔍 Fully Searchable Scholarship Intelligence Database")
    
    col_s1, col_s2, col_s3, col_s4 = st.columns(4)
    with col_s1:
        s_level = st.selectbox("Degree Level", ["All", "Bachelor's", "Master's", "PhD", "Postdoctoral", "Fellowship"])
    with col_s2:
        s_country = st.selectbox("Destination Country", ["All", "UK", "USA", "Canada", "Germany", "Europe (Multiple)", "Japan", "Turkey", "South Africa"])
    with col_s3:
        s_funding = st.selectbox("Funding Type", ["All", "Fully Funded", "Tuition Only", "Partial Funding"])
    with col_s4:
        s_field = st.selectbox("Academic Field", ["All", "Public Health", "Clinical Medicine", "Engineering", "AI", "Economics", "Climate Change"])
        
    # Data Filter Logic
    df = scholarships_csv.copy()
    
    if s_level != "All":
        df = df[df["Level"] == s_level]
    if s_country != "All":
        df = df[df["Host Country"] == s_country]
    if s_funding != "All":
        df = df[df["Funding Type"] == s_funding]
    if s_field != "All":
        df = df[df["Field"].str.contains(s_field, case=False, na=False)]
        
    st.data_editor(
    df[["Name", "Level", "Host Country", "Funding Type", "Min GPA", "IELTS", "Deadline", "Link"]],
    column_config={
        "Link": st.column_config.LinkColumn(
            "Apply",
            help="Open scholarship website",
            display_text="🔗 Apply Now"
        )
    },
    hide_index=True,
    use_container_width=True
)
    
    st.markdown("### Featured Quick Match")
    for item in df.to_dict(orient="records"):
        with st.expander(f"📌 {item['Name']} - {item['Host Country']} ({item['Level']})"):
            st.write(f"**Field Coverage:** {item['Field']}")
            st.write(f"**Prerequisites:** Min GPA {item['Min GPA']} | IELTS Band {item['IELTS']} | Min Work Experience: {item['Min Exp (Yrs)']} Yrs")
            st.markdown(f"👉 [Apply on Official Website]({item['Link']})")
if st.button(
    f"⭐ Save {item['Name']}",
    key=f"save_{item['Name']}"
):

    st.session_state.saved_scholarships.append(
        {
            "Scholarship": item["Name"],
            "Country": item["Host Country"],
            "Link": item["Link"]
        }
    )

    st.success("Scholarship saved successfully.")
# ---------------------------------------------------------
# TAB 2: SCHOLARSHIP RECOMMENDATION ENGINE
# ---------------------------------------------------------
with tabs[1]:
    st.subheader("🤖 Multidimensional Scholarship Match Engine")
    st.write("Fill out your full academic and professional profile for precision matching.")
    
    with st.form("match_form"):
        c1, c2, c3 = st.columns(3)
        with c1:
            u_nationality = st.text_input("Your Nationality", "Kenyan")
            u_gpa = st.number_input("Bachelor's GPA (4.0 Scale)", 0.0, 4.0, 3.4, 0.1)
            u_exp = st.number_input("Years of Professional Experience", 0, 15, 2)
        with c2:
            u_degree = st.selectbox("Target Degree Level", ["Master's", "PhD", "Bachelor's"])
            u_pubs = st.number_input("Research Publications", 0, 10, 1)
            u_ielts = st.number_input("Achieved/Target IELTS Band", 0.0, 9.0, 7.0, 0.5)
        with c3:
            u_lead = st.selectbox("Leadership Experience Level", ["High (Organized Initiatives/CBOs)", "Moderate (Team Lead)", "Basic"])
            u_need = st.selectbox("Financial Need Level", ["High Need", "Moderate", "None"])
            u_course = st.text_input("Target Field", "Public Health")
            
        submit_match = st.form_submit_button("Calculate Matching Scores", type="primary")

    if submit_match:

        st.markdown("### 🎯 Your Personalized Scholarship Matches")

        results = []

        for _, sch in scholarships_csv.iterrows():

            score = 0

            # GPA Score
            if u_gpa >= sch["Min GPA"]:
                score += 30

            # Experience Score
            if u_exp >= sch["Min Exp (Yrs)"]:
                score += 20

            # IELTS Score
            if u_ielts >= sch["IELTS"]:
                score += 20

            # Degree Match
            if u_degree == sch["Level"]:
                score += 15

            # Field Match
            if u_course.lower() in str(sch["Field"]).lower():
                score += 15

            results.append({
                "Scholarship": sch["Name"],
                "Country": sch["Host Country"],
                "Match Score": score,
                "Link": sch["Link"]
            })

        results_df = pd.DataFrame(results)

        results_df = results_df.sort_values(
            "Match Score",
            ascending=False
        )

        st.data_editor(
            results_df.head(10),
            column_config={
                "Link": st.column_config.LinkColumn(
                    "Apply",
                    display_text="🔗 Apply Now"
                )
            },
            hide_index=True,
            use_container_width=True
        )

        st.markdown("### 🏆 Top Recommended Scholarships")

        for _, row in results_df.head(5).iterrows():

            with st.expander(
                f"{row['Scholarship']} ({row['Match Score']}%)"
            ):

                st.metric(
                    "Match Score",
                    f"{row['Match Score']}%"
                )

                st.write(
                    f"Host Country: {row['Country']}"
                )

                st.markdown(
                    f"[Apply Here]({row['Link']})"
                )
# ---------------------------------------------------------
# TAB 3: SCHOLARSHIP DEADLINE INTELLIGENCE CENTER
# ---------------------------------------------------------
with tabs[2]:
    st.subheader("⏰ Real-Time Scholarship Deadline Intelligence")
    st.write("Track upcoming deadlines with live status indicators.")
    
    today = date.today()
    for _, sch in scholarships_csv.iterrows():
        deadline_date = datetime.strptime(sch["Deadline"], "%Y-%m-%d").date()
        days_left = (deadline_date - today).days
        
        if days_left <= 30:
            badge = f"<span class='badge-urgent'>🔴 Urgent ({days_left} Days Remaining)</span>"
        elif days_left <= 90:
            badge = f"<span class='badge-approaching'>🟡 Approaching ({days_left} Days Remaining)</span>"
        else:
            badge = f"<span class='badge-open'>🟢 Open ({days_left} Days Remaining)</span>"
            
        st.markdown(f"""
        <div class="card-box">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <h4>{sch['Name']} ({sch['Host Country']})</h4>
                {badge}
            </div>
            <p><b>Official Deadline:</b> {sch['Deadline']} | <b>Coverage:</b> {sch['Funding Type']}</p>
        </div>
        """, unsafe_allow_html=True)

# ---------------------------------------------------------
# TAB 4: COUNTRY STUDY HUB
# ---------------------------------------------------------
with tabs[3]:

    st.subheader("🌍 Country Intelligence Hub")

    selected_country = st.selectbox(
        "Select Study Destination",
        countries_csv["Country"].tolist()
    )

    country_info = countries_csv[
        countries_csv["Country"] == selected_country
    ].iloc[0]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "💰 Cost of Living",
            country_info["Living_Cost"]
        )

    with col2:
        st.metric(
            "💼 Work Rights",
            country_info["Work_Rights"]
        )

    with col3:
        st.metric(
            "🎓 Post-Study Visa",
            country_info["Post_Study_Visa"]
        )

    st.markdown("---")

    st.markdown(f"""
### 🌍 Study in {selected_country}

**Cost of Living:** {country_info["Living_Cost"]}

**Work Rights:** {country_info["Work_Rights"]}

**Post-Study Visa:** {country_info["Post_Study_Visa"]}

ScholarAtlas Country Intelligence provides students with key information for planning their academic journey abroad.
""")

# ---------------------------------------------------------
# TAB 5: UNIVERSITY FINDER
# ---------------------------------------------------------
with tabs[4]:

    st.subheader("🏛️ Global University Intelligence Database")

    selected_country_uni = st.selectbox(
        "Filter Universities by Country",
        ["All"] + sorted(universities_csv["Country"].unique().tolist())
    )

    uni_df = universities_csv.copy()

    if selected_country_uni != "All":
        uni_df = uni_df[
            uni_df["Country"] == selected_country_uni
        ]

    st.dataframe(
        uni_df,
        use_container_width=True
    )

    st.markdown("### 🎓 University Profiles")

    for _, uni in uni_df.iterrows():

        with st.expander(
            f"{uni['University']} ({uni['Country']})"
        ):

            st.write(
                f"**QS Ranking:** {uni['QS_Ranking']}"
            )

            st.write(
                f"**Annual Tuition:** {uni['Tuition']}"
            )

            st.write(
                f"**Minimum IELTS:** {uni['IELTS']}"
            )

# ---------------------------------------------------------
# TAB 6: ESSAY LIBRARY
# ---------------------------------------------------------
with tabs[5]:
    st.subheader("✍️ Winning Essays & SOP Repository")
    st.markdown("""
    <div class="card-box">
        <h4>🏆 Sample Chevening Leadership Essay (Annotated Excerpt)</h4>
        <p><i>"During my clinical officer internship, I spearheaded a community health outreach initiative that served over 1,200 rural patients..."</i></p>
        <p><b>Reviewer Note:</b> Clear use of the STAR method. quantifies exact impact metrics (1,200 patients) and highlights personal initiative.</p>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# TAB 7: CV MASTERCLASS
# ---------------------------------------------------------
with tabs[6]:
    st.subheader("📄 Professional Scholarship CV Builder")
    cv_type = st.radio("Select CV Format", ["Academic CV", "Europass CV", "Development Sector CV"])
    st.info(f"Showing optimal structure for **{cv_type}**: Prioritize Publications, Leadership Initiatives, and Quantifiable Impact.")

# ---------------------------------------------------------
# TAB 8: RECOMMENDATION LETTER TOOLKIT
# ---------------------------------------------------------
with tabs[7]:
    st.subheader("✉️ Referee Guidance & Request Toolkit")
    st.download_button("Download Email Request Template (.txt)", data="Dear Professor [Name],\nI am applying for the [Scholarship Name] and respectfully request a recommendation letter...", file_name="Referee_Request_Template.txt")

# ---------------------------------------------------------
# TAB 9: IELTS COMMAND CENTER
# ---------------------------------------------------------
with tabs[8]:
    st.subheader("🎙️ IELTS Band 8+ Command Center")
    st.markdown("""
    * **Writing Task 2:** 50+ Model Band 9 Essays.
    * **Speaking Simulator:** Interactive Cue Card Prompts.
    * **Academic Vocabulary Bank:** 2,000+ Topic-based words.
    """)

# ---------------------------------------------------------
# TAB 10: PROFILE COMPETITIVENESS ANALYZER
# ---------------------------------------------------------
with tabs[9]:
    st.subheader("📊 Scholarship Readiness Scorecard")
    st.write("Academic Strength: **82%** | Leadership: **95%** | Research: **61%** | Overall: **81%**")
    st.progress(0.81)

# ---------------------------------------------------------
# TAB 11: AFRICA OPPORTUNITIES HUB
# ---------------------------------------------------------
with tabs[10]:
    st.subheader("🌍 Targeted African Youth Opportunities")
    st.markdown("""
    * **African Union Youth Volunteers (AU-YVC)**
    * **Mandela Rhodes Foundation**
    * **AfDB HEST Opportunities**
    * **YALI Regional Leadership Centers**
    """)

# ---------------------------------------------------------
# TAB 12: FELLOWSHIPS & LEADERSHIP
# ---------------------------------------------------------
with tabs[11]:
    st.subheader("🌟 Global Fellowships & Youth Forums")
    st.write("Obama Foundation Leaders, One Young World, UN Youth Delegates, Global Shapers Community.")

# ---------------------------------------------------------
# TAB 13: RESEARCH FUNDING PORTAL
# ---------------------------------------------------------
with tabs[12]:
    st.subheader("🔬 PhD Grants & Conference Travel Funding")
    st.write("Find travel grants, thesis completion awards, and publication fee support schemes.")

# ---------------------------------------------------------
# TAB 14: SUCCESS STORIES
# ---------------------------------------------------------
with tabs[13]:
    st.subheader("🏆 Scholar Spotlights & Winner Profiles")
    st.markdown("""
    > **"I applied twice before securing Chevening. Focusing my leadership essay on measurable community health outcomes was the key turning point."**  
    > — *Jonathan O., Chevening & Public Health Leadership Fellow*
    """)

# ---------------------------------------------------------
# TAB 15: AI SCHOLARSHIP COACH
# ---------------------------------------------------------
with tabs[14]:

    st.subheader("🤖 Scholarship Advisory Coach")

    user_query = st.text_area(
        "Describe your profile",
        placeholder="Example: I am a Clinical Officer from Kenya with GPA 3.4, 2 years experience, interested in Public Health and fully funded Master's scholarships."
    )

    if st.button("Generate Scholarship Advice"):

        st.markdown("### 🎯 Scholarship Recommendations")

        query = user_query.lower()

        matches = []

        for _, sch in scholarships_csv.iterrows():

            score = 0

            if "public health" in query and "public health" in str(sch["Field"]).lower():
                score += 30

            if "clinical" in query and "clinical" in str(sch["Field"]).lower():
                score += 30

            if "master" in query and "master" in str(sch["Level"]).lower():
                score += 20

            if "fully funded" in query and "fully" in str(sch["Funding Type"]).lower():
                score += 20

            matches.append(
                {
                    "Scholarship": sch["Name"],
                    "Country": sch["Host Country"],
                    "Score": score,
                    "Link": sch["Link"]
                }
            )

        results_df = pd.DataFrame(matches)

        results_df = results_df.sort_values(
            "Score",
            ascending=False
        )

        st.data_editor(
            results_df.head(10),
            column_config={
                "Link": st.column_config.LinkColumn(
                    "Apply",
                    display_text="🔗 Apply"
                )
            },
            hide_index=True,
            use_container_width=True
        )

        st.success(
            "Recommendations generated using the ScholarAtlas scholarship database."
        )
# ---------------------------------------------------------
with tabs[15]:

    st.subheader("⭐ My Saved Scholarships")

    if len(st.session_state.saved_scholarships) == 0:

        st.info("You have not saved any scholarships yet.")

    else:

        saved_df = pd.DataFrame(
            st.session_state.saved_scholarships
        )

        st.data_editor(
            saved_df,
            column_config={
                "Link": st.column_config.LinkColumn(
                    "Apply",
                    display_text="🔗 Open"
                )
            },
            hide_index=True,
            use_container_width=True
        )
# TAB 16: COMMUNITY FORUM
# ---------------------------------------------------------
with tabs[17]:
    st.subheader("💬 Peer Application Forum")
    st.text_area("Post a question to the community:", placeholder="Ask about Chevening interview prep, Erasmus Mundus mobility tracks...")
    if st.button("Post Question"):
        st.info("Your question has been posted to the active applicant board!")
