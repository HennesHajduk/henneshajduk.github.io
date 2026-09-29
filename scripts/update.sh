#!/bin/bash

cd "$(git rev-parse --show-toplevel)"

git pull
scripts/bbl2md.py
scripts/tex2talks.py
# talkmap.py needs frontmatter/geopy/getorg, which live in this venv
"$HOME/ml/venv/bin/python3" _talkmap/talkmap.py
git add pages/publications.md
git add _talks/*.md
git add _talkmap/
git commit -m "Update publications, talks, and talk map"
git push
