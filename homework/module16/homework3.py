from fastapi import FastAPI, Path
from typing import Annotated
app = FastAPI()

users_db = {"1": "Имя: Example, возраст: 18"}

@app.get('/users')
async def get_users() -> dict:
    return users_db

@app.post('/user/{username}/{age}')
async def create_user(username: Annotated[str, Path( min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
                      age: Annotated[int, Path(le=120, ge=18, description='Enter age', example='24')]) -> str:
    user_id = str(int(max(users_db, key=int)) +1 )
    users_db[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} is registered'

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: str, 
                      username: Annotated[str, Path( min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
                      age: Annotated[int, Path(le=120, ge=18, description='Enter age', example='24')]) -> str:
    users_db[user_id] = f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} is registered'

@app.delete("/user/{user_id}")
async def delete_user(user_id: str) -> str:
    users_db.pop(user_id)
    return f'User {user_id} has been deleted'


# uvicorn homework.module16.homework3:app
# 127.0.0.1:8000/docs



















