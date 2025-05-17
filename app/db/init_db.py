from app.db.base import Base
from app.db.session import engine, SessionLocal
from sqlalchemy.exc import OperationalError
from app.models.product import Product
# import app.models.sale, app.models.inventory

def init_db():
    Base.metadata.create_all(bind=engine)


def create_demo_data():
    db = SessionLocal()
    try:
        if db.query(Product).count() == 0:
            sample = [
                Product(name="Wireless Mouse", category="Accessories", price=29.99),
                Product(name="Mechanical Keyboard", category="Accessories", price=79.50),
            ]
            db.add_all(sample)
            db.commit()
    except OperationalError:
        pass
    finally:
        db.close()