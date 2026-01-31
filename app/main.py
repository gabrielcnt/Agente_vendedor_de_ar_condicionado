from fastapi import FastAPI
from dotenv import load_dotenv

from app.core.database import db
from app.models.affiliate import AffiliateLinks
from app.models.product import Product
from app.models.product_specs import ProductSpecs


load_dotenv()

from app.services.ai_service import test_ai

db.Base.metadata.create_all(bind=db.engine)

app = FastAPI()

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