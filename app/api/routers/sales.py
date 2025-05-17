from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.sale import SaleCreate, SaleRead
from app.crud.sale import create_sale, list_sales
from app.api.deps import get_db

router = APIRouter()

@router.post("/", response_model=SaleRead)
def record_sale(payload: SaleCreate, db: Session = Depends(get_db)):
    return create_sale(db, payload)

@router.get("/", response_model=list[SaleRead])
def fetch_sales(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return list_sales(db, skip, limit)