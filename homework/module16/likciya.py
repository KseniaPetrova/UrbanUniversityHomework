# Get - адрес в строке ? переменная=значение (маршрут к странице)
# Put -
# Post - формы - оформить заказ в магазине
# Delete -

# Запуск сервера python3 - m uvicorn main:app
# адрес строки документации 127.0.0.1:8000/docs



from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}
@app.get("/user/{first_name}/{last_name}")
async def news(first_name: str, last_name: str) -> dict:
    return {"message": f"Hello, {first_name} {last_name}"}

@app.get("/id")
async def id_paginator(username: str = "alex", age: int = 24) -> dict: # установлены значения по умолчанию
    return {"User": username, "Age": age}














