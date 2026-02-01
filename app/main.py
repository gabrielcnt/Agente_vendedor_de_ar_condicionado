from fastapi import FastAPI
from dotenv import load_dotenv

from contextlib import asynccontextmanager

from app.core.database import db
from app.core.init_db import init_db



load_dotenv()

from app.services.ai_service import test_ai


@asynccontextmanager
async def lifespan(app: FastAPI):
    #startup
    init_db()
    yield
    # shutdown


app = FastAPI(lifespan=lifespan)

@app.get("/test-ia")
def ai_test():
    result = test_ai()
    return {"response": result}

@app.get("/db-test")
def db_test():
    conn = db.engine.connect()
    conn.close()
    return {
        "database_url": db.database_url,
        "status": "connected"
    }

@app.get("/health")
def health():
    return {"status": "ok"}