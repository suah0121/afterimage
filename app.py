
import streamlit as st
import streamlit.components.v1 as components

# ==========================================
# AFTERIMAGE.
# ==========================================

st.set_page_config(
    page_title="AFTERIMAGE.",
    page_icon="✳",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if "page" not in st.session_state:
    st.session_state.page = "landing"


# ==========================================
# STREAMLIT 기본 디자인
# ==========================================

st.markdown("""
<style>
[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stSidebar"] {
    display: none;
}

[data-testid="stAppViewContainer"] {
    background: #080808;
}

.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

.stButton {
    display: flex;
    justify-content: center;
}

.stButton > button {
    background: transparent;
    color: #e8d34b;
    border: 1px solid #bba936;
    border-radius: 0;
    padding: 12px 20px;
    font-size: 10px;
    letter-spacing: 2px;
    min-height: 48px;
    transition: 0.3s;
}

.stButton > button:hover {
    background: #e8d34b;
    color: #080808;
    border-color: #e8d34b;
}

.stButton > button:focus {
    box-shadow: none;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# LANDING PAGE
# ==========================================

def landing_page():

    html = """
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="UTF-8">

    <style>

    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500&family=Playfair+Display:wght@400;500&display=swap');

    * {
        box-sizing: border-box;
    }

    html, body {
        margin: 0;
        padding: 0;
        width: 100%;
        height: 100%;
        background: #080808;
        color: white;
        font-family: 'DM Sans', sans-serif;
        overflow: hidden;
    }

    .landing {
        width: 100%;
        height: 850px;
        position: relative;
        background: #080808;
        overflow: hidden;
    }

    /* TOP BAR */

    .topbar {
        height: 90px;
        padding: 0 7%;
        display: flex;
        justify-content: space-between;
        align-items: center;
        position: relative;
        z-index: 10;
    }

    .logo {
        color: #e8d34b;
        font-family: 'Playfair Display', serif;
        font-size: 21px;
        letter-spacing: 1px;
    }

    .nav {
        display: flex;
        gap: 42px;
        color: #b7b7b7;
        font-size: 10px;
        letter-spacing: 2px;
    }

    .nav span {
        transition: color .3s;
        cursor: pointer;
    }

    .nav span:hover {
        color: #e8d34b;
    }

    /* FLOWER */

    .flower {
        position: absolute;
        top: 3%;
        right: 3%;
        width: 57%;
        height: 90%;

        background-image:
            linear-gradient(
                90deg,
                #080808 0%,
                rgba(8,8,8,.4) 25%,
                rgba(8,8,8,.05) 75%,
                rgba(8,8,8,.2) 100%
            ),
            url('https://images.unsplash.com/photo-1490750967868-88aa4486c946?auto=format&fit=crop&w=1800&q=90');

        background-size: cover;
        background-position: center;
        filter: grayscale(100%) brightness(.55) contrast(1.1);
        opacity: .78;
        transform-origin: center;
        animation: flowerMove 9s ease-in-out infinite alternate;
    }

    @keyframes flowerMove {
        from {
            transform: rotate(-1deg) scale(1);
        }
        to {
            transform: rotate(1deg) scale(1.035);
        }
    }

    /* CURVE */

    .curve {
        position: absolute;
        width: 100%;
        height: 100%;
        inset: 0;
        z-index: 2;
        pointer-events: none;
    }

    .curve path {
        fill: none;
        stroke: rgba(255,255,255,.68);
        stroke-width: .8;
        stroke-dasharray: 1800;
        stroke-dashoffset: 1800;
        animation: drawLine 5s ease forwards .5s;
    }

    @keyframes drawLine {
        to {
            stroke-dashoffset: 0;
        }
    }

    /* HERO TEXT */

    .hero {
        position: absolute;
        top: 50%;
        left: 10%;
        transform: translateY(-50%);
        z-index: 5;
        animation: appear 1.6s ease forwards;
    }

    @keyframes appear {
        from {
            opacity: 0;
            transform: translateY(calc(-50% + 35px));
        }
        to {
            opacity: 1;
            transform: translateY(-50%);
        }
    }

    .eyebrow {
        color: #b6b6b6;
        font-size: 10px;
        letter-spacing: 5px;
        margin-bottom: 28px;
    }

    .title {
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
        color: #999;
        font-size: 12px;
        line-height: 2.2;
        margin-top: 25px;
        letter-spacing: .5px;
    }

    /* BOTTOM */

    .bottom {
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

    @media(max-width: 700px) {
        .topbar {
            padding: 0 6%;
        }

        .nav {
            gap: 15px;
            font-size: 8px;
        }

        .flower {
            width: 100%;
            right: -25%;
            opacity: .4;
        }

        .hero {
            left: 7%;
        }

        .title {
            font-size: 58px;
            letter-spacing: -3px;
        }

        .subtitle {
            font-size: 9px;
            letter-spacing: 3px;
        }
    }

    </style>
    </head>

    <body>

    <div class="landing">

        <header class="topbar">

            <div class="logo">
                AFTERIMAGE.
            </div>

            <nav class="nav">
                <span>EXPLORE</span>
                <span>ABOUT</span>
                <span>CREATE</span>
            </nav>

        </header>

        <div class="flower"></div>

        <svg class="curve"
             viewBox="0 0 1440 850"
             preserveAspectRatio="none">

            <path d="
                M -100 650
                C 250 400, 430 760, 720 500
                S 1150 150, 1550 300
            "/>

        </svg>

        <main class="hero">

            <div class="eyebrow">
                A DIGITAL ART EXHIBITION PLATFORM
            </div>

            <h1 class="title">
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

        </main>

        <div class="bottom">
            <span>EST. 2026</span>
            <span>AN EXHIBITION THAT STAYS WITH YOU.</span>
        </div>

    </div>

    </body>
    </html>
    """

    components.html(
        html,
        height=850,
        scrolling=False
    )

    # Streamlit buttons

    st.markdown("""
    <style>
    .button-space {
        height: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns([2, 1.5, 1.5, 2])

    with col2:
        if st.button("EXPLORE EXHIBITIONS", use_container_width=True):
            st.session_state.page = "explore"
            st.rerun()

    with col3:
        if st.button("START CREATING", use_container_width=True):
            st.session_state.page = "studio"
            st.rerun()


# ==========================================
# INNER PAGE
# ==========================================

def inner_page(title, description):

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="UTF-8">

    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400&family=Playfair+Display:wght@400;500&display=swap');

    * {{
        box-sizing: border-box;
    }}

    body {{
        margin: 0;
        background: #f8f8f6;
        color: #222;
        font-family: 'DM Sans', sans-serif;
    }}

    .page {{
        min-height: 800px;
        padding: 55px 8%;
        background: #f8f8f6;
    }}

    .logo {{
        font-family: 'Playfair Display', serif;
        color: #b9a52c;
        font-size: 25px;
    }}

    .title {{
        font-family: 'Playfair Display', serif;
        font-size: 55px;
        font-weight: 400;
        margin-top: 65px;
    }}

    .description {{
        color: #777;
        font-size: 14px;
        margin-top: 10px;
    }}
    </style>
    </head>

    <body>
        <div class="page">
            <div class="logo">AFTERIMAGE.</div>
            <div class="title">{title}</div>
            <div class="description">{description}</div>
        </div>
    </body>
    </html>
    """

    components.html(
        html,
        height=800,
        scrolling=False
    )

    if st.button("← BACK TO HOME", key="back_home"):
        st.session_state.page = "landing"
        st.rerun()


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
