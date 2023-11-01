from pydantic import BaseModel

class AcupuncturePointCreate(BaseModel):
    name: str
    description: str
