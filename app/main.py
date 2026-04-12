from fastapi import FastAPI
from app.database import Base
from app.database import engine
from app import models
from app.routers import todo
from app.routers  import user
from app.routers import auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {"todo is running"}

app.include_router(todo.router)
app.include_router(user.router)
app.include_router(auth.router)