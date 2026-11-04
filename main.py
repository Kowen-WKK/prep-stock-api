from fastapi import FastAPI
from routes import router as items_router
from routes_usage import router as usage_router
import models

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok", "service": "prep-stock-api"}

app.include_router(items_router)
app.include_router(usage_router)