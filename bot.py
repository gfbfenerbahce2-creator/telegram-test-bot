import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("TELEGRAM_BOT_TOKEN bulunamadı!")

print("Bot sistemi başladı.")
print("Token bulundu.")
print("Test başarıyla tamamlandı.")
