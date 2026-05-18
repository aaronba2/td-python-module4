import pandas as pd
import sqlite3
import schedule
import time


# Fonction de vérification du risque
def verifier_risque(pnl):

    if pnl < 0:
        return "Élevé"

    return "Faible"


# Fonction principale de monitoring
def monitoring_portefeuille():

    print("\n=== MONITORING PORTEFEUILLE ===")

    # Chargement des données CSV
    df = pd.read_csv("positions.csv")

    # Nombre total de positions
    nombre_positions = len(df)

    # Calcul du PnL total
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
    df["Risque"] = df["PnL"].apply(verifier_risque)

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

print("Contrôle portefeuille lancé...")


# Boucle automatique
while True:

    schedule.run_pending()

    time.sleep(1)
