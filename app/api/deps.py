from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import SessionLocal

def get_db() -> Session:
    """
    Dependency that yields a SQLAlchemy Session, and
    ensures it’s closed after the request finishes.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()