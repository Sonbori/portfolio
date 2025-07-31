import streamlit as st
import datetime, json, os
import yaml
from pathlib import Path

DATA_PATH = "data/visitor_count.json"

def load_counts():
    if not os.path.exists(DATA_PATH):
        counts = {"total": 0, "today": 0, "yesterday": 0, "date": str(datetime.date.today())}
    else:
        counts = json.load(open(DATA_PATH, "r", encoding="utf-8"))
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
    lines = path.read_text(encoding='utf-8').splitlines()
    if lines[0]=='---':
        end = lines[1:].index('---')+1
        meta = yaml.safe_load("\n".join(lines[1:end]))
        content = "\n".join(lines[end+1:])
    else:
        meta = {}
        content = path.read_text(encoding='utf-8')
    return meta, content