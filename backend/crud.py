from sqlalchemy.orm import Session
import models, schemas
from typing import Optional, List
from models import ToDo

def create_todo(db: Session, todo: schemas.ToDoRequest):
    db_todo = models.ToDo(name=todo.name, completed=todo.completed)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def read_todos(db: Session, completed: Optional[bool] = None) -> List[ToDo]:
    query = db.query(ToDo)
    if completed is not None:  # Only filter if completed is not None
        query = query.filter(ToDo.completed == completed)
    return query.all()

def read_todo(db: Session, id: int):
    return db.query(models.ToDo).filter(models.ToDo.id == id).first()

def update_todo(db: Session, id: int, todo: schemas.ToDoRequest):
    db_todo = db.query(models.ToDo).filter(models.ToDo.id == id).first()
    if db_todo is None:
        return None
    db.query(models.ToDo).filter(models.ToDo.id == id).update({'name': todo.name, 'completed': todo.completed})
    db.commit()
    db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, id: int):
    db_todo = db.query(models.ToDo).filter(models.ToDo.id == id).first()
    if db_todo is None:
        return None
    db.query(models.ToDo).filter(models.ToDo.id == id).delete()
    db.commit()
    return True