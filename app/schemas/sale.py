from pydantic import BaseModel
from datetime import date

class SaleBase(BaseModel):
    product_id: int
    date: date
    quantity: int
    total: float

class SaleCreate(SaleBase):
    pass

class SaleRead(SaleBase):
    id: int

    class Config:
        orm_mode = True