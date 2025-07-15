from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class UserSchema(BaseModel):
    username: str
    email: str

users = [
    
]

@app.get('/')
async def root():
    return{"message": "backend is running"}

@app.post('/create_user')
async def create_user(userdata:UserSchema):
    new_user = {
        "username": userdata.username,
        "email": userdata.email
    }
    users.append(new_user)
    return {"message":"user created sucessfully","user":new_user}


# @app.get('/greet}')
# async def  greetUsername(username:Optional[str]="User"):
#     return {"message":f"Hello {username}"}