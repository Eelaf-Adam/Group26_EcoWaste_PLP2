from models.database import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Purchase(Base):
    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True)
    buyer_id = Column(Integer, ForeignKey("users.id"))
    listing_id = Column(Integer, ForeignKey("listings.id"))

    buyer = relationship("User", back_populates="purchases")
    listing = relationship("Listing", back_populates="purchases")