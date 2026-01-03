from sqlalchemy import Column, Integer, String, BigInteger
from models.base import Base   # ✅ CORRECT IMPORT


class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    google_drive_id = Column(String, nullable=False)
    size = Column(BigInteger)
    mime_type = Column(String)
    storage_path = Column(String, nullable=False)
