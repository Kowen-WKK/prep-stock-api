from fastapi import FastAPI
from routes import router as items_router
from routes_usage import router as usage_router
from routes_suggestions import router as suggestions_router

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok", "service": "prep-stock-api"}

app.include_router(items_router)
app.include_router(usage_router)
app.include_router(suggestions_router)