from pydantic import BaseModel

# 基本的なツボ情報を表すスキーマです。これは他のスキーマのベースとして使用されます。
class AcupuncturePointBase(BaseModel):
    name: str
    description: str

# ツボを作成する際に使用するリクエストボディのスキーマです。
class AcupuncturePointCreate(AcupuncturePointBase):
    pass

# ツボを更新する際に使用するリクエストボディのスキーマです。
class AcupuncturePointUpdate(AcupuncturePointBase):
    pass

# データベースから読み取ったツボ情報をレスポンスとして返す際に使用するスキーマです。
# idフィールドが追加されています。
class AcupuncturePointInDBBase(AcupuncturePointBase):
    id: int

    # Pydanticの設定。ORMモデルとしても使用される場合に必要です。
    class Config:
        orm_mode = True

# レスポンスで使用される完全なツボ情報のスキーマです。
class AcupuncturePoint(AcupuncturePointInDBBase):
    pass

# データベース内のツボ情報を表すスキーマです。
class AcupuncturePointInDB(AcupuncturePointInDBBase):
    pass
