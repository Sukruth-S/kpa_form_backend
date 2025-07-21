from sqlalchemy import Column, Integer, String
from .database import Base

class FormData(Base):
    __tablename__ = "form_data"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=True)
    address = Column(String, nullable=True)
    resume_file = Column(String)  # store filename or path
