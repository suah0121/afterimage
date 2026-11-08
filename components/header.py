import streamlit as st


def render_header():
    st.markdown("""
    <div style="padding:25px 0 30px 0; border-bottom:1px solid #e8e8e5; margin-bottom:35px;">
        <div style="font-size:12px; letter-spacing:5px; color:#999; margin-bottom:12px;">
            DIGITAL ART ARCHIVE
        </div>
        <div style="font-size:32px; font-weight:600; letter-spacing:-1.5px; color:#202020;">
            AFTERIMAGE<span style="color:#b7a58b;">.</span>
        </div>
        <div style="font-size:11px; letter-spacing:2px; color:#999; margin-top:8px;">
            A SPACE FOR DIGITAL ART
        </div>
    </div>
    """, unsafe_allow_html=True)
