import streamlit as st
from Home import show_home
from utils import show_footer

st.set_page_config(
    page_title="sonbo",
    page_icon=":wave:",
    layout="wide"
)

# 메인 홈 페이지 호출
show_home()
