from pydantic import BaseModel, EmailStr
from typing import Optional
from fastapi import File, UploadFile

# Schema for creating form data (POST)
class FormDataCreate(BaseModel):
    full_name: str
    phone_number: str
    email: Optional[EmailStr] = None
    address: Optional[str] = None
    resume_file: Optional[str] = None  # <-- Add this line

# Schema for reading/returning form data (GET)
class FormDataOut(BaseModel):
    id: int
    full_name: str
    phone_number: str
    email: Optional[str]
    address: Optional[str]
    resume_file: Optional[str]

    class Config:
        orm_mode = True
