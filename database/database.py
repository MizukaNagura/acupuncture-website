from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#DATABASE_URL = "postgresql://user:password@db/acupuncture"

DATABASE_URL = "postgresql://user:password@localhost/acupuncture"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
