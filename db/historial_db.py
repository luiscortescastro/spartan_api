from typing import Dict
from pydantic import BaseModel
from datetime import datetime

class HistorialInDB(BaseModel):
    historialid: int
    facturaid: int
    usuarioid: int
    fecha: datetime
    direccion: str