import pandas as pd
import sqlite3
import schedule
import time

def monitoring_portefeuille():

    print("=== MONITORING PORTEFEUILLE ===")

    # Chargement des données
    df = pd.read_csv("positions.csv")

    # Nombre de positions
    nombre_positions = len(df)

    # PnL total
    pnl_total = df["PnL"].sum()

    print("\nNombre positions :", nombre_positions)

    print("\nPnL total :", pnl_total)

    # Détection des positions risquées
    positions_risquees = df[df["PnL"] < 0]

    if len(positions_risquees) > 0:

        print("\nALERTE RISQUE")

        print(positions_risquees)

    else:

        print("\nAucune position risquée")

    # Export des alertes
    positions_risquees.to_csv("alertes.csv", index=False)

    print("\nExport alertes.csv effectué")

    # Meilleure position
    meilleur = df.loc[df["PnL"].idxmax()]

    print("\n=== MEILLEURE POSITION ===")

    print(meilleur)

    # Ajout colonne risque
    df["Risque"] = df["PnL"].apply(
        lambda x: "Élevé" if x < 0 else "Faible"
    )

    print("\n=== DONNÉES AVEC RISQUE ===")

    print(df)

    # Sauvegarde SQLite
    connexion = sqlite3.connect("controle.db")

    df.to_sql(
        "positions",
        connexion,
        if_exists="replace",
        index=False
    )

    connexion.close()

    print("\nSauvegarde SQLite OK")


# Planification automatique toutes les 10 secondes
schedule.every(10).seconds.do(monitoring_portefeuille)

print("Contrôle portefeuille lancé...\n")

# Boucle automatique
while True:

    schedule.run_pending()

    time.sleep(1)
