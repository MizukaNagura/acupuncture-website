from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# データベースのURLを指定します。これは環境変数から取得するか、直接文字列として記述します。
# 例えば、PostgreSQLを使用する場合は以下のようなURLになります:
# postgresql://<ユーザー名>:<パスワード>@<ホスト>/<データベース名>
DATABASE_URL = "postgresql://user:password@localhost/acupuncture"

# SQLAlchemyのエンジンを作成します。これは、データベースとの接続プールや、
# SQLの実行を管理するためのものです。
engine = create_engine(DATABASE_URL)

# sessionmakerは、データベースセッションを作成するためのファクトリです。
# `autocommit=False`は、自動コミットを無効にするために設定します。
# これにより、トランザクションの明示的なコミットまたはロールバックが必要になります。
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)