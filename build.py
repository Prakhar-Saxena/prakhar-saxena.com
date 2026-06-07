#!/usr/bin/env python3
import json
import re
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from markupsafe import Markup, escape


def md_bold_to_html(text):
    escaped = str(escape(text))
    return Markup(re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', escaped))


def build():
    data = json.loads(Path('data.json').read_text())

    html_env = Environment(loader=FileSystemLoader('templates'), autoescape=True)
    html_env.filters['md_bold'] = md_bold_to_html

    md_env = Environment(loader=FileSystemLoader('templates'), autoescape=False)

    Path('index.html').write_text(html_env.get_template('index.html.j2').render(d=data))
    print('Generated index.html')

    Path('README.md').write_text(md_env.get_template('README.md.j2').render(d=data))
    print('Generated README.md')


if __name__ == '__main__':
    build()
