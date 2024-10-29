# Get - адрес в строке ? переменная=значение (маршрут к странице)
# Put -
# Post - формы - оформить заказ в магазине
# Delete -

# Запуск сервера python3 - m uvicorn main:app
# адрес строки документации 127.0.0.1:8000/docs

from fastapi import FastAPI, Path, status, Body, HTTPException
from typing import Annotated
from typing import List
from pydantic import BaseModel
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

# massages_db = {"0": "First post in FastApi"}
#
# @app.get("/")
# async def get_all_msg() -> dict:
#     return massages_db
#
# @app.get("msg/{msg_id}") #
# async def get_msg(msg_id: str) -> dict:
#     return massages_db[msg_id]
#
# @app.post('msg')
# async def create_msg(msg: str) -> str:
#     current_index = str(int(max(massages_db, key=int)) +1 )
#     massages_db[current_index] = msg
#     return 'Massage created!'
#
# @app.put('msg/{msg_id}')
# async def update_msg(msg_id: str, msg: str) -> str:
#     massages_db[msg_id] = msg
#     return 'Massage update'
#
# @app.delete('/msg/{msg_id}')
# async def delete_msg(msg_id: str) -> str:
#     massages_db.pop(msg_id)
#     return f'Message with {msg_id} was deleted'
#
# @app.delete('/')
# async def delete_all_msg() -> str:
#     massages_db.clear()
#     return "All messages deleted"

#--------------------------------------------
from fastapi import Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

msg_db = []

class Msg(BaseModel):
    id: int = None
    text: str

@app.get("/")
def get_all_msg(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("message.html",
                                      {'request': request,
                                       'messages': msg_db})

@app.get(path='/msg/{msg_id}')
def get_msg(request: Request, msg_id: int) -> HTMLResponse:
    try:
        return templates.TemplateResponse("message.html",
                                      {'request': request,
                                       'messages': msg_db[msg_id]})
    except IndexError:
        raise HTTPException(status_code=404, detail="Message not found")

@app.post('/')
def create_msg(request: Request, msg: str = Form()) -> HTMLResponse:
    if msg_db:
        msg_id = max(msg_db, key=lambda m: m.id).id +1
    else:
        msg_id = 0
    msg_db.append(Msg(id=msg_id, test = msg))
    return templates.TemplateResponse("message.html",
                                      {'request': request,
                                       'messages': msg_db})

@app.put('/msg/{msg_id}')
def update_msg(msg_id: int, msg: str = Body()) -> str:
    try:
        edit_msg = msg_db[msg_id]
        edit_msg.text = msg
        return f'Message updated'
    except IndexError:
        raise HTTPException(status_code=404, detail="Message not found")

@app.delete('/msg/{msg_id}')
def delete_msg(msg_id: int) -> str:
    try:
        msg_db.pop(msg_id)
        return f'Message ID={msg_id} deleted'
    except IndexError:
        raise HTTPException(status_code=404, detail="Message not found")

@app.delete('/')
def kill_msg_all() -> str:
    msg_db.clear()
    return "All message deleted"




