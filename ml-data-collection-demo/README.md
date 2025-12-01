# ML Data Collection Demo

This repository demonstrates multiple ways to collect data for Machine Learning with small, runnable examples.
It is intentionally minimal and educational. Do **not** commit secrets to Git; store them in environment variables.

## Structure
```
ml-data-collection-demo/
├─ README.md
├─ LICENSE
├─ .gitignore
├─ data/
│  ├─ raw/            # small example raw files (<10MB)
│  └─ processed/      # processed for model training
├─ scripts/
│  ├─ collect_public.py
│  ├─ scrape_reviews.py
│  ├─ collect_api.py
│  ├─ simulate_sensors.py
│  └─ synth_data.py
├─ notebooks/
│  └─ exploration.ipynb
├─ tools/
│  └─ validate_data.py
└─ .github/workflows/
   └─ data-check.yml
```
## Quickstart

1. Inspect `scripts/` to see example collection scripts (they are minimal and educational).
2. Run `python scripts/synth_data.py` to generate a small synthetic CSV in `data/raw/`.
3. Run `python tools/validate_data.py` to run a basic validation check.
4. Use `.gitignore` to avoid committing large raw files or secrets. For large datasets, prefer S3/GCS and keep a manifest file in this repo.

## Files included
- Small synthetic dataset `data/raw/synthetic.csv` (100 rows) for testing.
- Example scripts to show common data collection patterns (public downloads, scraping, APIs, simulated sensors, synthetic).
- A sample GitHub Actions workflow to run the validation on push (operates on small sample files).