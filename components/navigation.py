import streamlit as st


def render_navigation():
    menu_items = [
        "HOME",
        "EXPLORE",
        "EXHIBITION",
        "ABOUT",
        "ADMIN"
    ]

    if "current_page" not in st.session_state:
        st.session_state.current_page = "HOME"

    cols = st.columns(len(menu_items))

    for col, item in zip(cols, menu_items):
        with col:
            is_active = st.session_state.current_page == item

            if st.button(
                item,
                key=f"nav_{item}",
                use_container_width=True,
                type="primary" if is_active else "secondary"
            ):
                st.session_state.current_page = item
                st.rerun()

    st.markdown(
        "<hr style='margin-top:10px; margin-bottom:35px;'>",
        unsafe_allow_html=True
    )

    return st.session_state.current_page
