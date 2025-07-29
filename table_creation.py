#File run once to create the respective tables in the database after reset

from models.database import Base, engine
import models

Base.metadata.create_all(bind=engine)

print("Tables created successfully.")