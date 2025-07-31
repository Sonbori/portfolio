import streamlit as st
from utils import show_footer


st.header("📬 Contact & Inquiry")
st.write("이메일: thsqhrjs@gmail.com")
st.write("전화: +82-10-7234-6844")

with st.form(key="contact_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    if st.form_submit_button("Send Message"):
        st.success("메시지가 성공적으로 전송되었습니다!\n빠른 시일 내에 연락드리겠습니다.")

show_footer()