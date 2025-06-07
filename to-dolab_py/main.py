# Fichero: main.py

from typing import List
from fastapi import FastAPI, Depends
import schemas
from services import TaskService

app = FastAPI()

# 👇 AÑADE ESTE DECORADOR
@app.post("/tasks/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, service: TaskService = Depends(TaskService)):
    return service.create_task(db, task_data=task) # Asegúrate de pasar la sesión 'db' si la usas

# 👇 AÑADE ESTE DECORADOR
@app.get("/tasks/", response_model=List[schemas.Task])
def read_tasks(service: TaskService = Depends(TaskService)):
    return service.get_all_tasks(db) # Asegúrate de pasar la sesión 'db' si la usas