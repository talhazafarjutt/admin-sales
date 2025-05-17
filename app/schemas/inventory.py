from pydantic import BaseModel

class InventoryBase(BaseModel):
    product_id: int
    available: int

class InventoryCreate(InventoryBase):
    pass

class InventoryRead(InventoryBase):
    id: int

    class Config:
        orm_mode = True