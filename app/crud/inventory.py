from sqlalchemy.orm import Session
from app.models.inventory import Inventory
from app.schemas.inventory import InventoryCreate


def get_inventory(db: Session, product_id: int):
    return db.query(Inventory).filter(Inventory.product_id == product_id).first()


def update_inventory(db: Session, inventory_obj: Inventory):
    db.add(inventory_obj)
    db.commit()
    db.refresh(inventory_obj)
    return inventory_obj


def create_inventory(db: Session, inv_in: InventoryCreate):
    obj = Inventory(**inv_in.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj