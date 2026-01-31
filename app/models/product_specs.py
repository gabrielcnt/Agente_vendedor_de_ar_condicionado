from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey

from app.core.database import db

class ProductSpecs(db.Base):
    __tablename__ = "product_specs"

    id = Column(Integer, primary_key=True, autoincrement=True)

    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)

    btus = Column(Integer, nullable=False)
    tipo = Column(String)
    tecnologia = Column(String)
    ciclo = Column(String)

    consumo_energia_kwh = Column(Float)
    corrente_amperes = Column(Float)
    potencia_watts = Column(Integer)
    area_recomendada_m2 = Column(Integer)
    voltagem = Column(String, nullable=True)
    tipo_gas = Column(String, nullable=True)
    
    wifi = Column(Boolean, nullable=True)
    smart_home = Column(Boolean, nullable=True)