import streamlit as st
from utils.image_handler import get_image_path


def render_artwork_card(artwork):
    image_path = get_image_path(artwork.get("image"))

    with st.container(border=True):
        if image_path:
            st.image(image_path, use_container_width=True)
        else:
            st.markdown(
                "<div style='background:#eeeeeb;height:220px;"
                "display:flex;align-items:center;justify-content:center;"
                "color:#999;'>NO IMAGE</div>",
                unsafe_allow_html=True
            )

        st.markdown(
            f"**{artwork.get('title', 'Untitled')}**"
        )

        st.caption(
            f"{artwork.get('category', 'ART')} · "
            f"{artwork.get('author', 'Anonymous')}"
        )

        if artwork.get("description"):
            st.write(artwork["description"])
