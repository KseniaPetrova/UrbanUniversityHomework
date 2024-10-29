# Get - адрес в строке ? переменная=значение (маршрут к странице)
# Put -
# Post - формы - оформить заказ в магазине
# Delete -

# Запуск сервера python3 - m uvicorn main:app
# адрес строки документации 127.0.0.1:8000/docs

from fastapi import FastAPI, Path
from typing import Annotated
app = FastAPI()

# @app.get("/")
# async def welcome() -> dict:
#     return {"message": "Hello World"}
# @app.get("/user/{first_name}/{id}") # Path - контроль вводимых данных
# async def news(first_name: Annotated[str, Path(min_length=3, max_length=15, description="Enter your username", example='Naruto')],
#                id: str = Path(ge=0, le=100, description="Enter your id", example='18')) -> dict:
#     return {"message": f"Hello, {first_name} {id}"}
#
# @app.get("/id")
# async def id_paginator(username: str = "alex", age: int = 24) -> dict: # установлены значения по умолчанию
#     return {"User": username, "Age": age}

#--------------------------------------------

massages_db = {"0": "First post in FastApi"}

@app.get("/")
async def get_all_msg() -> dict:
    return massages_db

@app.get("msg/{msg_id}") #
async def get_msg(msg_id: str) -> dict:
    return massages_db[msg_id]

@app.post('msg')
async def create_msg(msg: str) -> str:
    current_index = str(int(max(massages_db, key=int)) +1 )
    massages_db[current_index] = msg
    return 'Massage created!'

@app.put('msg/{msg_id}')
async def update_msg(msg_id: str, msg: str) -> str:
    massages_db[msg_id] = msg
    return 'Massage update'

@app.delete('/msg/{msg_id}')
async def delete_msg(msg_id: str) -> str:
    massages_db.pop(msg_id)
    return f'Message with {msg_id} was deleted'

@app.delete('/')
async def delete_all_msg() -> str:
    massages_db.clear()
    return "All messages deleted"








