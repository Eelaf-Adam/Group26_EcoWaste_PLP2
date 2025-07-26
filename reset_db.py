# reset_db.py

from models.database import Base, engine
from models.user import User
from models.listings import Listing
from models.purchases import Purchase

# Drop all tables (Warning: this deletes all existing data)
Base.metadata.drop_all(bind=engine)
print("All tables dropped.")

# Recreate all tables from your model definitions
Base.metadata.create_all(bind=engine)
print("All tables created successfully.")
