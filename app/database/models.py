from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Investigation(Base):
    __tablename__ = "investigations"

    id = Column(Integer, primary_key=True, index=True)
    topic = Column(String, nullable=False)
    internal_sections = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    filename = Column(String, nullable=False)
    paragraphs = Column(Integer, nullable=False)
    citations_count = Column(Integer, nullable=False)