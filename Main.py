import os
import time
import requests
from flask import Flask
from threading import Thread

# --- SERVER MINIMO PER RENDER ---
app = Flask('')
@app.route('/')
def home(): return "Bot Oro Online"

def run():
    app.run(host='0.0.0.0', port=10000) # Render usa spesso la porta 10000

# --- CONFIGURAZIONE TELEGRAM ---
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def invia_messaggio(testo):
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        params = {"chat_id": CHAT_ID, "text": testo, "parse_mode": "Markdown"}
        requests.get(url, params=params)
    except Exception as e:
        print(f"Errore invio: {e}")

if __name__ == "__main__":
    # Avvia il server web per far stare buono Render
    t = Thread(target=run)
    t.start()
    
    # Messaggio di prova per capire se è vivo
    invia_messaggio("✅ Bot Oro collegato con successo da Render!")
    
    print("Bot in ascolto...")
    while True:
        # Qui poi metteremo la logica dello stocastico
        # Per ora lo teniamo acceso e basta per testare
        time.sleep(30)
