import streamlit as st
from utils.data_manager import get_projects, get_exhibitions
from components.artwork_card import render_artwork_card
from components.exhibition_card import render_exhibition_card


def render_home():

    st.markdown("""
        <div style="padding: 55px 0 75px 0;">
            <p style="
                font-size: 11px;
                letter-spacing: 4px;
                color: #999;
            ">A DIGITAL ART PLATFORM</p>

            <h1 style="
                font-size: 64px;
                font-weight: 500;
                letter-spacing: -4px;
                margin: 20px 0;
            ">AFTERIMAGE.</h1>

            <p style="
                font-size: 17px;
                color: #777;
                line-height: 1.9;
            ">
                사라진 순간 이후에도 남아 있는 것들.<br>
                작품과 시선이 머무는 디지털 전시 공간.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # FEATURED ARTWORKS
    st.markdown("### SELECTED WORKS")
    st.caption("다양한 시선으로 완성된 작품들")

    projects = get_projects()

    if projects:
        cols = st.columns(3)

        for i, project in enumerate(projects[:6]):
            with cols[i % 3]:
                render_artwork_card(project)
    else:
        st.info("아직 등록된 작품이 없습니다.")

    st.markdown("---")

    # EXHIBITIONS
    st.markdown("### CURRENT EXHIBITIONS")
    st.caption("지금 AFTERIMAGE에서 만날 수 있는 전시")

    exhibitions = get_exhibitions()

    if exhibitions:
        for exhibition in exhibitions[:3]:
            render_exhibition_card(exhibition)
    else:
        st.info("현재 등록된 전시가 없습니다.")

    st.markdown("---")

    st.markdown("""
        <div style="
            padding: 35px 0;
            text-align: center;
            color: #999;
            font-size: 11px;
            letter-spacing: 2px;
        ">
            AFTERIMAGE · DIGITAL ART ARCHIVE
        </div>
    """, unsafe_allow_html=True)
