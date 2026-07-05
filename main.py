import os
import time
import requests
import json

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = "@Market_Hunter_Channel"
# الرابط المخصص لمجموعة الهدايا المطورة (Gift Sets)
MARKET_API_URL = "https://api.getgems.io/v1/nft/search?collection=EQAOQdwd327K4W7X9vYk2bM31r8q4N8mY3-w3Xn3-w3Xn3-w&sort=price_asc" 

def send_alert_with_button(name, price, link):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    
    keyboard = {
        "inline_keyboard": [
            [{"text": "🛒 اشترِ الآن", "url": link}]
        ]
    }
    
    payload = {
        "chat_id": CHANNEL_ID,
        "text": f"💎 <b>صيدة جديدة في الماركت!</b>\n\n🏷 <b>الاسم:</b> {name}\n💰 <b>السعر:</b> {price} TON",
        "parse_mode": "HTML",
        "reply_markup": json.dumps(keyboard)
    }
    requests.post(url, json=payload)

def check_deals():
    try:
        response = requests.get(MARKET_API_URL, timeout=10)
        if response.status_code == 200:
            items = response.json().get('items', [])
            if items:
                # البوت سيقوم الآن بفحص أرخص قطعة متاحة في المجموعة
                item = items[0]
                name = item.get('name', 'غير معروف')
                price = item.get('sale', {}).get('price', 0) / 1000000000
                link = f"https://getgems.io/nft/{item.get('address')}"
                
                send_alert_with_button(name, price, link)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    while True:
        check_deals()
        time.sleep(300) # فحص كل 5 دقائق
