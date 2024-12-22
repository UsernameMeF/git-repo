from fastapi import FastAPI
from db import schemas

users = [schemas.User(id=0, username="User1", email="example1@gmail.com"),
        schemas.User(id=0, username="User1", email="example1@gmail.com"),
        schemas.User(id=0, username="User1", email="example1@gmail.com")
            ]


app = FastAPI()


@app.post("/create-user/")
def create_user(user: schemas.User):
    users.append(user)
    print(users)


@app.get("/users/")
def get_users():
    return users

@app.get("/users/{user.id}")
def get_users(user_id: int):
    for user in users:
        if user.id == user.id:
            return user



if __name__ == "__main__":
    import os
    os.system("uvicorn main:app --reload")
