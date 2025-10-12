# examples/load_numerics.py
import pandas as pd
import yaml
import pathlib

# repo root = parent of the 'examples' folder
root = pathlib.Path(__file__).resolve().parents[1]

csv_path  = root / "numerics" / "data" / "models_accuracies.csv"
yaml_path = root / "numerics" / "settings.yaml"

# Load data
acc = pd.read_csv(csv_path)
with open(yaml_path, "r") as f:
    settings = yaml.safe_load(f)

# Build counts from effective N in settings
N_eff = settings["samples"]["N_per_subdomain"]
acc["N_ij"] = N_eff
acc["C_ij"] = (acc["theta_hat"] * N_eff).round().astype(int)

print("=== models_accuracies.csv (first few rows) ===")
print(acc.head(8).to_string(index=False))

print("\n=== settings.yaml keys ===")
print(list(settings.keys()))
