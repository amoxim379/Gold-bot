import os
import time
import requests
from flask import Flask
from threading import Thread

# --- SERVER WEB PER RENDER (Necessario per non far crashare il bot) ---
app = Flask('')

@app.route('/')
def home():
    return "Bot Oro Online!"

def run():
    # Render usa la porta 10000 di default
    app.run(host='0.0.0.0', port=10000)

# --- CONFIGURAZIONE TELEGRAM ---
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def invia_messaggio(testo):
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        params = {
            "chat_id": CHAT_ID, 
            "text": testo, 
            "parse_mode": "Markdown"
        }
        requests.get(url, params=params)
    except Exception as e:
        print(f"Errore invio: {e}")

if __name__ == "__main__":
    # Avvia il server web in un thread separato
    t = Thread(target=run)
    t.start()
    
    # Invia un messaggio di test per confermare che funziona
    invia_messaggio("✅ *Bot Oro Online!*\nIl collegamento con Render è riuscito. Ora sono attivo 24/7.")
    
    print("Bot acceso...")
    
    # Ciclo infinito per tenere il processo attivo
    while True:
        # Qui gira la logica del tuo trading
        time.sleep(30)
