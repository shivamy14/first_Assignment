from database import engine
from models.base import Base
import models.image

print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("Tables created successfully!")
