import streamlit as st


def render_exhibition_card(exhibition):
    with st.container(border=True):
        st.markdown(
            f"### {exhibition.get('title', 'Untitled Exhibition')}"
        )

        st.caption(
            f"{exhibition.get('date', '')} "
            f"· {exhibition.get('status', '예정')}"
        )

        if exhibition.get("description"):
            st.write(exhibition["description"])

        if exhibition.get("cover"):
            st.image(
                exhibition["cover"],
                use_container_width=True
            )
