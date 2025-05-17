from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.inventory import InventoryCreate, InventoryRead
from app.crud.inventory import get_inventory, create_inventory, update_inventory
from app.api.deps import get_db

router = APIRouter()

@router.get("/{product_id}", response_model=InventoryRead)
def check_stock(product_id: int, db: Session = Depends(get_db)):
    inv = get_inventory(db, product_id)
    if not inv:
        raise HTTPException(status_code=404, detail="No stock record found")
    return inv

@router.post("/", response_model=InventoryRead)
def create_stock(payload: InventoryCreate, db: Session = Depends(get_db)):
    return create_inventory(db, payload)