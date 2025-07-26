from models.database import Base
from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy import Float

class Purchase(Base):
    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True)
    buyer_id = Column(Integer, ForeignKey("users.id"))
    listing_id = Column(Integer, ForeignKey("listings.id"))
    quantity = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    buyer = relationship("User", back_populates="purchases")
    listing = relationship("Listing", back_populates="purchases")