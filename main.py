from fastapi import FastAPI, Request
import requests
import os

BOT_TOKEN = "8650861652:AAE0Q4-ONNBPj8Pv9YxAp6abJZN0Qhk1in0"

app = FastAPI()


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

        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": f"Вы написали: {text}"
            }
        )

    return {"ok": True}
