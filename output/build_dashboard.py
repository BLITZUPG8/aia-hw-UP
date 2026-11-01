"""สร้าง output/dashboard.html จาก claims.csv และ companies.json

วิธีใช้: python3 output/build_dashboard.py
แก้ข้อมูลที่ claims.csv หรือ companies.json แล้วรันใหม่ ห้ามแก้ dashboard.html ตรง ๆ
"""
import csv
import json
from datetime import date
from pathlib import Path

HERE = Path(__file__).parent

claims = list(csv.DictReader(open(HERE / "claims.csv", encoding="utf-8-sig")))
companies = json.load(open(HERE / "companies.json", encoding="utf-8"))

data = {"claims": claims, "companies": companies, "built": date.today().isoformat()}
template = (HERE / "dashboard_template.html").read_text(encoding="utf-8")
html = template.replace("/*__DATA__*/null", json.dumps(data, ensure_ascii=False))
(HERE / "dashboard.html").write_text(html, encoding="utf-8")
print(f"dashboard.html: {len(companies)} บริษัท · {len(claims)} ข้อ")
