import streamlit as st
from pathlib import Path

from config import SITE_NAME
from components.header import render_header
from components.navigation import render_navigation

from pages.home import render_home
from pages.explore import render_explore
from pages.exhibition import render_exhibition
from pages.about import render_about
from pages.admin import render_admin


# 기본 설정
st.set_page_config(
    page_title=SITE_NAME,
    page_icon="✳",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS 불러오기
css_path = Path(__file__).parent / "styles" / "main.css"

if css_path.exists():
    with open(css_path, encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# 기본 레이아웃
st.markdown("""
<style>
[data-testid="stSidebar"] {
    display: none;
}

.block-container {
    padding-top: 1.5rem;
}
</style>
""", unsafe_allow_html=True)

# 헤더
render_header()

# 내비게이션
page = render_navigation()

# 페이지 연결
if page == "HOME":
    render_home()

elif page == "EXPLORE":
    render_explore()

elif page == "EXHIBITION":
    render_exhibition()

elif page == "ABOUT":
    render_about()

elif page == "ADMIN":
    render_admin()
