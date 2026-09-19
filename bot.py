import os
import time

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("TELEGRAM_BOT_TOKEN bulunamadı!")

print("Bot sistemi başladı.")

while True:
    print("Sistem çalışıyor...")
    time.sleep(60)
