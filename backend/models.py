from sqlalchemy import Column, Integer, String, Date, Numeric, ForeignKey, DateTime
from datetime import datetime
from database import Base

class Owner(Base):
    __tablename__ = "owners"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    mobile = Column(String)
    village = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class Tractor(Base):
    __tablename__ = "tractors"
    id = Column(Integer, primary_key=True)
    tractor_number = Column(String, nullable=False)
    model = Column(String)
    owner_id = Column(Integer, ForeignKey("owners.id"))

class Expense(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True)
    tractor_id = Column(Integer, ForeignKey("tractors.id"))
    date = Column(Date)
    type = Column(String)
    description = Column(String)
    amount = Column(Numeric)

class Income(Base):
    __tablename__ = "income"
    id = Column(Integer, primary_key=True)
    tractor_id = Column(Integer, ForeignKey("tractors.id"))
    date = Column(Date)
    work_type = Column(String)
    quantity = Column(Numeric)
    rate = Column(Numeric)
    total_amount = Column(Numeric)
