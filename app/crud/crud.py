from sqlalchemy.orm import Session
from ..models.acupuncture_point import AcupuncturePoint as AcupuncturePointModel
from ..schemas import AcupuncturePointCreate, AcupuncturePointUpdate

def get_acupuncture_point(db: Session, point_id: int):
    return db.query(AcupuncturePointModel).filter(AcupuncturePointModel.id == point_id).first()

def get_acupuncture_points(db: Session, skip: int = 0, limit: int = 10):
    return db.query(AcupuncturePointModel).offset(skip).limit(limit).all()

def create_acupuncture_point(db: Session, point: AcupuncturePointCreate):
    db_point = AcupuncturePointModel(**point.dict())
    db.add(db_point)
    db.commit()
    db.refresh(db_point)
    return db_point

def update_acupuncture_point(db: Session, point_id: int, point: AcupuncturePointUpdate):
    db_point = db.query(AcupuncturePointModel).filter(AcupuncturePointModel.id == point_id).first()
    if db_point:
        update_data = point.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_point, key, value)
        db.commit()
        db.refresh(db_point)
    return db_point

def delete_acupuncture_point(db: Session, point_id: int):
    db_point = db.query(AcupuncturePointModel).filter(AcupuncturePointModel.id == point_id).first()
    if db_point:
        db.delete(db_point)
        db.commit()
    return db_point
