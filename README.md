# 🤖 AI Assistent - Telegram Bot

> **Yaratuvchi:** [@MurodbekAzatov](https://t.me/MurodbekAzatov)

OpenAI API asosida ishlayigan Telegram bot. GPT-4, DALL-E 2, Whisper va boshqa imkoniyatlar bilan.

## ⚡ Imkoniyatlari

- 🚀 Tez javob (3-5 soniyada)
- 💬 GPT-4 / GPT-4 Turbo / GPT-4 Vision / GPT-4o qo'llab-quvvatlash
- 🎨 DALL-E 2 bilan rasm yaratish
- 🎤 Ovozli xabarlarni tanib olish (Whisper)
- 📝 12 ta maxsus suhbat rejimi
- 👥 Guruh chatlarida ishlash
- 📊 Streaming mode - javob so'z-so'z ko'rinadi

## 🛠 Bot buyruqlari

| Buyruq | Tavsif |
|--------|--------|
| `/start` | Botni boshlash |
| `/new` | Yangi suhbat boshlash |
| `/mode` | Suhbat rejimini tanlash |
| `/retry` | Oxirgi javobni qayta yaratish |
| `/settings` | Sozlamalar (model tanlash) |
| `/balance` | Balansni ko'rish |
| `/help` | Yordam |

## 🚀 Railway'ga deploy qilish

1. [Railway.app](https://railway.app) ga kiring
2. **MongoDB** pluginini qo'shing
3. Yangi service yarating → GitHub repo'dan deploy qiling
4. **Environment variables** ga qo'shing:
   - `TELEGRAM_TOKEN` - Telegram bot tokeningiz
   - `OPENAI_API_KEY` - OpenAI API kalitingiz
   - `MONGODB_URI` - MongoDB ulanish manzili (Railway o'zi beradi)

## 📁 Loyiha tuzilishi

```
AI-bot/
├── bot/
│   ├── bot.py          # Asosiy bot logikasi
│   ├── config.py       # Konfiguratsiya
│   ├── database.py     # MongoDB bilan ishlash
│   └── openai_utils.py # OpenAI API bilan ishlash
├── config/
│   ├── config.yml      # Asosiy sozlamalar
│   ├── config.env      # Environment o'zgaruvchilari
│   ├── chat_modes.yml  # Suhbat rejimlari
│   └── models.yml      # Model sozlamalari
├── Dockerfile
├── docker-compose.yml
├── railway.json
└── requirements.txt
```

## 📝 Litsenziya

MIT License

---

**Yaratuvchi:** Murodbek Azatov | [@MurodbekAzatov](https://t.me/MurodbekAzatov)
