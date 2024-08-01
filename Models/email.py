from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()

class Email(Base):
    __tablename__ = 'email'
    id = Column(Integer, primary_key=True, autoincrement=True)
    from_address = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    date_received = Column(DateTime, default=datetime.datetime.utcnow)
    email_id = Column(String, nullable=False)
    message = Column(String, nullable=False)

    def __repr__(self):
        return f"<Email(subject={self.subject}, from_address={self.from_address})>"

