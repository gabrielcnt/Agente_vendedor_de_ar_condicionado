from pydantic import BaseModel
from typing import Optional
from app.schemas.product_schemas import ProductCreate

class IngestRequest(BaseModel):
    raw_text: str
    extrated_data: Optional[ProductCreate] = None 