#!/bin/bash

./bbl2md.py
./tex2talks.py
git add pages/publications.md
git add _talks/*.md
git commit -m "Update publications and talks"
git push
