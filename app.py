import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.write('Hello!!!!,:sunglasses:') 
st.write('Hello!!!!,:sunglasses:') 
st.title('Title *Markdown* 인식') 
st.header('Title *Markdown* 인식') 
st.subheader('Title *Markdown* 인식') 

st.text('title *Markdown* 인식못함.') 
st.markdown('*Markdown* 출력.') 

st.text('This is some text.') 
x=10
y=20
st.write('x=',x,'y=',y) 

df = pd.DataFrame({'col1':[1,2,3]}) 
st.write('데이터 프레임',df) 
df # 데이터프레임을 직접 작성하여 출력도 가능 

arr = np.random.normal(1,1,size=100) 
fig, ax = plt.subplots() 
ax.hist(arr, bins=20) 
st.pyplot(fig)