# create_tables.py
# app.models.acupuncture_point の代わりに
from database.database import engine
from app.models.acupuncture_point import Base

# データベーステーブルを作成する
Base.metadata.create_all(bind=engine)
