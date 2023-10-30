from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import SessionLocal
from app.models.acupuncture_point import AcupuncturePoint

router = APIRouter()

@router.get("/points/")
def get_points(skip: int = 0, limit: int = 10, db: Session = Depends(SessionLocal)):
    return db.query(AcupuncturePoint).offset(skip).limit(limit).all()
