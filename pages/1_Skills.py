import streamlit as st
from utils import show_footer


st.header("⚙️ Skills")

langs, frameworks, dbs, viz = st.columns(4)

with langs:
    st.subheader("Language")
    st.write("Python")
    st.progress(0.9)

with frameworks:
    st.subheader("ML/DL")
    st.write("PyTorch, TensorFlow")
    st.progress(0.8)

with dbs:
    st.subheader("Database")
    st.write("PostgreSQL")
    st.progress(0.8)

with viz:
    st.subheader("Visualization")
    st.write("Tableau, Matplotlib, Plotly")
    st.progress(0.8)

st.markdown("---")

show_footer()