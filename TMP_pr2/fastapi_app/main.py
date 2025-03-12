from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    email: str

# В реальном приложении здесь будет работа с базой данных
fake_db = []

@app.post("/users/")
def create_user(user: User):
    fake_db.append(user)
    return user

@app.get("/users/")
def read_users():
    return fake_db