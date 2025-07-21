from sqlalchemy.orm import Session
from app import models
from app import schemas


# Create new form data entry
def create_form_data(db: Session, form_data: schemas.FormDataCreate):
    db_form = models.FormData(
        full_name=form_data.full_name,
        phone_number=form_data.phone_number,
        email=form_data.email,
        address=form_data.address,
        resume_file=form_data.resume_file  # <-- use the value from schema
    )
    db.add(db_form)
    db.commit()
    db.refresh(db_form)
    return db_form

# Get form data by ID
def get_form_data(db: Session, form_id: int):
    return db.query(models.FormData).filter(models.FormData.id == form_id).first()

def get_all_form_data(db: Session):
    return db.query(models.FormData).all()