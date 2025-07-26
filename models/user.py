from sqlalchemy import Column, Integer, String
from models.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(128), nullable=False)
    role = Column(String(20), nullable=False)

    company_name = Column(String(100), nullable=True)
    company_domain = Column(String(100), nullable=True)

    location = Column(String(100), nullable=True)
    name = Column(String(100), nullable=True)

    listings = relationship("Listing", back_populates="provider")
    purchases = relationship("Purchase", back_populates="buyer")

    def __repr__(self):
        return f"<User(email='{self.email}', role='{self.role}')>"

    def home(self):
        print(f"Welcome to the {self.role.capitalize()} Home Page!")