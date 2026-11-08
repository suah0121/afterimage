import streamlit as st

from utils.data_manager import (
    get_projects, add_project, delete_project,
    get_exhibitions, add_exhibition, delete_exhibition
)
from utils.image_handler import save_image

def render_admin():
    st.markdown("# ADMIN")
    st.caption("AFTERIMAGE CONTENT MANAGEMENT")

    tab1, tab2, tab3, tab4 = st.tabs([
        "작품 등록", "작품 관리", "전시 등록", "전시 관리"
    ])

    # 작품 등록
    with tab1:
        st.markdown("### NEW ARTWORK")

        with st.form("add_project_form"):
            title = st.text_input("작품명")
            author = st.text_input("작가명")
            category = st.selectbox(
                "카테고리",
                ["디지털 아트", "일러스트", "사진", "영상", "기타"]
            )
            description = st.text_area("작품 설명")
            uploaded_image = st.file_uploader(
                "작품 이미지",
                type=["png", "jpg", "jpeg", "webp"]
            )

            submitted = st.form_submit_button(
                "작품 등록",
                use_container_width=True
            )

            if submitted:
                if not title or not author:
                    st.error("작품명과 작가명을 입력해 주세요.")
                else:
                    image_path = save_image(uploaded_image)

                    add_project({
                        "title": title,
                        "author": author,
                        "category": category,
                        "description": description,
                        "image": image_path
                    })

                    st.success("작품이 등록되었습니다!")
                    st.rerun()

    # 작품 관리
    with tab2:
        st.markdown("### MANAGE ARTWORKS")

        projects = get_projects()

        if projects:
            selected = st.selectbox(
                "삭제할 작품 선택",
                projects,
                format_func=lambda p: p.get("title", "Untitled"),
                key="delete_project"
            )

            if st.button("선택한 작품 삭제", type="primary"):
                delete_project(selected["id"])
                st.success("작품이 삭제되었습니다.")
                st.rerun()
        else:
            st.info("등록된 작품이 없습니다.")

    # 전시 등록
    with tab3:
        st.markdown("### NEW EXHIBITION")

        with st.form("add_exhibition_form"):
            title = st.text_input("전시명")
            date = st.text_input("전시 기간")
            status = st.selectbox(
                "전시 상태",
                ["예정", "진행 중", "종료"]
            )
            description = st.text_area("전시 소개")
            detail = st.text_area("상세 설명")
            uploaded_cover = st.file_uploader(
                "전시 대표 이미지",
                type=["png", "jpg", "jpeg", "webp"]
            )

            submitted = st.form_submit_button(
                "전시 등록",
                use_container_width=True
            )

            if submitted:
                if not title:
                    st.error("전시명을 입력해 주세요.")
                else:
                    cover_path = save_image(uploaded_cover)

                    add_exhibition({
                        "title": title,
                        "date": date,
                        "status": status,
                        "description": description,
                        "detail": detail,
                        "cover": cover_path
                    })

                    st.success("전시가 등록되었습니다!")
                    st.rerun()

    # 전시 관리
    with tab4:
        st.markdown("### MANAGE EXHIBITIONS")

        exhibitions = get_exhibitions()

        if exhibitions:
            selected = st.selectbox(
                "삭제할 전시 선택",
                exhibitions,
                format_func=lambda e: e.get("title", "Untitled"),
                key="delete_exhibition"
            )

            if st.button("선택한 전시 삭제", type="primary"):
                delete_exhibition(selected["id"])
                st.success("전시가 삭제되었습니다.")
                st.rerun()
        else:
            st.info("등록된 전시가 없습니다.")
