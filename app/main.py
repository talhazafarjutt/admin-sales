from fastapi import FastAPI
from app.api.api_v1 import api_router
from app.db.init_db import init_db, create_demo_data
from app.core.config import settings

app = FastAPI(
    title="E‑Commerce Admin API",
    description="APIs for dashboards: sales, revenue, inventory & products.",
    version="1.0.0",
)

@app.on_event("startup")
def on_startup():
    # initialize database and seed sample data
    init_db()
    create_demo_data()

app.include_router(api_router, prefix="/api/v1")