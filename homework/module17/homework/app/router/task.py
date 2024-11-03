from fastapi import APIRouter, Depends, status, HTTPException
# Сессия БД
from sqlalchemy.orm import Session
# Функция подключения к БД
from app.backend.db_depends import get_db
# Аннотации, Модели БД и Pydantic.
from typing import Annotated, List
from app.models import Task, User
from app.schemas import UpdateTask, CreateTask
# Функции работы с записями.
from sqlalchemy import insert, select, update, delete
# Функция создания slug-строки
from slugify import slugify



router = APIRouter(prefix="/task", tags=["task"])

@router.get("/")
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    query = select(Task)
    tasks = db.execute(query).scalars().all()
    return tasks

@router.get("/{tasks_id}")
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    query = select(Task).where(Task.id == task_id)
    task = db.execute(query).scalar_one_or_none()

    if task is None:
        raise HTTPException(status_code=404, detail="Task was not found")

    return task

@router.post("/create")
async def create_task(db: Annotated[Session, Depends(get_db)], task: CreateTask, user_id: int):
    user_query = select(User).where(User.id == user_id)
    user = db.execute(user_query).scalar_one_or_none()

    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    task_data = task.dict()
    task_data['user_id'] = user_id

    db.execute(insert(Task).values(**task_data))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


@router.put("/update/{task_id}")
async def update_task(db: Annotated[Session, Depends(get_db)], task_id: int, task: UpdateTask):
    query = select(Task).where(Task.id == task_id)
    existing_task = db.execute(query).scalar_one_or_none()

    if existing_task is None:
        raise HTTPException(status_code=404, detail="Task was not found")

    # Обновление значений задачи
    for key, value in task.dict(exclude_unset=True).items():
        setattr(existing_task, key, value)

    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'Task update is successful!'}

@router.delete("/delete/{task_id}")
async def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int):
    query = select(Task).where(Task.id == task_id)
    existing_task = db.execute(query).scalar_one_or_none()

    if existing_task is None:
        raise HTTPException(status_code=404, detail="Task was not found")

    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    return {'status_code': status.HTTP_204_NO_CONTENT}