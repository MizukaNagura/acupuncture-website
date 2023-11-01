from sqlalchemy.orm import Session
from database import SessionLocal

# 依存性
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
