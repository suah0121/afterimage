import streamlit as st
from utils.data_manager import get_projects
from components.artwork_card import render_artwork_card
from config import ARTWORK_CATEGORIES


def render_explore():
    st.markdown("# EXPLORE")
    st.caption("Discover artworks from different perspectives.")

    projects = get_projects()

    # 검색 및 필터
    col1, col2 = st.columns([2, 1])

    with col1:
        keyword = st.text_input(
            "작품 검색",
            placeholder="작품명 또는 작가명을 검색하세요."
        )

    with col2:
        category = st.selectbox(
            "카테고리",
            ARTWORK_CATEGORIES
        )

    filtered = projects

    if keyword:
        filtered = [
            p for p in filtered
            if keyword.lower() in p.get("title", "").lower()
            or keyword.lower() in p.get("author", "").lower()
        ]

    if category != "전체":
        filtered = [
            p for p in filtered
            if p.get("category") == category
        ]

    st.markdown("---")
    st.caption(f"TOTAL {len(filtered)} WORKS")

    if filtered:
        cols = st.columns(3)

        for i, project in enumerate(filtered):
            with cols[i % 3]:
                render_artwork_card(project)
    else:
        st.info("검색 결과가 없습니다.")
