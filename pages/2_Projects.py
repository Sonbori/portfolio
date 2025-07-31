import streamlit as st

st.header("🏆 Projects")

# 프로젝트 A
with st.expander("프로젝트 A: 공공데이터 AI 모델 개발"):
    st.write("**기간:** 2025.02 ~ 2025.05 (4개월)")
    st.write("**역할:** 데이터 전처리, 모델링, 배포")
    st.write("**기술:** Python, Pandas, Scikit-learn, Streamlit")
    st.write("**성과:** 랜덤포레스트 모델로 85% 정확도 달성")
    st.image("images/project_a.png", caption="Feature 중요도 시각화")
    st.write("**배운 점:** 데이터 파이프라인 구축 경험, 모델 해석 기법 익힘")

# 프로젝트 B
with st.expander("프로젝트 B: 시계열 예측 모델 구현"):
    st.write("**기간:** 2024.10 ~ 2024.12 (3개월)")
    st.write("**역할:** 데이터 수집 및 모델 개발")
    st.write("**기술:** Python, Pandas, Prophet, Plotly")
    st.write("**성과:** 월별 판매량 예측 MAPE 10% 달성")
    st.image("images/project_b.png", caption="예측 결과 그래프")
    st.write("**배운 점:** 시계열 데이터 전처리 및 Prophet 활용법 익힘")

# 프로젝트 C
with st.expander("프로젝트 C: 비정형 텍스트 분류"):
    st.write("**기간:** 2024.06 ~ 2024.08 (2개월)")
    st.write("**역할:** 텍스트 전처리, 모델 평가")
    st.write("**기술:** Python, NLTK, Hugging Face Transformers")
    st.write("**성과:** BERT 기반 분류기로 F1-score 0.82 달성")
    st.image("images/project_c.png", caption="발표자료 슬라이드")
    st.write("**배운 점:** NLP 전처리 및 Transfer Learning 경험")

st.markdown("---")