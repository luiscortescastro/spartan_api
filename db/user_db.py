from typing import Dict
from pydantic import BaseModel

class UserInDB(BaseModel):
    userid: int
    username: str
    password: str
    telefono: int
    direccion: str

database_users = Dict[str, UserInDB]

database_users = {
    101 : UserInDB(**{"userid":101, "username":"angie","password":"angie1234",
                    "telefono":314314, "direccion": "Calle 0 # 0-0"}),
    102 : UserInDB(**{"userid":102, "username":"carlos","password":"carlos1234",
                    "telefono":315315, "direccion": "Calle 0 # 0-0"}),
    103 : UserInDB(**{"userid":103, "username":"david","password":"david1234",
                    "telefono":316316, "direccion": "Calle 0 # 0-0"}),
}

def get_user(userid: int):
    if userid in database_users.keys():
        return database_users[userid]
    else:
        return None

def update_user(user_in_db: UserInDB):
    database_users[user_in_db.userid] = user_in_db
    return user_in_db