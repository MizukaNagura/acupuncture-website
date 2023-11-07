from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str
    # 他のフィールドがあればここに追加
