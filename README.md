# Bothost Telegram Bot

## 1. Распакуй архив

НЕ загружай ZIP на GitHub.

Нужно распаковать архив и загрузить файлы.

---

## 2. Создай GitHub Repository

https://github.com/new

Repository должен быть PUBLIC.

---

## 3. Загрузи файлы

Нужно загрузить:

- main.py
- requirements.txt
- README.md

НЕ ZIP архив.

---

## 4. Bothost настройки

### Build Command

pip install -r requirements.txt

### Start Command

uvicorn main:app --host 0.0.0.0 --port 8000

### Branch

main

---

## 5. ENV Variables

BOT_TOKEN=твой_токен

WEBHOOK_URL=https://your-project.bothost.ru/webhook

---

## 6. Deploy

Нажми Deploy.

---

## 7. Проверка

Открой:

https://YOUR_PROJECT.bothost.ru

Должно показать:

{"status":"ok"}

---

## 8. Webhook

https://api.telegram.org/botTOKEN/setWebhook?url=https://YOUR_PROJECT.bothost.ru/webhook

---

## 9. Проверка webhook

https://api.telegram.org/botTOKEN/getWebhookInfo
