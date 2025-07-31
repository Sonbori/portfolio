import streamlit as st
import os
import yaml
from pathlib import Path

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