from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ..dependencies import get_db
from app.models.schemas import AcupuncturePointCreate, AcupuncturePointUpdate, AcupuncturePoint
from app.crud import get_acupuncture_points, create_acupuncture_point, get_acupuncture_point, update_acupuncture_point, delete_acupuncture_point

router = APIRouter()

@router.get("/points/", response_model=List[AcupuncturePoint])
def read_points(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    points = get_acupuncture_points(db, skip=skip, limit=limit)
    return points

@router.get("/points/{point_id}", response_model=AcupuncturePoint)
def read_point(point_id: int, db: Session = Depends(get_db)):
    db_point = get_acupuncture_point(db, point_id=point_id)
    if db_point is None:
        raise HTTPException(status_code=404, detail="Acupuncture point not found")
    return db_point

@router.post("/points/", response_model=AcupuncturePoint, status_code=status.HTTP_201_CREATED)
def create_point(point: AcupuncturePointCreate, db: Session = Depends(get_db)):
    return create_acupuncture_point(db=db, point=point)

@router.put("/points/{point_id}", response_model=AcupuncturePoint)
def update_point(point_id: int, point: AcupuncturePointUpdate, db: Session = Depends(get_db)):
    db_point = update_acupuncture_point(db, point_id=point_id, point=point)
    if db_point is None:
        raise HTTPException(status_code=404, detail="Acupuncture point not found")
    return db_point

@router.delete("/points/{point_id}", response_model=AcupuncturePoint)
def delete_point(point_id: int, db: Session = Depends(get_db)):
    db_point = delete_acupuncture_point(db, point_id=point_id)
    if db_point is None:
        raise HTTPException(status_code=404, detail="Acupuncture point not found")
