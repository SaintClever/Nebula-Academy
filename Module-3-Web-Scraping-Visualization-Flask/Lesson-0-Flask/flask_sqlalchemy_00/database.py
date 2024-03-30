import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv(".env")

host: str = os.getenv("HOST")
database: str = os.getenv("DATABASE")
user: str = os.getenv("USER")
password: str = os.getenv("PASSWORD")

engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}/{database}")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
