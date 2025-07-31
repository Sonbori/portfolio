import streamlit as st
from utils import show_footer


st.header("💼 Experience & Internships")

# 인턴십 예시
with st.expander("이스트소프트 AI 모델 개발 8기 (교육생)"):
    st.write("**기간:** 2025.02 ~ 2025.07 (5개월)")
    st.write("**주요 성과:**")
    st.write("- 공공데이터 활용 정형 데이터 AI 모델 구현")
    st.write("- 자연과학 데이터 시계열 예측 모델 개발")
    st.write("- 비정형 서비스용 인사이트 도출 애플리케이션 개발")

# 이전 경험
with st.expander("주요 인턴/아르바이트 이력"):
    st.write("• KT 대전 네트워크 서비스센터 (2018.12 ~ 2019.02): 개인정보 보안 및 데이터 정리 분석")
    st.write("• 한국플랫폼서비스기술 (2023.12 ~ 2024.02): 도로/공장 안전사고 예방 데이터 라벨링")
    st.write("• KARI 우주연구원 (2024.02 ~ 2024.03): 간이 위성 제작 및 CUDA 기반 영상 처리")

st.markdown("---")

show_footer()