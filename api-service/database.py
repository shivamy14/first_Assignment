import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.base import Base
import models.image   # ✅ IMPORTANT: REGISTER Image MODEL

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@db:5432/images_db"
)

engine = create_engine(DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def create_tables():
    Base.metadata.create_all(bind=engine)
