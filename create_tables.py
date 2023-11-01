from app.models.acupuncture_point import Base
from database.database import engine

# データベーステーブルを作成する
Base.metadata.create_all(bind=engine)
