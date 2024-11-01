from fastapi import FastAPI
from homework.module17.homework.app.router import user, task
from homework.module17.homework.app.models import User, Task
from sqlalchemy.schema import CreateTable


app = FastAPI()
# uvicorn homework.module17.homework.app.main:app
# 127.0.0.1:8000/docs
# находясь в дериктории UrbanUniversityHomework\homework\module17\homework>
# alembic init app/migrations
# alembic revision --autogenerate -m "Initial migration"
# alembic -c homework/module17/homework/alembic.ini revision --autogenerate -m "Initial migration"


@app.get("/")
async def welcome():
    return {"msg": "Welcome to Taskmanager"}

app.include_router(user.router)
app.include_router(task.router)

print(CreateTable(User.__table__))
print(CreateTable(Task.__table__))












