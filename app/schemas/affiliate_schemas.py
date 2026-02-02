from pydantic import BaseModel, HttpUrl

from typing import Optional


class AffiliateLinkBase(BaseModel):
    plataform: str
    affiliate_link: HttpUrl
    
    priority: Optional[int] = 1
    active: Optional[bool] = True




class AffiliateLinkCreate(AffiliateLinkBase):
    product_id: int




class AffiliateLinkUpdate(BaseModel):
    plataform: Optional[str] = None
    affiliate_url: Optional[HttpUrl] = None

    priority: Optional[int] = None
    active: Optional[bool] = None

class AffiliateLinkOut(AffiliateLinkBase):
    id: int
    
    class Config:
        from_attributes = True