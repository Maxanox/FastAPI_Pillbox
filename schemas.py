from pydantic import BaseModel
from typing import Iterable, Optional, List



class PillboxBase(BaseModel):
    pass

class PillboxCreateIn(PillboxBase):
    pass

class PillboxUpdateIn(PillboxBase):
    owner_id: int

class Pillbox(PillboxBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class PillboxCreateOut(Pillbox):
    pass

class PillboxUpdateOut(Pillbox):
    pass



class PatientBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str

class PatientCreateIn(PatientBase):
    doctor_id: int

class PatientUpdateIn(PatientBase):
    doctor_id: int
 
class Patient(PatientBase):
    id: int
    doctor_id: int
    pillbox: Pillbox = None

    class Config:
        orm_mode = True

class PatientCreateOut(Patient):
    password: str

class PatientUpdateOut(Patient):
    pass



class DoctorBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str

class DoctorCreateIn(DoctorBase):
    pass

class DoctorUpdateIn(DoctorBase):
    pass

class Doctor(DoctorBase):
    id: int
    patients: List[Patient] = []
    
    class Config:
        orm_mode = True

class DoctorCreateOut(Doctor):
    password: str

class DoctorUpdateOut(Doctor):
    pass
    

