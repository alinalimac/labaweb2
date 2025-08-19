from sqlalchemy.orm import Session
from .models import Student
from .schemas import StudentCreate, StudentUpdate

def get_students(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Student).offset(skip).limit(limit).all()

# def create_student(db: Session, student: StudentCreate):
#     db_student = Student(**student.dict())
#     db.add(db_student)
#     db.commit()
#     db.refresh(db_student)
#     return db_student

# def update_student(db: Session, student_id: int, updates: StudentUpdate):
#     db_student = db.query(Student).filter(Student.id == student_id).first()
#     if not db_student:
#         return None
#     for key, value in updates.dict(exclude_unset=True).items():
#         setattr(db_student, key, value)
#     db.commit()
#     db.refresh(db_student)
#     return db_student

# def delete_student(db: Session, student_id: int):
#     db_student = db.query(Student).filter(Student.id == student_id).first()
#     if not db_student:
#         return None
#     db.delete(db_student)
#     db.commit()
#     return db_student
