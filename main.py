import requests
import os

BOT_TOKEN = "ضع_التوكن_هنا" # ضع التوكن الذي حصلت عليه
CHANNEL_ID = "@Market_Hunter_Channel"

def test_bot():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_ID,
        "text": "البوت يعمل بنجاح! إذا وصلت هذه الرسالة، فالمشكلة في الكود السابق وليست في الاتصال."
    }
    response = requests.post(url, json=payload)
    print(response.json())

test_bot()
