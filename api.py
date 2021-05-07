from fastapi import FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import session
from typing import Optional, List
from fastapi.encoders import jsonable_encoder
from .database import SessionLocal, engine
from . import crud, schemas, models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()  

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Root
@app.get('/', tags=['Root'],
    status_code=status.HTTP_200_OK
)
async def read_root() -> str:
    response = "Welcome on my API"
    return response


# Doctors
@app.post('/doctors/create', tags=['Doctors'], summary="Creation of a doctor in the database",
    status_code = status.HTTP_201_CREATED, 
    response_model = schemas.DoctorCreateOut,
    response_model_exclude = {'patients'},
    response_description = "Creation of a doctor in the database, successful." 
)
async def doctors_create(request: schemas.DoctorCreateIn, db: session = Depends(get_db)) -> dict:
    return crud.doctors_create(request, db)
    


@app.get('/doctors/read/all', tags=['Doctors'], summary="Retrieving all doctors in the database",
    status_code = status.HTTP_200_OK, 
    response_model = List[schemas.Doctor],
    response_description = "Retrieving all doctors in the database, successful." 
)
async def doctors_read_all(db: session = Depends(get_db)) -> list:
    return crud.doctors_read_all(db)



@app.get('/doctors/read/{id}', tags=['Doctors'], summary="Retrieving doctor by his id in the database",
    status_code = status.HTTP_200_OK,
    response_model = schemas.Doctor,
    response_model_exclude = {'id'}, 
    response_description = "Retrieving doctor by his id in the database, successful." 
)
async def doctors_read_by_id(id: int, db: session = Depends(get_db)) -> dict:
    return crud.doctors_read_by_id(id, db)



@app.delete('/doctors/delete/{id}', tags=['Doctors'], summary="Removal of the doctor by his id in the database",
    status_code = status.HTTP_204_NO_CONTENT,
    response_description = "Removal of the doctor by his id in the database, successful." 
)
async def doctors_delete_by_id(id: int, db: session = Depends(get_db)) -> dict:
    return crud.doctors_delete_by_id(id, db)
    


@app.put('/doctors/updated/{id}', tags=['Doctors'], summary="Update of the doctor by his id in the database",
    status_code = status.HTTP_202_ACCEPTED,
    response_model = schemas.DoctorUpdateOut,
    response_description = "Update of the doctor by his id in the database, successful" 
)
async def doctors_updated_by_id(id: int, request: schemas.DoctorUpdateIn, db: session = Depends(get_db)) -> dict:
    return crud.doctors_updated_by_id(id, request, db)


# Patients
@app.post('/patients/create', tags=['Patients'], summary="Creation of a patient in the database",
    status_code = status.HTTP_201_CREATED, 
    response_model = schemas.PatientCreateOut,
    response_model_exclude = {'pillbox'},
    response_description = "Creation of a patient in the database, successful." 
)
async def patients_create(request: schemas.PatientCreateIn, db: session = Depends(get_db)) -> dict:
    return crud.patients_create(request, db)



@app.get('/patients/read/all', tags=['Patients'], summary="Retrieving all patients in the database",
    status_code = status.HTTP_200_OK, 
    response_model = List[schemas.Patient],
    response_description = "Retrieving all patients in the database, successful." 
)
async def patients_read_all(db: session = Depends(get_db)) -> list:
    return crud.patients_read_all(db)



@app.get('/patients/read/{id}', tags=['Patients'], summary="Retrieving patient by his id in the database",
    status_code = status.HTTP_200_OK,
    response_model = schemas.Patient,
    response_model_exclude = {'id'}, 
    response_description = "Retrieving patient by his id in the database, successful." 
)
async def patients_read_by_id(id: int, db: session = Depends(get_db)) -> dict:
    return crud.patients_read_by_id(id, db)



@app.delete('/patients/delete/{id}', tags=['Patients'], summary="Removal of the patient by his id in the database",
    status_code = status.HTTP_204_NO_CONTENT,
    response_description = "Removal of the patient by his id in the database, successful." 
)
async def patients_delete_by_id(id: int, db: session = Depends(get_db)) -> dict:
    return crud.patients_delete_by_id(id, db)
    


@app.put('/patients/updated/{id}', tags=['Patients'], summary="Update of the patient by his id in the database",
    status_code = status.HTTP_202_ACCEPTED,
    response_model = schemas.PatientUpdateOut,
    response_model_exclude = {'id'},
    response_description = "Update of the patient by his id in the database, successful" 
)
async def patients_updated_by_id(id: int, request: schemas.PatientUpdateIn, db: session = Depends(get_db)) -> dict:
    return crud.patients_updated_by_id(id, request, db)



# Pillbox 
@app.post('/pillboxes/create/{how_many}', tags=['Pillboxes'], summary="Creation of one or many pillboxes in the database",
    status_code = status.HTTP_201_CREATED, 
    response_model = List[schemas.Pillbox],
    response_description = "Creation of one or many pillboxes in the database, successful" 
)
async def pillboxes_create(how_many: int, db: session = Depends(get_db)) -> list[dict]:
    return crud.pillboxes_create(how_many, db)



@app.get('/pillboxes/read/all', tags=['Pillboxes'], summary="Retrieving all pillboxes in the database",
    status_code = status.HTTP_200_OK, 
    response_model = List[schemas.Pillbox],
    response_description = "Retrieving all pillboxes in the database, successful." 
)
async def pillboxes_read_all(db: session = Depends(get_db)) -> list:
    return crud.pillboxes_read_all(db)



@app.get('/pillboxes/read/{id}', tags=['Pillboxes'], summary="Retrieving pillbox by his id in the database",
    status_code = status.HTTP_200_OK,
    response_model = schemas.Pillbox,
    response_model_exclude = {'id'}, 
    response_description = "Retrieving pillbox by his id in the database, successful." 
)
async def pillboxes_read_by_id(id: int, db: session = Depends(get_db)) -> dict:
    return crud.pillboxes_read_by_id(id, db)



@app.delete('/pillboxes/delete/{id}', tags=['Pillboxes'], summary="Removal of the pillbox by his id in the database",
    status_code = status.HTTP_204_NO_CONTENT,
    response_description = "Removal of the pillbox by his id in the database, successful." 
)
async def pillboxes_delete_by_id(id: int, db: session = Depends(get_db)) -> dict:
    return crud.pillboxes_delete_by_id(id, db)
    


@app.put('/pillboxes/updated/{id}', tags=['Pillboxes'], summary="Update of the pillbox by his id in the database",
    status_code = status.HTTP_202_ACCEPTED,
    response_model = schemas.PillboxUpdateOut,
    response_model_exclude = {'id'},
    response_description = "Update of the pillbox by his id in the database, successful" 
)
async def pillboxes_updated_by_id(id: int, request: schemas.PillboxUpdateIn, db: session = Depends(get_db)) -> dict:
    return crud.pillboxes_updated_by_id(id, request, db)