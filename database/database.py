from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#DATABASE_URL = "postgresql://user:password@db/acupuncture"  # 本番用のURL
DATABASE_URL = "postgresql://user:password@localhost/acupuncture"  # ローカル環境用のURL


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
