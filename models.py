from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.elements import Null

from .database import Base

class Doctor(Base):
    __tablename__ = 'Doctors'

    id = Column(Integer, primary_key=True, unique=True, index=True, nullable=False)

    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True)
    phone_number = Column(String, unique=True, index=True)

    hashed_password = Column(String)
    
    patients = relationship('Patient', back_populates='doctor')

class Patient(Base):
    __tablename__ = 'Patients'

    id = Column(Integer, primary_key=True, unique=True, index=True, nullable=False)

    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True)
    phone_number = Column(String, unique=True, index=True)

    hashed_password = Column(String)

    doctor_id = Column(Integer, ForeignKey("Doctors.id"))
    doctor = relationship('Doctor', back_populates='patients')
    pillbox = relationship('Pillbox', back_populates='owner')
    
class Pillbox(Base):
    __tablename__ = 'Pillboxes'

    id = Column(Integer, primary_key=True, unique=True, index=True, nullable=False)

    owner_id = Column(Integer, ForeignKey("Patients.id"), default=0)
    owner = relationship('Patient', back_populates='pillbox')
