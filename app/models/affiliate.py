from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship

from datetime import datetime

from app.core.database import db

class AffiliateLinks(db.Base):
    __tablename__ = "affiliates_links"

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    
    store_name = Column(String, nullable=False)
    affiliate_url = Column(String, nullable=False)
    
    priority = Column(Integer, default=1)
    active = Column(Boolean, default=True)

    product = relationship("Product", backref="affiliate_links")