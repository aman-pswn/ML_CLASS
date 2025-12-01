# tools/validate_data.py
import pandas as pd
from pathlib import Path
import sys

p = Path('data/raw/synthetic.csv')
if not p.exists():
    print('ERROR: expected sample dataset at', p)
    sys.exit(2)

df = pd.read_csv(p)
print('rows', len(df))
nulls = df.isnull().sum().sum()
print('nulls', nulls)
if nulls > 0:
    print('Validation failed: null values present')
    sys.exit(3)

if 'label' not in df.columns:
    print('Validation failed: label column missing')
    sys.exit(4)

print('Basic validation passed')