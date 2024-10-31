from fastapi import FastAPI
from homework.module17.homework.app.router import user, task


app = FastAPI()
# uvicorn homework.module17.homework.app.main:app
# 127.0.0.1:8000/docs

@app.get("/")
async def welcome():
    return {"msg": "Welcome to Taskmanager"}

app.include_router(user.router)
app.include_router(task.router)














