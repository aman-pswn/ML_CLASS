# scripts/collect_api.py
import os
from pathlib import Path
import requests

DATA_DIR = Path("data/raw")
DATA_DIR.mkdir(parents=True, exist_ok=True)

owm_key = os.getenv('OPENWEATHER_API_KEY')  # DO NOT hardcode keys
city = "London"
if owm_key:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={owm_key}"
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    (DATA_DIR / "weather_london.json").write_text(r.text)
    print('Saved weather_london.json')
else:
    print('Missing OPENWEATHER_API_KEY — set as env var before running this script')