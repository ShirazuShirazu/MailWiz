from Models.rule import Rule
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Condition(Base):
    __tablename__ = 'condition'
    id = Column(Integer, primary_key=True, autoincrement=True)
    field = Column(String, nullable=False)
    predicate = Column(String, nullable=False)
    value = Column(String, nullable=False)
    rule_id = Column(Integer, ForeignKey('rule.id'), nullable=False)

    # rule = relationship('Rule')

    def __repr__(self):
        return f"<Condition(field={self.field}, predicate={self.predicate}, value={self.value}, rule_id={self.rule_id})>"
