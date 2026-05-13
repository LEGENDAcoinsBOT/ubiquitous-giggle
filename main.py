from fastapi import FastAPI, Request
import requests

BOT_TOKEN = "ТВОЙ_НОВЫЙ_ТОКЕН"

app = FastAPI()


def send_message(chat_id, text, keyboard=None):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": text,
    }

    if keyboard:
        payload["reply_markup"] = keyboard

    requests.post(url, json=payload)


@app.get("/")
async def home():
    return {"status": "ok"}


@app.post("/webhook")
async def webhook(req: Request):
    data = await req.json()

    print(data)

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        keyboard = {
            "inline_keyboard": [
                [
                    {"text": "💰 TikTok Coins", "callback_data": "coins"}
                ],
                [
                    {"text": "⭐ Telegram Stars", "callback_data": "stars"}
                ],
                [
                    {"text": "👑 Telegram Premium", "callback_data": "premium"}
                ]
            ]
        }

        if text == "/start":
            send_message(
                chat_id,
                "Добро пожаловать в магазин 👋",
                keyboard
            )

    if "callback_query" in data:
        query = data["callback_query"]

        chat_id = query["message"]["chat"]["id"]
        data_btn = query["data"]

        if data_btn == "coins":
            send_message(chat_id, "Введите username TikTok")

        elif data_btn == "stars":
            send_message(chat_id, "Введите Telegram username")

        elif data_btn == "premium":
            send_message(chat_id, "Выберите срок Premium")

    return {"ok": True}
