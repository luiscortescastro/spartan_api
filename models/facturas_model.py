from pydantic import BaseModel
from datetime import datetime

class FacturasIn(BaseModel):
    userid: int
    facturaid: int
    
class FacturasOut(BaseModel):
    facturaid: int
    userid: int
    fecha: datetime
    direccion: str
    