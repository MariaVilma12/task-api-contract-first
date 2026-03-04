import yaml
from fastapi import FastAPI, Depends, HTTPException
from fastapi import Response
from sqlalchemy.orm import Session

from backend.database import engine, SessionLocal
import backend.models as models
import backend.crud as crud

# Create tables
models.Base.metadata.create_all(bind=engine)

# Load OpenAPI contract
with open("openapi.yaml", "r") as f:
    openapi_schema = yaml.safe_load(f)

app = FastAPI()

app.openapi_schema = openapi_schema

def custom_openapi():
    return app.openapi_schema

app.openapi = custom_openapi

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db)

@app.post("/tasks", status_code=201)
def create_task(task: dict, db: Session = Depends(get_db)):
    return crud.create_task(db, task)

@app.get("/tasks/{taskId}")
def get_task(taskId: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, taskId)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.delete("/tasks/{taskId}", status_code=204)
def delete_task(taskId: int, db: Session = Depends(get_db)):
    task = crud.delete_task(db, taskId)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return Response(status_code=204)