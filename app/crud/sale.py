from sqlalchemy.orm import Session
from app.models.sale import Sale
from app.schemas.sale import SaleCreate


def create_sale(db: Session, sale_in: SaleCreate):
    obj = Sale(**sale_in.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def list_sales(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Sale).offset(skip).limit(limit).all()