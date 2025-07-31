import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

_, col, _ = st.columns([2,6,2])
col.header("Streamlit 시각화")

dfIris = sns.load_dataset('iris') 
colors = {"setosa":"red", "virginica":"green", "versicolor":"blue"}
st.sidebar.title('Iris Species🌸') # 사이드바 제목 
with st.sidebar: # 사이드바 안에 위젯 배치
    selectX = st.selectbox("X 변수 선택:", ["sepal_length", "sepal_width", "petal_length", "petal_width"]) 
    selectY = st.selectbox("Y 변수 선택:", ["sepal_length", "sepal_width", "petal_length", "petal_width"]) 
    selectSpecies = st.multiselect("붓꽃 유형 선택 (:blue[다중]):",["setosa", "versicolor", "virginica"]) 
    selectAlpha = st.slider("alpha 설정:", 0.1, 1.0, 0.5) 

# 선택된 붓꽃 유형별 산점도로 시각화 표현
if selectSpecies: # 붓꽃 유형이 선택되었을 경우 
    fig = plt.figure(figsize=(7,5)) # 그래프 크기 설정 
    for aSpecies in selectSpecies: # 선택된 각 종(species)에 대해 
        df = dfIris[dfIris.species==aSpecies] # 해당 종의 데이터만 필터링 
        plt.scatter(df[selectX], df[selectY], color=colors[aSpecies], alpha=selectAlpha, label=aSpecies) 
    plt.legend(loc="lower right") # 범례 위치 설정 
    plt.xlabel(selectX) # X축 레이블 설정 
    plt.ylabel(selectY) # Y축 레이블 설정 
    plt.title("Iris Scatter Plot") # 그래프 제목 설정 
    st.pyplot(fig) # Streamlit에 Matplotlib 그래프 표시 
else: # 붓꽃 유형이 선택되지 않았을 경우 
    st.warning("붓꽃의 유형을 선택해 주세요!!!") # 경고 메시지 표시 