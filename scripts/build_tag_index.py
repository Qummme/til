import re, pathlib, yaml, json, datetime

root = pathlib.Path("logbook")
section_pattern = re.compile(r"^##\s+(.+?)\s+#(\w+)", re.MULTILINE)
index = {}

for file in sorted(root.glob("*.md")):
    text = file.read_text(encoding="utf-8")
    fm = re.match(r"---\n(.*?)\n---", text, re.DOTALL)
    date = None
    if fm:
        front = yaml.safe_load(fm.group(1))
        date = front.get("date")
        # 👇 ここで日付を文字列化しておく
        if isinstance(date, (datetime.date, datetime.datetime)):
            date = date.isoformat()
    sections = section_pattern.findall(text)
    for title, tag in sections:
        index.setdefault(tag, []).append({
            "file": file.name,
            "date": date,
            "title": title.strip(),
        })

pathlib.Path("tag_index.json").write_text(
    json.dumps(index, indent=2, ensure_ascii=False),
    encoding="utf-8"
)
print("✅ tag_index.json updated.")

