import requests
import time

BOT_TOKEN = "8950426447:AAGIfbiL6qa5fkGdT0Qgb1zH6kbwSQ5nlmE"
CHANNEL_ID = -1004347664335

def main():
    # رسالة التأكيد
    message = "✅ البوت يعمل الآن بنظام المراقبة بانتظار الأوامر."
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHANNEL_ID, "text": message})
    
    # حلقة تكرار لا تنتهي عشان ما يطفي البوت
    while True:
        time.sleep(60) # البوت رح ينام 60 ثانية ويرجع يعيد، هيك بضل شغال

if __name__ == "__main__":
    main()
