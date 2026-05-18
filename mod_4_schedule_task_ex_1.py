import schedule
import time

def verification():
    print("Vérification automatique du portefeuille...")

schedule.every(10).seconds.do(verification)

while True:
    schedule.run_pending()
    time.sleep(1)