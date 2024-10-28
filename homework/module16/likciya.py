# Get - адрес в строке ? переменная=значение (маршрут к странице)
# Put -
# Post - формы - оформить заказ в магазине
# Delete -

# Запуск сервера python3 - m uvicorn main:app
# адрес строки документации 127.0.0.1:8000/docs



from fastapi import FastAPI, Path
from typing import Annotated
app = FastAPI()
@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}
@app.get("/user/{first_name}/{id}") # Path - контроль вводимых данных
async def news(first_name: Annotated[str, Path(min_length=3, max_length=15, description="Enter your username", example='Naruto')],
               id: str = Path(ge=0, le=100, description="Enter your id", example='18')) -> dict:
    return {"message": f"Hello, {first_name} {id}"}

@app.get("/id")
async def id_paginator(username: str = "alex", age: int = 24) -> dict: # установлены значения по умолчанию
    return {"User": username, "Age": age}














