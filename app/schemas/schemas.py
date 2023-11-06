from pydantic import BaseModel

class AcupuncturePointCreate(BaseModel):
    name: str
    description: str

class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float = None
