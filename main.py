import requests
import os

BOT_TOKEN = "8950426447:AAGIfbiL6qa5fkGdTOQgb1zH6kbwSQ5nlmE" 
CHANNEL_ID = -1004347664335
def test_bot():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_ID,
        "text": "البوت يعمل بنجاح! إذا وصلت هذه الرسالة، فالمشكلة في الكود السابق وليست في الاتصال."
    }
    response = requests.post(url, json=payload)
    print(response.json())

test_bot()
