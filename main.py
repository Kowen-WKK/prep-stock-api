from fastapi import FastAPI
from routes import router
import models

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok", "service": "prep-stock-api"}

app.include_router(router)