import streamlit as st
import pathlib


def load_local_css(path: str):
    css = pathlib.Path(path).read_text(encoding="utf-8")
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


load_local_css("assets/style.css")


from Home import show_home
from utils import show_visitor_count


st.set_page_config(
    page_title="sonbo",
    page_icon=":wave:",
    layout="wide"
)

# 메인 홈 페이지 호출
show_home()

show_visitor_count()