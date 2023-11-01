from app.models.acupuncture_point import Base
from database.database import engine

# データベーステーブルを作成する
Base.metadata.create_all(bind=engine)

# このスクリプトを実行することで、定義したモデルに基づいてデータベーステーブルが作成され、
# アプリケーションが使用するデータを格納する準備が整います。
