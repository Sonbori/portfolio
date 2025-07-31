import streamlit as st
import datetime, json, os
from pathlib import Path

DATA_PATH = "data/visitor_count.json"

def load_counts():
    if not os.path.exists(DATA_PATH):
        counts = {"total": 0, "today": 0, "yesterday": 0, "date": str(datetime.date.today())}
    else:
        try:
            with open(DATA_PATH, "r", encoding="utf-8") as fp:
                counts = json.load(fp)
        except (ValueError, json.JSONDecodeError):
            # 파일이 비어 있거나 JSON이 깨졌을 때 기본값으로 초기화
            counts = {"total": 0, "today": 0, "yesterday": 0, "date": str(datetime.date.today())}
    return counts

def save_counts(counts):
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(counts, f)

def increment_count():
    counts = load_counts()
    today = str(datetime.date.today())
    if counts["date"] != today:
        counts["yesterday"] = counts["today"]
        counts["today"] = 0
        counts["date"] = today
    counts["today"] += 1
    counts["total"] += 1
    save_counts(counts)
    return counts

def show_footer():
    counts = increment_count()
    st.markdown(
        f"""
        <div class="footer">
          © 2025 Shin's AI & ML/DL Learning Hub. All Rights Reserved.<br>
          (오늘: {counts["today"]} | 어제: {counts["yesterday"]} | 전체: {counts["total"]})
        </div>
        """,
        unsafe_allow_html=True
    )
def load_markdown_posts(folder="posts"):
    posts = []
    for md in sorted(Path(folder).glob("*.md")):
        meta, content = parse_md(md)
        posts.append({**meta, "content": content, "path": md})
    return posts

def parse_md(path):
    """파일 상단에 --- 구분 front-matter가 있으면 수동 파싱, 없으면 전체를 content로."""
    lines = path.read_text(encoding='utf-8').splitlines()
    meta = {}
    content_start = 0
    if len(lines) >= 3 and lines[0].strip() == '---':
        # 두 번째 '---' 찾기
        try:
            end_idx = lines[1:].index('---') + 1
            # front-matter 구역
            for ln in lines[1:end_idx]:
                if ':' in ln:
                    k, v = ln.split(':', 1)
                    k = k.strip()
                    v = v.strip()
                    # tags는 [a,b] 형태로 파싱
                    if k == 'tags':
                        items = v.strip('[]').split(',')
                        meta['tags'] = [it.strip().strip('\"').strip('\'') for it in items if it.strip()]
                    else:
                        meta[k] = v.strip('\"').strip('\'')
        except ValueError:
            end_idx = 0
        content_start = end_idx + 1
    content = "\n".join(lines[content_start:])
    return meta, content
 