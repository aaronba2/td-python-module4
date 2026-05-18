import pandas as pd

df = pd.read_csv("positions.csv")

positions_risquees = df[df["PnL"] < 0]

print("=== ALERTES RISQUE ===")
print(positions_risquees)