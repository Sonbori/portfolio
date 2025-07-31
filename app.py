import streamlit as st
from Home import show_home

st.set_page_config(
    page_title="sonbo",
    page_icon=":wave:",
    layout="wide"
)

# 메인 홈 페이지 호출
show_home()
show_footer()