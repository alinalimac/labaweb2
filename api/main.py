from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, Base, get_db

# Создаем таблицы
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/", response_model=list[schemas.StudentOut])
def read_students(page: int = 1, size: int = 10, db: Session = Depends(get_db)):
    skip = (page - 1) * size
    students = crud.get_students(db, skip=skip, limit=size)
    return students
