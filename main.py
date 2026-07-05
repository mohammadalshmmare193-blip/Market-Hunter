import os
import time
import requests

# جلب التوكن من النظام
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = "@Market_Hunter_Channel"
MARKET_API_URL = "https://api.getgems.io/v1/asset/marketplace" 

def check_deals():
    try:
        print("جاري فحص السوق الآن من GetGems...")
        response = requests.get(MARKET_API_URL, timeout=10)
        if response.status_code == 200:
            data = response.json()
            print("تم جلب بيانات السوق بنجاح الماركت شغال!")
            # هنا مستقبلاً بنحط شروط الفحص وإرسال التنبيهات
        else:
            print(f"تنبيه: السيرفر رد بكود مختلف: {response.status_code}")
    except Exception as e:
        print(f"خطأ أثناء فحص السوق: {e}")

def send_alert(message):
    if not BOT_TOKEN:
        print("خطأ: لم يتم العثور على BOT_TOKEN!")
        return
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        res = requests.post(url, json=payload)
        print(f"حالة إرسال التنبيه للقناة: {res.status_code}")
    except Exception as e:
        print(f"فشل إرسال الرسالة: {e}")

if __name__ == "__main__":
    print("🚀 بوت صائد الماركت (Market Hunter) بدأ العمل بنجاح واشتعلت المنظومة!")
    # تجربة إرسال رسالة ترحيبية أول ما يشتغل البوت في القناة للتأكد
    send_alert("⚡ تم تشغيل بوت Market Hunter بنجاح على سيرفر Render وهو الآن يراقب السوق!")
    
    while True:
        check_deals()
        print("💤 سأنام لمدة دقيقة الآن ثم أعود للفحص...")
        time.sleep(60)
