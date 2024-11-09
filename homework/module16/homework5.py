"""

"""

from fastapi import FastAPI, Path, status, Body, HTTPException, Request, Form
from typing import Annotated
from typing import List
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()
templates = Jinja2Templates(directory=os.path.join("homework.txt", "module16", "templates"))

users: list = []

class User(BaseModel):
    id: int
    username: str
    age: int

@app.get("/")
def get_all_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html",
                                      {'request': request,
                                       'users': users})

@app.get('/user/{user_id}')
async def get_users(request: Request, user_id: int) -> HTMLResponse:
    user = next((user for user in users if user.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    return templates.TemplateResponse("users.html",
                                      {'request': request,
                                       'user': user})

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
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user

    raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id: int) -> User:
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User was not found")


# uvicorn homework.txt.module16.homework5:app
# 127.0.0.1:8000/docs


































