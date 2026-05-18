import pandas as pd

df = pd.read_csv("positions.csv")

rapport = df.groupby("Produit")["PnL"].sum()

print("=== RAPPORT AUTOMATIQUE ===")
print(rapport)