#!/bin/bash

cd "$(git rev-parse --show-toplevel)"

_scripts/bbl2md.py
_scripts/tex2talks.py
git add pages/publications.md
git add _talks/*.md
git commit -m "Update publications and talks"
git push
