from pydantic import BaseModel

class AcupuncturePointBase(BaseModel):
    name: str
    description: str

class AcupuncturePointCreate(AcupuncturePointBase):
    pass

class AcupuncturePointUpdate(AcupuncturePointBase):
    pass

class AcupuncturePointInDBBase(AcupuncturePointBase):
    id: int

    class Config:
        from_attributes = True

class AcupuncturePoint(AcupuncturePointInDBBase):
    pass

class AcupuncturePointInDB(AcupuncturePointInDBBase):
    pass
