# init_db.py

from models.database import Base, engine
from models.user import User

# Create all tables defined using Base (including the User table)
#Base.metadata.create_all(bind=engine)

#print("Tables created successfully.")
