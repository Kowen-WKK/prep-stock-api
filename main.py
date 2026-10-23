from fastapi import FastAPI
from routes import router
from database import Base, engine
import models

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok", "service": "prep-stock-api"}

app.include_router(router)