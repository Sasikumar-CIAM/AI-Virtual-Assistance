from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from app.db import Base

class Faq(Base):
    __tablename__ = "faqs"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String(255), nullable=False, unique=True)
    answer = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
