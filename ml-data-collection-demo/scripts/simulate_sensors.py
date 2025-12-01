# scripts/simulate_sensors.py
import csv
import random
from datetime import datetime
from pathlib import Path

DATA_DIR = Path("data/raw")
DATA_DIR.mkdir(parents=True, exist_ok=True)
out = DATA_DIR / "sensor_sim.csv"

with open(out, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['timestamp','sensor_id','temperature_c'])
    for i in range(100):
        ts = datetime.utcnow().isoformat()
        temp = 20 + random.normalvariate(0, 1.5)
        writer.writerow([ts, 'sensor_1', f"{temp:.2f}"])
print('Wrote', out)