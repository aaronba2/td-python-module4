import pandas as pd

df = pd.read_csv("positions.csv")

print(df)

nombre_positions = len(df)

pnl_total = df["PnL"].sum()

print("\nNombre total de positions :", nombre_positions)

print("PnL total :", pnl_total)
