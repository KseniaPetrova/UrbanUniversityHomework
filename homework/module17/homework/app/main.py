from fastapi import FastAPI
from app.router import user, task
from app.models import User, Task
from sqlalchemy.schema import CreateTable


app = FastAPI()
# uvicorn homework.txt.module17.homework.txt.app.main:app
# cd homework.txt/module17/homework.txt
# uvicorn app.main:app
# 127.0.0.1:8000/docs
# находясь в дериктории UrbanUniversityHomework\homework.txt\module17\homework.txt>
# alembic init app/migrations
# alembic revision --autogenerate -m "Initial migration"
# alembic -c homework.txt/module17/homework.txt/alembic.ini revision --autogenerate -m "Initial migration"


@app.get("/")
async def welcome():
    return {"msg": "Welcome to Taskmanager"}

app.include_router(user.router)
app.include_router(task.router)

print(CreateTable(User.__table__))
print(CreateTable(Task.__table__))












