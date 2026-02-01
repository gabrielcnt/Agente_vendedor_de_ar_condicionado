from sqlalchemy import Column, Integer, String, Boolean,Float, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship

from datetime import datetime

from app.core.database import db

class Product(db.Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    category = Column(String, nullable=False)
    ideal_for = Column(Text, nullable=False)
    selling_points = Column(Text, nullable=False)
    objections = Column(Text, nullable=False)
    raw_descrption = Column(Text, nullable=False)

    active = Column(Boolean, default=True)
    specs = relationship("ProductsSpecs", backref="product", uselist=False)    
    need_review = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now())
