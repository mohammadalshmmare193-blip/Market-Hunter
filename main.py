import os
import requests
import time
from flask import Flask
from threading import Thread

app = Flask(__name__)

# هذا المسار يجعله "Web Service" يستجيب للطلب
@app.route('/')
def home():
    return "البوت يعمل الآن!"

# دالة لتشغيل البوت في الخلفية
def bot_logic():
    BOT_TOKEN = "8950426447:AAGIfbiL6qa5fkGdT0Qgb1zH6kbwSQ5nlmE"
    CHANNEL_ID = -1004347664335
    
    # رسالة عند بدء التشغيل
    try:
        requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", 
                      json={"chat_id": CHANNEL_ID, "text": "✅ البوت يعمل الآن بنجاح كـ Web Service."})
    except:
        pass
        
    while True:
        time.sleep(300) # البوت سيعمل في الخلفية بدون توقف

# تشغيل الـ Flask والـ Bot معاً
if __name__ == "__main__":
    Thread(target=bot_logic).start()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
