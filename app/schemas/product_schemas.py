from pydantic import BaseModel
from typing import Optional, Literal



class ProductCreate(BaseModel):
    name: str
    category: Literal["economico", "custo_beneficio", "premium"]

    ideal_for: Optional[str] = None
    selling_points: Optional[str] = None
    objections: Optional[str] = None
    raw_description: Optional[str] = None




class ProductSpecsCreate(BaseModel):
    btus: int
    tipo: Optional[Literal["split", "split_inverter", "janela", "portatil", "cassete", "piso_teto"]] = None
    tecnologia: Optional[str] = None
    ciclo: Literal["frio", "quente", "quente_frio"]

    consumo_energia_kwh: Optional[float] = None
    corrente_amperes: Optional[float] = None
    potencia_watts: Optional[int] = None
    area_recomendada_m2: Optional[int] = None
    voltagem: Literal["110v", "220v", "bivolt"]
    tipo_gas: Optional[str] = None
    
    wifi: Optional[bool] = None
    smart_home: Optional[bool] = None




class ProductUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[Literal["economico", "custo_beneficio", "premium"]] = None

    ideal_for: Optional[str] = None
    selling_points: Optional[str] = None
    objections: Optional[str] = None
    raw_description: Optional[str] = None




class ProductSpecsUpdate(BaseModel):
    btus: Optional[int] = None
    tipo: Optional[tipo_aparelho] = None
    tecnologia: Optional[str] = None
    ciclo: Optional[Literal["frio", "quente", "quente_frio"]] = None

    consumo_energia_kwh: Optional[float] = None
    corrente_amperes: Optional[float] = None
    potencia_watts: Optional[int] = None
    area_recomendada_m2: Optional[int] = None
    voltagem: Optional[Literal["110v", "220v", "bivolt"]] = None
    tipo_gas: Optional[str] = None
    
    wifi: Optional[bool] = None
    smart_home: Optional[bool] = None


