# scripts/synth_data.py
import pandas as pd
import numpy as np
from pathlib import Path

DATA_DIR = Path("data/raw")
DATA_DIR.mkdir(parents=True, exist_ok=True)

n_samples = 200
n_features = 8
rng = np.random.default_rng(42)
X = rng.normal(size=(n_samples, n_features))
# simple linear separable labels with noise
weights = rng.normal(size=(n_features,))
logits = X.dot(weights)
y = (logits + rng.normal(scale=0.5, size=n_samples) > 0).astype(int)

df = pd.DataFrame(X, columns=[f"f{i}" for i in range(n_features)])
df['label'] = y
out = DATA_DIR / 'synthetic.csv'
df.to_csv(out, index=False)
print('Saved', out)