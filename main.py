import os
import time
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = "@Market_Hunter_Channel"
MARKET_API_URL = "https://api.getgems.io/v1/asset/marketplace" 

def check_deals():
    try:
        response = requests.get(MARKET_API_URL, timeout=10)
        if response.status_code == 200:
            data = response.json()
            pass 
    except Exception as e:
        print(f"Error checking market: {e}")

def send_alert(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)

if __name__ == "__main__":
    print("Market Hunter Bot is running...")
    while True:
        check_deals()
        time.sleep(60)
