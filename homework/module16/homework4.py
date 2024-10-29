"""
Задача "Модель пользователя":
Подготовка:
Используйте CRUD запросы из предыдущей задачи.
Создайте пустой список users = []
Создайте класс(модель) User, наследованный от BaseModel, который будет содержать следующие поля:
id - номер пользователя (int)
username - имя пользователя (str)
age - возраст пользователя (int)

Измените и дополните ранее описанные 4 CRUD запроса:
get запрос по маршруту '/users' теперь возвращает список users.
post запрос по маршруту '/user/{username}/{age}', теперь:
Добавляет в список users объект User.
id этого объекта будет на 1 больше, чем у последнего в списке users. Если список users пустой, то 1.
Все остальные параметры объекта User - переданные в функцию username и age соответственно.
В конце возвращает созданного пользователя.
put запрос по маршруту '/user/{user_id}/{username}/{age}' теперь:
Обновляет username и age пользователя, если пользователь с таким user_id есть в списке users и возвращает его.
В случае отсутствия пользователя выбрасывается исключение HTTPException с описанием "User was not found" и кодом 404.
delete запрос по маршруту '/user/{user_id}', теперь:
Удаляет пользователя, если пользователь с таким user_id есть в списке users и возвращает его.
В случае отсутствия пользователя выбрасывается исключение HTTPException с описанием "User was not found" и кодом 404.
"""

from fastapi import FastAPI, Path, status, Body, HTTPException
from typing import Annotated
from typing import List
from pydantic import BaseModel
app = FastAPI()

users: list = []

class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/users')
async def get_users() -> list:
    return users

@app.post('/user/{username}/{age}')
async def create_user(username: Annotated[str, Path( min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
                      age: Annotated[int, Path(le=120, ge=18, description='Enter age', example='24')]) -> User:
    user_id = 1 if not users else users[-1].id + 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int,
                      username: Annotated[str, Path( min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
                      age: Annotated[int, Path(le=120, ge=18, description='Enter age', example='24')]):
    try:
        for user in users:
            if user.id == user_id:
                user.username = username
                user.age = age
                return user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id: int) -> User:
    try:
        for user in users:
            if user.id == user_id:
                users.remove(user)
                return user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


# uvicorn homework.module16.homework4:app
# 127.0.0.1:8000/docs





































