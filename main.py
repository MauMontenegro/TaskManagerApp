from fastapi import FastAPI
from pydantic import BaseModel
from typing import Annotated,List

app = FastAPI()

class Tasks(BaseModel):
    name : str
    description: str | None
    finished : bool = False

# Dummy DataBase
todos = []

# End-points
@app.get("/todos",response_model=List[Tasks]) # Here i expect a list of models
async def get_tasks():
    return todos

@app.post("/todos",response_model=Tasks) # Here i only expect only one model
async def add_task(task:Tasks):
    todos.append(task)
    return task
