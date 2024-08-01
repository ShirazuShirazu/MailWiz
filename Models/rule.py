from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Rule(Base):
    __tablename__ = 'rule'
    id = Column(Integer, primary_key=True, autoincrement=True)
    cond_match_type = Column(String, nullable=False)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f"<Rule(name={self.name}, cond_match_type={self.cond_match_type})>"