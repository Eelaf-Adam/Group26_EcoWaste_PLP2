#File run once to clear the existing content in the databases

from models.database import Base, engine
from models.user import User
from models.listings import Listing
from models.purchases import Purchase

# Drop all tables
Base.metadata.drop_all(bind=engine)
print("All tables dropped.")

# Recreates all tables
Base.metadata.create_all(bind=engine)
print("All tables created successfully.")
