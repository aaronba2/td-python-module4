import pandas as pd

df = pd.read_csv("positions.csv")

positions_risquees = df[df["PnL"] < 0]

if len(positions_risquees) > 0:
    print("ALERTE RISQUE")
    print(positions_risquees)
else:
    print("Aucune position risquée")
