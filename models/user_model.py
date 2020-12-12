from pydantic import BaseModel

class UserIn(BaseModel):
    userid: int
    password: str
    
class UserOut(BaseModel):
    userid: int
    username: str
    password: str
    telefono: int
    direccion: str
    