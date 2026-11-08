import streamlit as st
from utils.data_manager import get_exhibitions


def render_exhibition():
    st.markdown("# EXHIBITION")
    st.caption("Explore curated digital exhibitions.")

    exhibitions = get_exhibitions()

    if not exhibitions:
        st.info("아직 등록된 전시가 없습니다.")
        return

    for exhibition in exhibitions:
        with st.container(border=True):
            if exhibition.get("cover"):
                st.image(
                    exhibition["cover"],
                    use_container_width=True
                )

            st.markdown(f"## {exhibition.get('title', 'Untitled')}")

            st.caption(
                f"{exhibition.get('status', '예정')} "
                f"· {exhibition.get('date', '')}"
            )

            st.write(
                exhibition.get("description", "")
            )

            with st.expander("전시 자세히 보기"):
                st.write(
                    exhibition.get(
                        "detail",
                        "전시 소개가 준비 중입니다."
                    )
                )
