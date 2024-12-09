from pydantic import BaseModel

class StudentBase(BaseModel):
    first_name: str
    last_name: str
    middle_name: str
    course: int
    group: str
    faculty: str

class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    middle_name: str | None = None
    course: int | None = None
    group: str | None = None
    faculty: str | None = None

class StudentOut(StudentBase):
    id: int

    class Config:
        orm_mode = True
