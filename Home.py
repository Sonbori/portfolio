import streamlit as st

# 프로필 및 소개

def show_home():
    st.title("안녕하세요, 손보건입니다. 🖐️")
    
    col1, col2 = st.columns([1, 2], gap="large")
    with col1:
        st.image("images/son.png", caption="손보건", width=200)
    with col2:
        st.subheader("효과적인 데이터 분석 신입")
        st.subheader("AI 개발자 & 데이터사이언티스트 지망생")
        st.write(
            """
            • 말 한마디 하더라도 듣기 좋게 말하는 것을 중요하게 생각합니다.
            
            • 프롬프트 구상력이 뛰어납니다.
            
            • 새로운 툴을 금방 익힙니다.
            """
        )
        st.markdown("---")
        st.write(
            "✉️ thsqhrjs@gmail.com   |   📞 +82-10-7234-6844"
        )
        st.write(
            "🔗 [GitHub](https://github.com/Sonbori)  |  📝 [Blog](https://velog.io/@sonbo/posts)  |  📸 [Instagram](https://www.instagram.com/)"
        )