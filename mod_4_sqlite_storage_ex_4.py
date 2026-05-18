import sqlite3

connexion = sqlite3.connect("controle.db")

curseur = connexion.cursor()

curseur.execute("""
CREATE TABLE IF NOT EXISTS operations (
    produit TEXT,
    pnl INTEGER
)
""")

curseur.execute("INSERT INTO operations VALUES ('Bitcoin', 250)")
curseur.execute("INSERT INTO operations VALUES ('Ethereum', -120)")

connexion.commit()

curseur.execute("SELECT * FROM operations")

resultats = curseur.fetchall()

print("=== DONNÉES ENREGISTRÉES ===")

for ligne in resultats:
    print(ligne)

connexion.close()
