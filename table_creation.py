from models.database import Base, engine
import models

Base.metadata.create_all(bind=engine)

print("Tables created successfully.")
