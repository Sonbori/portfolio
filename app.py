# streamlit_portfolio_blog/app.py
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import requests

# 페이지 설정
st.set_page_config(
    page_title="손보건 Portofolio & Blog",
    page_icon="📂",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Lottie 애니메이션 로드 함수
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# 상단 네비게이션
selected = option_menu(
    menu_title=None,
    options=["Home", "Skills", "Projects", "Archive", "Experience", "Resume", "Contact"],
    icons=["house", "gear", "project-diagram", "archive", "briefcase", "file-earmark-text", "envelope"],
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#282a36"},
        "icon": {"color": "#bd93f9", "font-size": "20px"},
        "nav-link": {"font-size": "16px", "text-align": "center", "margin": "0px 10px", "color": "#f8f8f2"},
        "nav-link-selected": {"background-color": "#44475a", "color": "#50fa7b"}
    }
)

# 마인드맵(Graphviz) 사이드바
with st.sidebar:
    st.markdown("## 사이트 구조")
    graph = st.graphviz_chart(
        '''
        digraph G {
          node [shape=box, style=filled, color="#44475a", fontcolor="#f8f8f2"];
          Home -> Skills;
          Home -> Projects;
          Home -> Archive;
          Home -> Experience;
          Home -> Resume;
          Home -> Contact;
        }
        ''', use_container_width=True)

# Lottie 배경 애니메이션 (Home에만)
if selected == "Home":
    from Home import show_home
    lottie = load_lottie("https://assets5.lottiefiles.com/packages/lf20_jcikwtux.json")
    if lottie:
        st_lottie(lottie, height=200, key="intro")
    show_home()
elif selected == "Skills":
    from pages_1_Skills import show_skills; show_skills()
elif selected == "Projects":
    from pages_2_Projects import show_projects; show_projects()
elif selected == "Archive":
    from pagesArchive import show_archive; show_archive()
elif selected == "Experience":
    from pages_3_Experience import show_experience; show_experience()
elif selected == "Resume":
    from pages_4_Resume import show_resume; show_resume()
elif selected == "Contact":
    from pages_5_Contact import show_contact; show_contact()
