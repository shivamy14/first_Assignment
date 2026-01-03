from sqlalchemy import Column, Integer, String, BigInteger, ForeignKey
from database import Base

class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    google_drive_id = Column(String)
    size = Column(BigInteger)
    mime_type = Column(String)
    storage_path = Column(String)
    job_id = Column(Integer, ForeignKey("jobs.id"))
