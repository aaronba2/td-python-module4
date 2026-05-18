import schedule
import time

def controle():
    print("Contrôle portefeuille exécuté")

schedule.every(5).seconds.do(controle)

while True:
    schedule.run_pending()
    time.sleep(1)
