from fastapi import APIRouter, Depends, status, HTTPException
# Сессия БД
from sqlalchemy.orm import Session
# Функция подключения к БД
from app.backend.db_depends import get_db
# Аннотации, Модели БД и Pydantic.
from typing import Annotated
from app.models import User, Task
from app.schemas import CreateUser, UpdateUser
# Функции работы с записями.
from sqlalchemy import insert, select, update, delete
# Функция создания slug-строки
from slugify import slugify



router = APIRouter(prefix="/user", tags=["user"])

@router.get("/")
async def all_users(db: Annotated[Session, Depends(get_db)]):
    query = select(User)
    users = db.execute(query).scalars().all()
    return users


@router.get("/{user_id}")
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    query = select(User).where(User.id == user_id)
    user = db.execute(query).scalar_one_or_none()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User was not found")

    return user

@router.post("/create")
async def create_user(db: Annotated[Session, Depends(get_db)], user: CreateUser):
    new_user = User(**user.dict())
    db.execute(insert(User).values(**user.dict()))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }

@router.put("/update/{user_id}")
async def update_user(db: Annotated[Session, Depends(get_db)], user_id: int, user: UpdateUser):
    query = select(User).where(User.id == user_id)
    existing_user = db.execute(query).scalar_one_or_none()

    if existing_user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    # Обновляем значения пользователя
    for key, value in user.dict(exclude_unset=True).items():
        setattr(existing_user, key, value)

    db.commit()  # Сохраняем изменения в БД
    return {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}


@router.get("/{user_id}/tasks")
async def tasks_by_user_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
    query = select(Task).where(Task.user_id == user_id)
    tasks = db.execute(query).scalars().all()

    return tasks

@router.delete("/delete/{user_id}")
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    query = select(User).where(User.id == user_id)
    existing_user = db.execute(query).scalar_one_or_none()

    if existing_user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    db.execute(delete(Task).where(Task.user_id == user_id))
    db.execute(delete(User).where(User.id == user_id))
    db.commit()
    return {'status_code': status.HTTP_204_NO_CONTENT}


















