import streamlit as st


def render_about():
    st.markdown("# ABOUT AFTERIMAGE")

    st.markdown("""
    <div style="padding: 45px 0;">
        <p style="font-size:12px; letter-spacing:4px; color:#999;">
            BEYOND THE MOMENT
        </p>

        <h1 style="font-size:48px;">
            AFTERIMAGE.
        </h1>

        <p style="font-size:18px; color:#777; line-height:2;">
            순간은 사라져도, 그 순간이 남긴 감각은 계속된다.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### OUR PURPOSE")

    st.write("""
    AFTERIMAGE는 다양한 디지털 작품과 창작자의 시선을
    하나의 공간에서 만날 수 있도록 만들어진 온라인 전시 플랫폼입니다.

    장르와 형식에 제한 없이 작품을 소개하고,
    관람자와 창작자가 새로운 영감을 나누는 공간을 지향합니다.
    """)

    st.markdown("---")

    st.markdown("### WHAT WE VALUE")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("#### 01. ART")
        st.caption("다양한 형태의 창작과 표현")

    with col2:
        st.markdown("#### 02. CONNECTION")
        st.caption("작품과 사람 사이의 연결")

    with col3:
        st.markdown("#### 03. ARCHIVE")
        st.caption("순간과 감각의 기록")

    st.markdown("---")

    st.caption("AFTERIMAGE · DIGITAL ART ARCHIVE")
