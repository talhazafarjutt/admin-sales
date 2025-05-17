from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import ProductCreate


def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def list_products(db: Session, skip: int = 0, limit: int = 50):
    return db.query(Product).offset(skip).limit(limit).all()

def create_product(db: Session, product_in: ProductCreate):
    obj = Product(**product_in.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj