from pydantic import BaseModel
from typing import Optional


class PatientCreate(BaseModel):
    name: str
    phone: str
    email: Optional[str] = None


class PatientResponse(BaseModel):
    id: int
    name: str
    phone: str
    email: Optional[str] = None

    class Config:
        from_attributes = True