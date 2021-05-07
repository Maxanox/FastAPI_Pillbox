from sqlalchemy.orm import session
from fastapi import HTTPException, status
from sqlalchemy.sql.expression import delete

from . import models, schemas, password_gen as pg, hashing

# Doctors
def doctors_create(doctor: schemas.DoctorCreateIn, db: session) -> dict:
    password = pg.generate()

    doctor_model = models.Doctor(
        first_name = doctor.first_name,
        last_name = doctor.last_name,
        email = doctor.email,
        phone_number = doctor.phone_number,
        hashed_password = hashing.get_password_hash(password),
    )

    db.add(doctor_model)
    db.commit()
    db.refresh(doctor_model)

    doctor_model.__dict__['password'] = password
    
    return doctor_model



def doctors_read_all(db: session) -> list[dict]:
    db_doctors = db.query(models.Doctor).all()

    return db_doctors



def doctors_read_by_id(id: int, db: session) -> dict:
    db_doctor = db.query(models.Doctor).filter(models.Doctor.id == id).first()

    if not db_doctor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"doctor with the id '{id}' not found")

    return db_doctor



def doctors_delete_by_id(id: int, db: session):
    db_doctor = db.query(models.Doctor).filter(models.Doctor.id == id).first()

    if not db_doctor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"doctor with the id '{id}' not found")

    db.delete(db_doctor)
    db.commit()



def doctors_updated_by_id(id: int, doctor: schemas.DoctorBase, db: session) -> dict:
    db_doctor = db.query(models.Doctor).filter(models.Doctor.id==id).first()

    if not db_doctor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"doctor with the id '{id}' not found")

    db_doctor.first_name = doctor.first_name
    db_doctor.last_name = doctor.last_name
    db_doctor.email = doctor.email
    db_doctor.phone_number = doctor.phone_number

    db.commit()
    db.refresh(db_doctor)

    return db_doctor


# Patients
def patients_create(patient: schemas.PatientCreateIn, db: session) -> dict:
    password = pg.generate()

    patient_model = models.Patient(
        first_name = patient.first_name,
        last_name = patient.last_name,
        email = patient.email,
        phone_number = patient.phone_number,
        hashed_password = hashing.get_password_hash(password),
        doctor_id = patient.doctor_id
    )

    db.add(patient_model)
    db.commit()
    db.refresh(patient_model)

    patient_model.__dict__['password'] = password

    return patient_model



def patients_read_all(db: session) -> list[dict]:
    db_patients = db.query(models.Patient).all()

    return db_patients



def patients_read_by_id(id: int, db: session) -> dict:
    db_patient = db.query(models.Patient).filter(models.Patient.id == id).first()

    if not db_patient:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"patient with the id '{id}' not found")

    return db_patient



def patients_delete_by_id(id: int, db: session) -> None:
    db_patient = db.query(models.Patient).filter(models.Patient.id == id).first()

    if not db_patient:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"patient with the id '{id}' not found")

    db.delete(db_patient)
    db.commit()



def patients_updated_by_id(id: int, patient: schemas.PatientBase, db: session) -> dict:
    db_patient = db.query(models.Patient).filter(models.Patient.id==id).first()

    if not db_patient:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"patient with the id '{id}' not found")

    db_patient.first_name = patient.first_name
    db_patient.last_name = patient.last_name
    db_patient.email = patient.email
    db_patient.phone_number = patient.phone_number
    db_patient.doctor_id = patient.doctor_id

    db.commit()
    db.refresh(db_patient)

    return db_patient



# Pillboxes
def pillboxes_create(how_many: int, db: session) -> list[dict]:

    for _ in range(how_many):
        pillbox_model = models.Pillbox()

        db.add(pillbox_model)
        db.commit()
        db.refresh(pillbox_model)
    
        yield pillbox_model



def pillboxes_read_all(db: session) -> list[dict]:
    db_pillboxes = db.query(models.Pillbox).all()

    return db_pillboxes



def pillboxes_read_by_id(id: int, db: session) -> dict:
    db_pillbox = db.query(models.Pillbox).filter(models.Pillbox.id == id).first()

    if not db_pillbox:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"pillbox with the id '{id}' not found")

    return db_pillbox



def pillboxes_delete_by_id(id: int, db: session) -> None:
    db_pillbox = db.query(models.Pillbox).filter(models.Pillbox.id==id).first()

    if not db_pillbox:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"pillbox with the id '{id}' not found")

    db.delete(db_pillbox)
    db.commit()



def pillboxes_updated_by_id(id: int, pillbox: schemas.PillboxBase, db: session) -> dict:
    db_pillbox = db.query(models.Pillbox).filter(models.Pillbox.id==id).first()

    if not db_pillbox:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"pillbox with the id '{id}' not found")

    db_owner = db.query(models.Patient).filter(models.Patient.id==pillbox.owner_id).first()

    if not db_owner:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"patient with the id '{id}' not found")

    db_pillbox.owner_id = pillbox.owner_id

    db.commit()
    db.refresh(db_pillbox)

    return db_pillbox