from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def home():
    return {"status": "ok"}


@app.post("/webhook")
async def webhook(req: Request):
    data = await req.json()
    print(data)
    return {"ok": True}
