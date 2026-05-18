import pandas as pd

df = pd.read_csv("positions.csv")

def rapport():

    nombre_positions = len(df)

    pnl_total = df["PnL"].sum()

    positions_perdantes = df[df["PnL"] < 0]

    print("=== RAPPORT AUTOMATIQUE ===")

    print("\nNombre positions :", nombre_positions)

    print("PnL total :", pnl_total)

    print("\n=== POSITIONS PERDANTES ===")

    print(positions_perdantes)

rapport()
