import streamlit as st
from utils import show_footer


st.header("📝 Resume")

st.subheader("학력")
st.write("- 한밭고등학교 졸업 (2014.03 - 2017.02)")
st.write("- 대전보건대학교 컴퓨터정보과 졸업 (2018.03 - 2025.02)")

st.subheader("자격증")
st.write("• 정보처리기사 (2023)")
st.write("• ADsP (2023)")

st.subheader("수상내역")
st.write("• 교내 아이디어 공모전 우수상 (2021)")
st.write("• ICCT 캡스톤 대회 최우수상 (2022)")
st.write("• 대전지역 문제해결 창업경진대회 우수상 (2024)")

st.subheader("대외활동")
st.write("• 밴드 동아리 활동 (2018~2025)")
st.write("• AI 스터디 멤버, 블로그 글 기고")

show_footer()