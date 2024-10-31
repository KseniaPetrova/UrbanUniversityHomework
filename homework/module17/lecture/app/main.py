from fastapi import FastAPI
from homework.module17.lecture.app.routers import category

app = FastAPI()
# uvicorn homework.module17.lecture.app.main:app
# 127.0.0.1:8000/docs

@app.get("/")
async def welcome():
    return {"msg": "My shop"}

app.include_router(category.router)












