from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.product import ProductCreate, ProductRead
from app.crud.product import create_product, get_product, list_products
from app.api.deps import get_db

router = APIRouter()

@router.post("/", response_model=ProductRead)
def add_product(payload: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, payload)

@router.get("/", response_model=list[ProductRead])
def read_products(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    return list_products(db, skip, limit)

@router.get("/{product_id}", response_model=ProductRead)
def read_single_product(product_id: int, db: Session = Depends(get_db)):
    prod = get_product(db, product_id)
    if not prod:
        raise HTTPException(status_code=404, detail="Product not found")
    return prod