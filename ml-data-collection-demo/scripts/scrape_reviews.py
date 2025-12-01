# scripts/scrape_reviews.py
# NOTE: This script is illustrative. Always obey robots.txt and terms of service.
import requests
from bs4 import BeautifulSoup
import csv
from pathlib import Path

DATA_DIR = Path("data/raw")
DATA_DIR.mkdir(parents=True, exist_ok=True)
output = DATA_DIR / "reviews.csv"

# Placeholder URL(s) for demonstration — replace with allowed targets
urls = [
    "https://example.com/product/123"
]

rows = []
for url in urls:
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
    except Exception as e:
        print("Skipping", url, ":", e)
        continue
    soup = BeautifulSoup(r.text, "html.parser")
    title = soup.select_one("h1.product-title")
    title_text = title.get_text(strip=True) if title else "UNKNOWN"
    for rev in soup.select("div.review"):
        text = rev.select_one("p.text").get_text(strip=True) if rev.select_one("p.text") else ""
        rating = rev.select_one("span.rating").get_text(strip=True) if rev.select_one("span.rating") else ""
        rows.append({"url": url, "title": title_text, "review": text, "rating": rating})

with open(output, "w", newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=["url","title","review","rating"])
    writer.writeheader()
    writer.writerows(rows)
print("Wrote", output)