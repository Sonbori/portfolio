import streamlit as st
from utils import load_markdown_posts
from utils import show_footer


st.title("🗂️ Archive")

# 검색 및 카테고리 필터
posts = load_markdown_posts()
tags = sorted({t for p in posts for t in p.get('tags',[])})
selected_tags = st.multiselect("태그 선택", options=tags)
q = st.text_input("검색어 입력...")

# 필터링
filtered = [p for p in posts if
    (not selected_tags or any(t in p.get('tags',[]) for t in selected_tags)) and
    (q.lower() in p['title'].lower() or q.lower() in p['content'].lower())]

st.write(f"### {len(filtered)}개의 게시글")
for p in filtered:
    st.markdown(f"- [{p['title']}]({p['path']})  ")

show_footer()