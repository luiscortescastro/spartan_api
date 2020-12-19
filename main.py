from db.user_db import UserInDB
from db.user_db import get_user, update_user
from models.user_model import UserIn, UserOut
import datetime
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware

api = FastAPI()

origins = [
    "http://localhost:8080",
    "http://127.0.0.1:8080"
]
api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@api.post("/user/auth/")
async def user_auth(user_in: UserIn):
    user_in_db = get_user(user_in.useremail)
    if user_in_db == None:
        raise HTTPException(status_code=404, 
                            detail = 'El Usuario No Existe')
    if user_in_db.password != user_in.password:
        return {'Autenticado': False}
    return {'Autenticado': True}
        
@api.get("/user/config/{useremail}")
async def get_historial(useremail: str):
    user_in_db = get_user(useremail)
    if user_in_db == None:
        raise HTTPException(status_code=404, detail = 'El Usuario No Existe')
    user_out = UserOut(**(user_in_db.dict()))
    return user_out
    
