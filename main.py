from fastapi import FastAPI, Request
import requests

BOT_TOKEN = "8650861652:AAE0Q4-ONNBPj8Pv9YxAp6abJZN0Qhk1in0"
CRYPTO_TOKEN = "581231:AAvJOWsgCmW0tFzPi1q0OnTLzf4ty7SHQuq"

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


def create_invoice(amount=1):
    url = "https://pay.crypt.bot/api/createInvoice"

    headers = {
        "Crypto-Pay-API-Token": CRYPTO_TOKEN
    }

    payload = {
        "asset": "USDT",
        "amount": amount,
        "description": "Оплата заказа"
    }

    r = requests.post(url, json=payload, headers=headers)

    print(r.text)

    return r.json()


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

        invoice = create_invoice(1)

        if invoice.get("ok"):

            pay_url = invoice["result"]["pay_url"]

            keyboard = {
                "inline_keyboard": [
                    [
                        {
                            "text": "💳 Оплатить",
                            "url": pay_url
                        }
                    ]
                ]
            }

            send_message(
                chat_id,
                "Для продолжения оплатите счёт:",
                keyboard
            )

    return {"ok": True}

@router.message(F.successful_payment)
async def successful_payment(message: Message):
    await message.answer("✅ Оплата успешна!")
