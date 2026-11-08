import textwrap
import streamlit as st
import streamlit.components.v1 as components

# ==========================================
# AFTERIMAGE.
# 1단계: Landing Page
# ==========================================

st.set_page_config(
    page_title="AFTERIMAGE.",
    page_icon="✳",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 페이지 상태
if "page" not in st.session_state:
    st.session_state.page = "landing"

# ==========================================
# CSS
# ==========================================

st.markdown("""
<style>

/* 기본 설정 */
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500&family=Playfair+Display:wght@400;500;600&display=swap');

* {
    box-sizing: border-box;
}

html, body, [data-testid="stAppViewContainer"] {
    background: #080808;
    color: #ffffff;
    font-family: 'DM Sans', sans-serif;
}

[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stToolbar"] {
    display: none;
}

[data-testid="stSidebar"] {
    display: none;
}

.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

/* Streamlit 기본 요소 */
.stButton {
    display: flex;
    justify-content: center;
}

.stButton > button {
    background: transparent;
    color: #e8d34b;
    border: 1px solid rgba(232,211,75,0.65);
    border-radius: 0;
    padding: 13px 30px;
    font-family: 'DM Sans', sans-serif;
    font-size: 11px;
    letter-spacing: 2px;
    transition: all 0.35s ease;
}

.stButton > button:hover {
    background: #e8d34b;
    color: #080808;
    border-color: #e8d34b;
    transform: translateY(-2px);
}

.stButton > button:focus {
    box-shadow: none;
    border-color: #e8d34b;
}

/* 랜딩 페이지 */
.landing {
    min-height: 100vh;
    width: 100%;
    position: relative;
    overflow: hidden;
    background: #080808;
    display: flex;
    flex-direction: column;
}

/* 상단 메뉴 */
.topbar {
    height: 90px;
    padding: 0 7%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: relative;
    z-index: 10;
}

.logo-small {
    color: #e8d34b;
    font-family: 'Playfair Display', serif;
    font-size: 19px;
    letter-spacing: 1px;
}

.nav {
    display: flex;
    gap: 42px;
    color: #b7b7b7;
    font-size: 10px;
    letter-spacing: 2px;
}

/* 메인 영역 */
.hero {
    position: relative;
    min-height: 690px;
    height: calc(100vh - 90px);
    display: flex;
    align-items: center;
    padding: 0 10%;
    overflow: hidden;
}

/* 꽃 이미지 */
.flower {
    position: absolute;
    right: 4%;
    top: 4%;
    width: 53%;
    height: 88%;
    background-image:
        linear-gradient(
            90deg,
            #080808 0%,
            rgba(8,8,8,0.15) 45%,
            rgba(8,8,8,0.12) 100%
        ),
        url('https://images.unsplash.com/photo-1490750967868-88aa4486c946?auto=format&fit=crop&w=1800&q=90');
    background-size: cover;
    background-position: center;
    filter: grayscale(100%) brightness(0.55) contrast(1.12);
    opacity: 0.75;
    animation: flowerMove 9s ease-in-out infinite alternate;
    transform-origin: center;
}

@keyframes flowerMove {
    0% { transform: rotate(-1deg) scale(1); }
    100% { transform: rotate(1deg) scale(1.035); }
}

/* 흰색 곡선 */
.curve {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 2;
}

.curve path {
    fill: none;
    stroke: rgba(255,255,255,0.65);
    stroke-width: 0.8;
    stroke-dasharray: 1800;
    stroke-dashoffset: 1800;
    animation: drawLine 5s ease forwards 0.6s;
}

@keyframes drawLine {
    to { stroke-dashoffset: 0; }
}

/* 제목 */
.hero-content {
    position: relative;
    z-index: 5;
    margin-top: -15px;
    animation: titleAppear 1.6s ease forwards;
}

@keyframes titleAppear {
    from {
        opacity: 0;
        transform: translateY(35px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.eyebrow {
    color: #b6b6b6;
    font-size: 10px;
    letter-spacing: 5px;
    margin-bottom: 28px;
}

.main-title {
    color: #e8d34b;
    font-family: 'Playfair Display', serif;
    font-size: clamp(65px, 9.5vw, 145px);
    font-weight: 400;
    letter-spacing: -6px;
    line-height: 1;
    white-space: nowrap;
    margin: 0;
}

.subtitle {
    color: #e2e2e2;
    font-size: 12px;
    letter-spacing: 5px;
    margin-top: 30px;
    font-weight: 300;
}

.description {
    color: #999999;
    font-size: 12px;
    line-height: 2.2;
    margin-top: 25px;
    letter-spacing: 0.5px;
}

/* 하단 정보 */
.bottom-info {
    position: absolute;
    bottom: 30px;
    left: 7%;
    right: 7%;
    display: flex;
    justify-content: space-between;
    color: #777;
    font-size: 9px;
    letter-spacing: 2px;
    z-index: 5;
}

/* 내부 페이지 */
.inner-page {
    min-height: 100vh;
    background: #f8f8f6;
    color: #222;
    padding: 55px 8%;
}

.inner-logo {
    font-family: 'Playfair Display', serif;
    color: #b9a52c;
    font-size: 25px;
}

.inner-title {
    font-family: 'Playfair Display', serif;
    font-size: 55px;
    font-weight: 400;
    margin-top: 65px;
}

.inner-description {
    color: #777;
    font-size: 14px;
    margin-top: 10px;
}

@media(max-width: 700px) {
    .topbar {
        padding: 0 6%;
    }

    .nav {
        gap: 15px;
        font-size: 8px;
    }

    .hero {
        min-height: 650px;
        padding: 0 7%;
    }

    .flower {
        width: 100%;
        right: -25%;
        opacity: 0.4;
    }

    .main-title {
        font-size: 58px;
        letter-spacing: -3px;
    }

    .subtitle {
        font-size: 9px;
        letter-spacing: 3px;
    }

    .bottom-info {
        font-size: 7px;
    }
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# LANDING PAGE
# ==========================================

def landing_page():

   st.markdown(textwrap.dedent("""
    <div class="landing">

        <header class="topbar">
            <div class="logo-small">AFTERIMAGE.</div>

            <nav class="nav">
                <span>EXPLORE</span>
                <span>ABOUT</span>
                <span>CREATE</span>
            </nav>
        </header>

        <main class="hero">

            <div class="flower"></div>

            <svg class="curve" viewBox="0 0 1440 850"
                 preserveAspectRatio="none">
                <path d="
                    M -100 650
                    C 250 400, 430 760, 720 500
                    S 1150 150, 1550 300
                "/>
            </svg>

            <div class="hero-content">

                <div class="eyebrow">
                    A DIGITAL ART EXHIBITION PLATFORM
                </div>

                <h1 class="main-title">AFTERIMAGE.</h1>

                <div class="subtitle">
                    YOUR ART. YOUR WORLD.
                </div>

                <div class="description">
                    Create your own exhibition.<br>
                    Give your artworks a space to exist.<br>
                    Leave something behind.
                </div>

            </div>

            <div class="bottom-info">
                <span>EST. 2026</span>
                <span>AN EXHIBITION THAT STAYS WITH YOU.</span>
            </div>

        </main>
    </div>
"""), unsafe_allow_html=True)

        <header class="topbar">
            <div class="logo-small">AFTERIMAGE.</div>

            <nav class="nav">
                <span>EXPLORE</span>
                <span>ABOUT</span>
                <span>CREATE</span>
            </nav>
        </header>

        <main class="hero">

            <div class="flower"></div>

            <svg class="curve" viewBox="0 0 1440 850"
                 preserveAspectRatio="none">
                <path d="
                    M -100 650
                    C 250 400, 430 760, 720 500
                    S 1150 150, 1550 300
                "/>
            </svg>

            <div class="hero-content">

                <div class="eyebrow">
                    A DIGITAL ART EXHIBITION PLATFORM
                </div>

                <h1 class="main-title">
                    AFTERIMAGE.
                </h1>

                <div class="subtitle">
                    YOUR ART. YOUR WORLD.
                </div>

                <div class="description">
                    Create your own exhibition.<br>
                    Give your artworks a space to exist.<br>
                    Leave something behind.
                </div>

            </div>

            <div class="bottom-info">
                <span>EST. 2026</span>
                <span>AN EXHIBITION THAT STAYS WITH YOU.</span>
            </div>

        </main>
    </div>
    """, unsafe_allow_html=True)

    # 실제 Streamlit 버튼
    col1, col2, col3, col4 = st.columns([2, 1, 1, 2])

    with col2:
        if st.button("EXPLORE EXHIBITIONS", use_container_width=True):
            st.session_state.page = "explore"
            st.rerun()

    with col3:
        if st.button("START CREATING", use_container_width=True):
            st.session_state.page = "studio"
            st.rerun()


# ==========================================
# 임시 내부 페이지
# ==========================================

def inner_page(title, description):

st.markdown(textwrap.dedent(f"""
    <div class="inner-page">

        <div class="inner-logo">AFTERIMAGE.</div>

        <div class="inner-title">{title}</div>

        <div class="inner-description">
            {description}
        </div>

    </div>
"""), unsafe_allow_html=True)


# ==========================================
# PAGE ROUTER
# ==========================================

if st.session_state.page == "landing":
    landing_page()

elif st.session_state.page == "studio":
    inner_page(
        "MY STUDIO",
        "Manage your creative projects."
    )

elif st.session_state.page == "explore":
    inner_page(
        "EXPLORE",
        "Discover exhibitions from different creators."
    )
