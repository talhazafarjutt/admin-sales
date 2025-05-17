from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    category: str
    price: float

class ProductCreate(ProductBase):
    pass

class ProductRead(ProductBase):
    id: int

    class Config:
        orm_mode = True