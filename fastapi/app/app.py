from fastapi import FastAPI
from fastapi.responses import FileResponse


app= FastAPI()

@app.get("/", tags=['ROOT'])
async def root() -> dict:
    return {"ping": "pong"}


@app.get('/todo', tags=['todos'])
async def get_todo() -> dict:
    return FileResponse("/home/auxiliar/Desktop/fastapi_crud_crash/fastapi/app/img.png")


@app.post('/todo', tags=['todos'])
async def add_todo(todo:dict) -> dict:
    todos.append(todo)
    return {
        "data": "todo has been added"
    }


todos= [
    {
        "id": "1",
        "Activity": "running",
    }
]