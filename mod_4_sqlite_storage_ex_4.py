import sqlite3
import pandas as pd

connexion = sqlite3.connect("controle.db")

df = pd.read_csv("positions.csv")

df.to_sql("positions", connexion, if_exists="replace", index=False)

print("Données enregistrées dans SQLite")

connexion.close()