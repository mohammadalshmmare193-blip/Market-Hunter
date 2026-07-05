import os
import time
import requests
import json
from flask import Flask
from threading import Thread

app = Flask(__name__)
@app.route('/')
def home():
    return "Bot is hunting continuously!"

def run():
    app.run(host='0.0.0.0', port=8080)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = "@Market_Hunter_Channel"

MARKET_URLS = [
    "https://api.getgems.io/v1/nft/search?collection=EQCD3DWcnrH2csxHLM5S55hL1vB51v6Y-y4t2_M1V8m4S-9v&sort=listed_at_desc",
    "https://api.getgems.io/v1/nft/search?collection=EQAOQdwd327K4W7X9vYk2bM31r8q4N8mY3-w3Xn3-w3Xn3-w&sort=listed_at_desc",
    "https://api.getgems.io/v1/nft/search?collection=EQDk80u94s_s4x7c-0k500p3J5_18G7C7V7-p4_18G7C7V7-p4&sort=listed_at_desc"
]

def send_alert(name, price, link, image_url):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    keyboard = {"inline_keyboard": [[{"text": "🛒 اشترِ الآن", "url": link}]]}
    payload = {
        "chat_id": CHANNEL_ID,
        "photo": image_url,
        "caption": f"💎 <b>صفقة جديدة في الماركت!</b>\n\n🏷 <b>الاسم:</b> {name}\n💰 <b>السعر:</b> {price} TON",
        "parse_mode": "HTML",
        "reply_markup": json.dumps(keyboard)
    }
    requests.post(url, json=payload)

def check_deals():
    for url in MARKET_URLS:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                items = response.json().get('items', [])
                if items:
                    item = items[0] # ينشر آخر قطعة نزلت فوراً
                    name = item.get('name', 'غير معروف')
                    price = item.get('sale', {}).get('price', 0) / 1000000000
                    link = f"https://getgems.io/nft/{item.get('address')}"
                    image_url = item.get('image', '')
                    send_alert(name, price, link, image_url)
            time.sleep(5) # انتظار بسيط بين كل متجر
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    t = Thread(target=run)
    t.start()
    while True:
        check_deals()
        time.sleep(60) # تحديث كل دقيقة بدلاً من 5
