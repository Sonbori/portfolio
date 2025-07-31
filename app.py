import streamlit as st
from Home import show_home

st.set_page_config(
    page_title="손보건 포트폴리오",
    page_icon=":laptop:",
    layout="wide"
)

# 메인 홈 페이지 호출
show_home()