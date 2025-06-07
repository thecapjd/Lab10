from sqlalchemy.orm import Session
import models, schemas

class TaskService:
    def get_all_tasks(self, db: Session):
        return db.query(models.Task).all()

    def create_task(self, db: Session, task_data: schemas.TaskCreate):
        db_task = models.Task(**task_data.dict())
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        return db_task