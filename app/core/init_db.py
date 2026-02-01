from app.core.database import db

from app.models.affiliate import AffiliateLinks
from app.models.product import Product
from app.models.product_specs import ProductSpecs

def init_db():
    db.Base.metadata.create_all(bind=db.engine)