from pydantic import BaseModel

class UserIn(BaseModel):
    useremail: str
    password: str
    
class UserOut(BaseModel):
    userid: int
    useremail: str
    username: str
    password: str
    telefono: int
    direccion: str
    