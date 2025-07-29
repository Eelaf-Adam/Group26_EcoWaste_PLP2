from models.database import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

class Listing(Base):

    """
    This class contains the specifications
    for the listing table in the database
    """
    
    __tablename__ = "listings"

    id = Column(Integer, primary_key=True)

    provider_id = Column(Integer, ForeignKey("users.id"))
    category = Column(String(50))
    type = Column(String(50))
    quantity = Column(Float)
    location = Column(String(100))

    provider = relationship("User", back_populates="listings")

    purchases = relationship("Purchase", back_populates="listing")