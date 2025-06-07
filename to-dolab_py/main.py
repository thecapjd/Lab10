from typing import List
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models, schemas, services
from database import engine, get_db

# Crea la tabla en la BD automáticamente
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Todo Lab API", description="API para gestionar tareas")

@app.post("/tasks/", response_model=schemas.Task)
def create_task(
    task: schemas.TaskCreate, 
    db: Session = Depends(get_db)
):
    service = services.TaskService()
    return service.create_task(db=db, task_data=task)

@app.get("/tasks/", response_model=List[schemas.Task])
def read_tasks(db: Session = Depends(get_db)):
    service = services.TaskService()
    return service.get_all_tasks(db=db)

@app.get("/")
def root():
    return {"message": "Todo Lab API está funcionando!"}