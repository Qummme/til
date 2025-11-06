import sys, re, pathlib, yaml

for path in pathlib.Path("logbook").glob("*.md"):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        print(f"❌ Missing YAML header in {path}")
        sys.exit(1)
    data = yaml.safe_load(match.group(1))
    if not data.get("tags"):
        print(f"❌ Missing tags in {path}")
        sys.exit(1)
print("✅ Tag check passed.")

