from sqlalchemy import Column, Integer, String
from database import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    folder_url = Column(String, nullable=False)
    status = Column(String, default="started")
    total_images = Column(Integer, default=0)
