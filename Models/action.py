from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Action(Base):
    __tablename__ = 'action'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    action_type = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    rule_id = Column(Integer, ForeignKey('rule.id'), nullable=False)

    def __repr__(self):
        return f"<Action(id={self.id}, action_type={self.action_type}, destination={self.destination}, rule_id={self.rule_id})>"
