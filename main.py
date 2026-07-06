import requests
import time

BOT_TOKEN = "8950426447:AAGIfbiL6qa5fkGdT0Qgb1zH6kbwSQ5nlmE"
CHANNEL_ID = -1004347664335

def check_market():
    # هنا سنضع رابط المتجر لاحقاً، حالياً سنقوم بتجربة إرسال رسالة مفصلة
    message = (
        "🔍 **جاري البحث في السوق...**\n\n"
        "💎 **اسم القطعة:** (تجريبي - جاري التطوير)\n"
        "💰 **السعر:** 50 TON\n"
        "📊 **النسبة:** Rare\n"
        "📦 **العدد:** 1/1000\n\n"
        "تم فحص السوق بنجاح! ننتظر ربط الموقع الفعلي."
    )
    
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHANNEL_ID, "text": message, "parse_mode": "Markdown"}
    requests.post(url, json=payload)

if __name__ == "__main__":
    check_market()
