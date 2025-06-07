from typing import List, Dict
import schemas

# Usamos un diccionario en memoria para simular una base de datos por ahora
fake_db: Dict[int, schemas.Task] = {}
next_id = 1

class TaskService:
    def get_all_tasks(self) -> List[schemas.Task]:
        return list(fake_db.values())

    def create_task(self, task_data: schemas.TaskCreate) -> schemas.Task:
        global next_id
        new_task = schemas.Task(id=next_id, **task_data.dict())
        fake_db[next_id] = new_task
        next_id += 1
        return new_task