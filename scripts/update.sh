#!/bin/bash

cd "$(git rev-parse --show-toplevel)"

scripts/bbl2md.py
scripts/tex2talks.py
_talkmap/talkmap.py
git add pages/publications.md
git add _talks/*.md
git add _talkmap/
git commit -m "Update publications, talks, and talk map"
git push
