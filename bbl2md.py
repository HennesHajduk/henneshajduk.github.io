#!/usr/bin/env python3

import re

files = {
    "Books": "../hennes-data/vitae/book.bbl",
    "Journal Articles": "../hennes-data/vitae/journal.bbl",
    "Proceedings": "../hennes-data/vitae/proceeding.bbl",
    "Preprints": "../hennes-data/vitae/preprint.bbl",
    "Thesis": "../hennes-data/vitae/thesis.bbl",
}

def process_bbl(path):
    with open(path) as f:
        text = f.read()

    # remove everything before first \bibitem
    text = re.split(r"\\bibitem", text, maxsplit=1)[-1]
    text = "\\bibitem" + text

    # split entries
    entries = re.split(r"\\bibitem\{.*?\}", text)

    html_entries = []

    # common latex special chars / accents
    latex_map = {
        r'\{\\"a\}': "ä",
        r'\{\\"A\}': "Ä",
        r'\{\\"o\}': "ö",
        r'\{\\"O\}': "Ö",
        r'\{\\"u\}': "ü",
        r'\{\\"U\}': "Ü",
        r"{\\ss}"  : "ß",
        r"{\\ae}"  : "æ",
        r"{\\AE}"  : "Æ",
        r"{\\oe}"  : "œ",
        r"{\\OE}"  : "Œ",
        r"{\\o}"   : "ø",
        r"{\\O}"   : "Ø",
        r"{\\aa}"  : "å",
        r"{\\AA}"  : "Å",
    }

    for e in entries:
        e = e.strip()
        if not e:
            continue

        # handle special characters
        for k, v in latex_map.items():
            e = re.sub(k, v, e)

        e = re.sub(r"\s+", " ", e)
        e = e.replace("~", " ")
        e = e.replace("--", "-")
        e = re.sub(
            r"\\urlprefix\s*\\url\{(.*?)\}",
            r'URL: <a href="\1">\1</a>',
            e
        )
        e = re.sub(
            r"\\url\{(.*?)\}",
            r'<a href="\1">\1</a>',
            e
        )
        e = re.sub(
            r"\\arxiv\{(.*?)\}\{(.*?)\}",
            r'Preprint, arXiv: <a href="https://arxiv.org/abs/\1">\1</a> [\2]',
            e
        )
        e = re.sub(r"\\textsc\{(.*?)\}", r"<span style='font-variant: small-caps;'>\1</span>", e)
        e = re.sub(r"\\emph\{(.*?)\}", r"<em>\1</em>", e)
        e = re.sub(r"\\textbf\{(.*?)\}", r"<strong>\1</strong>", e)
        e = re.sub(r"\\doi\{(.*?)\}", r'<a href="https://doi.org/\1">doi:\1</a>', e)
        e = e.replace("{B}achelor", "Bachelor")
        e = re.sub(r"\\texttt\{(.*?)\}", r"\1", e)

        # remove remaining latex commands
        e = re.sub(r"\\[a-zA-Z]+\{.*?\}", "", e)

        html_entries.append(f"<p>{e}</p>")

    return "\n".join(html_entries)


# build markdown file
output = """---
title: "Publications"
permalink: /publications/
---

"""

for section, path in files.items():
    html = process_bbl(path)

    output += f"## {section}\n<div>\n{html}\n</div>\n\n"


with open("_pages/publications.md", "w") as f:
    f.write(output)
