from sqlalchemy.orm import Session
from database import SessionLocal

# 依存性
# get_db 依存性関数は、APIエンドポイントの各リクエストに対して新しいセッションを生成し、
# リクエスト処理が完了した後にセッションを閉じる役割を果たします。
# これにより、リクエストごとに独立したデータベースのコンテキストが確保され、
# データベース操作が安全に行えるようになります。
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()