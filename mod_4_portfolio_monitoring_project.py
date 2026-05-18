import pandas as pd
import sqlite3

df = pd.read_csv("positions.csv")

print("=== MONITORING PORTEFEUILLE ===")

print("\nNombre positions :", len(df))

print("\nPnL total :", df["PnL"].sum())

positions_risquees = df[df["PnL"] < 0]

print("\n=== POSITIONS RISQUÉES ===")
print(positions_risquees)

connexion = sqlite3.connect("controle.db")

df.to_sql("positions", connexion, if_exists="replace", index=False)

connexion.close()

print("\nSauvegarde SQLite terminée")