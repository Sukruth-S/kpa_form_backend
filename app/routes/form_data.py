from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud, database
import shutil
import os
from typing import Optional, List

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/form-data", response_model=schemas.FormDataOut)
async def create_form_data(
    full_name: str = Form(...),
    phone_number: str = Form(...),
    email: Optional[str] = Form(None),
    address: Optional[str] = Form(None),
    resume: Optional[UploadFile] = File(None),
    db: Session = Depends(database.get_db)
):
    resume_filename = None
    if resume:
        resume_filename = f"{phone_number}_{resume.filename}"
        file_path = os.path.join(UPLOAD_DIR, resume_filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(resume.file, buffer)

    form_data = schemas.FormDataCreate(
        full_name=full_name,
        phone_number=phone_number,
        email=email,
        address=address,
        resume_file=resume_filename  # ✅ THIS LINE IS CRUCIAL
    )
    print("Resume filename to save:", resume_filename)  # Add this before creating form_data
    return crud.create_form_data(db=db, form_data=form_data)

@router.get("/form-data", response_model=List[schemas.FormDataOut])
def get_all_form_data(db: Session = Depends(database.get_db)):
    return crud.get_all_form_data(db)

@router.get("/form-data/{id}", response_model=schemas.FormDataOut)
def get_form_data(id: int, db: Session = Depends(database.get_db)):
    form_data = crud.get_form_data(db, id)
    if not form_data:
        raise HTTPException(status_code=404, detail="Form data not found")
    return form_data

@router.post("/test-upload")
async def test_upload(resume: UploadFile = File(...)):
    print("Received file:", resume.filename)
    return {"filename": resume.filename}