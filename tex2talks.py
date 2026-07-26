#!/usr/bin/env python3

"""Convert Hennes' LaTeX CV talk lists into _talks/*.md files for Jekyll."""

import re
import unicodedata
from datetime import date

CONF_FILE = "../hennes-data/vitae/english/talks.tex"
SEMINAR_FILE = "../hennes-data/vitae/english/selected.tex"
OUTPUT_DIR = "_talks"

# Conference-talk macros: name -> (number of args, type label)
# 4-arg form:  {conference/workshop name}{location}{date}{title}
# 5-arg form:  {abbreviation}{full name}{location}{date}{title}
CONF_MACROS = {
    "confContr":     (4, "Contributed talk"),
    "confMini":      (4, "Minisymposium talk"),
    "confInv":       (4, "Invited talk"),
    "abbConfContr":  (5, "Contributed talk"),
    "abbConfMini":   (5, "Minisymposium talk"),
    "abbConfInv":    (5, "Invited talk"),
}

MONTHS = {
    "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
    "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12,
}

# Seminar hosts whose location field in the .tex is just a bare country
# (no city). Add a ("keyword in institute name", "city") entry here whenever
# a future \seminar{} entry has this problem.
SEMINAR_CITY_OVERRIDES = [
    ("Clausthal", "Clausthal-Zellerfeld"),
    ("Saarbrücken", "Saarbrücken"),
    ("Trends in Scientific Computing", "Dortmund"),
    ("Lappeenranta", "Lappeenranta"),
    ("TU Dortmund", "Dortmund"),
    ("University of Oslo", "Oslo"),
    ("University of Zürich", "Zürich"),
]


def clean_latex(s):
    s = s.replace("\\ ", " ").replace("~", " ")
    s = s.replace("\\-", "")
    s = s.replace("\\&", "&").replace("\\%", "%")

    # accents: \'e, \`a, \"o, \^e, \c{c}, \v{c} (braces around the letter optional)
    accents = [(r"\\'", "\u0301"), (r"\\`", "\u0300"), (r'\\"', "\u0308"),
               (r"\\\^", "\u0302"), (r"\\c", "\u0327"), (r"\\v", "\u030C")]
    for pattern, combining in accents:
        s = re.sub(pattern + r"\{?([a-zA-Z])\}?", lambda m, c=combining: unicodedata.normalize("NFC", m.group(1) + c), s)

    # strip no-op formatting commands, innermost first, repeatedly (handles nesting)
    while True:
        new = re.sub(r"\\(?:textbf|textit|textsc|emph|normalfont|text)\{([^{}]*)\}", r"\1", s)
        if new == s:
            break
        s = new

    s = re.sub(r"\s+", " ", s).strip()
    if "\\" in s:
        print(f"warning: unhandled LaTeX escape left in cleaned string: {s!r}")
    return s


def parse_conf_date(raw):
    s = clean_latex(raw)
    year = int(re.findall(r"\d{4}", s)[-1])
    month = MONTHS[re.search(r"Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec", s).group()]
    day = int(re.search(r"\d{1,2}", s).group())
    return date(year, month, day)


def parse_seminar_date(raw):
    s = clean_latex(raw)
    m = re.search(r"([A-Za-z]+)\.?\s+(\d{1,2}),\s*(\d{4})", s)
    month = MONTHS[m.group(1)[:3].capitalize()]
    return date(int(m.group(3)), month, int(m.group(2)))


def slugify(s, max_words=6):
    words = re.sub(r"[^a-zA-Z0-9]+", " ", s).strip().lower().split()
    return "-".join(words[:max_words])


def yaml_str(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def find_macro_calls(text, names):
    """Yield (name, [args]) for each `\\name{...}{...}...` call, brace-aware."""
    pattern = re.compile(r"\\(" + "|".join(re.escape(n) for n in names) + r")\{")
    pos = 0
    while True:
        m = pattern.search(text, pos)
        if not m:
            return
        name = m.group(1)
        n_args = CONF_MACROS[name][0] if name in CONF_MACROS else 4
        args = []
        cursor = m.end() - 1  # points at the opening '{' of the first arg
        for _ in range(n_args):
            assert text[cursor] == "{"
            depth = 1
            start = cursor + 1
            i = start
            while depth > 0:
                if text[i] == "{":
                    depth += 1
                elif text[i] == "}":
                    depth -= 1
                i += 1
            args.append(text[start:i - 1])
            cursor = i
        args_end = cursor
        yield name, args
        pos = args_end


def strip_comments(text):
    return "\n".join(line for line in text.splitlines() if not line.lstrip().startswith("%"))


def resolve_seminar_place(institute, raw_location):
    location = clean_latex(raw_location)
    if "," in location:
        return location, location.split(",")[0].strip()
    city = next((c for kw, c in SEMINAR_CITY_OVERRIDES if kw in institute), None)
    if city is None:
        print(f"warning: no city known for seminar host {institute!r} (location is just {location!r}); "
              f"add an entry to SEMINAR_CITY_OVERRIDES")
        city = location
    return f"{city}, {location}", city


def conf_entries():
    text = strip_comments(open(CONF_FILE).read())
    for name, args in find_macro_calls(text, list(CONF_MACROS)):
        talk_type = CONF_MACROS[name][1]
        if len(args) == 4:
            venue_name, raw_location, raw_date, raw_title = args
        else:
            abbrev, full_name, raw_location, raw_date, raw_title = args
            venue_name = f"{clean_latex(abbrev)}: {clean_latex(full_name)}"

        location = clean_latex(raw_location)
        city = location.split(",")[0].strip()
        yield {
            "title": clean_latex(raw_title),
            "type": talk_type,
            "venue": clean_latex(venue_name) if len(args) == 4 else venue_name,
            "location": location,
            "city": city,
            "date": parse_conf_date(raw_date),
        }


def seminar_entries():
    text = strip_comments(open(SEMINAR_FILE).read())
    for name, args in find_macro_calls(text, ["seminar"]):
        raw_title, raw_institute, raw_location, raw_date = args
        institute = clean_latex(raw_institute)
        location, city = resolve_seminar_place(institute, raw_location)
        yield {
            "title": clean_latex(raw_title),
            "type": "Invited seminar",
            "venue": institute,
            "location": location,
            "city": city,
            "date": parse_seminar_date(raw_date),
        }


def write_talk(entry, seen_slugs):
    slug = slugify(entry["title"])
    candidate = slug
    n = 2
    key = f"{entry['date'].isoformat()}-{candidate}"
    while key in seen_slugs:
        candidate = f"{slug}-{n}"
        key = f"{entry['date'].isoformat()}-{candidate}"
        n += 1
    seen_slugs.add(key)

    permalink = f"/talks/{key}"
    front_matter = "\n".join([
        "---",
        f"title: {yaml_str(entry['title'])}",
        "collection: talks",
        f"type: {yaml_str(entry['type'])}",
        f"venue: {yaml_str(entry['venue'])}",
        f"date: {entry['date'].isoformat()}",
        f"location: {yaml_str(entry['location'])}",
        f"city: {yaml_str(entry['city'])}",
        f"permalink: {permalink}",
        "---",
        "",
    ])

    with open(f"{OUTPUT_DIR}/{key}.md", "w") as f:
        f.write(front_matter)


if __name__ == "__main__":
    seen = set()
    count = 0
    for entry in list(conf_entries()) + list(seminar_entries()):
        write_talk(entry, seen)
        count += 1
    print(f"wrote {count} talk files to {OUTPUT_DIR}/")
