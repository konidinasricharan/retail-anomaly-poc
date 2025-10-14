import markdown
import sys
from pathlib import Path

md_file = Path("mini_paper.md")
html_file = Path("mini_paper.html")

if not md_file.exists():
    print("mini_paper.md not found. Please create it first.")
    sys.exit(1)

md_text = md_file.read_text(encoding="utf-8")
html_body = markdown.markdown(md_text, extensions=['fenced_code','tables'])
html_template = f"""<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Mini Paper - Retail Anomaly Detection</title>
  <style>
    body {{ font-family: Arial, sans-serif; margin: 40px; line-height:1.4; color:#222 }}
    h1,h2,h3 {{ color: #0b3d91; }}
    pre {{ background:#f6f8fa; padding:10px; border-radius:6px; }}
    table {{ border-collapse: collapse; width:100%; }}
    table, th, td {{ border: 1px solid #ddd; padding: 8px; }}
    code {{ background:#eee; padding:2px 4px; border-radius:4px; }}
  </style>
</head>
<body>
{html_body}
</body>
</html>"""

html_file.write_text(html_template, encoding="utf-8")
print("Wrote", html_file.resolve())
