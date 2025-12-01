# scripts/collect_public.py
import requests
from pathlib import Path

DATA_DIR = Path("data/raw")
DATA_DIR.mkdir(parents=True, exist_ok=True)
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
out = DATA_DIR / "wine.data"

r = requests.get(url, timeout=20)
r.raise_for_status()
with open(out, "wb") as f:
    f.write(r.content)
print("Saved to", out)