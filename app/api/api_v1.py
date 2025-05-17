from fastapi import APIRouter
from app.api.routers import products, sales, inventory

api_router = APIRouter()
api_router.include_router(products.router, prefix="/products", tags=["Products"])
api_router.include_router(sales.router, prefix="/sales", tags=["Sales"])
api_router.include_router(inventory.router, prefix="/inventory", tags=["Inventory"])