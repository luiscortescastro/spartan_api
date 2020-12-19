from typing import Dict
from pydantic import BaseModel
from datetime import datetime

class FacturasInDB(BaseModel):
    facturaid: int
    userid: int
    fecha: datetime
    direccion: str
    
database_facturas = Dict[int, FacturasInDB]

database_facturas = {
    1001 : FacturasInDB(**{"facturaid": 1001, "userid":101, "fecha":"20201214","direccion": "Calle 0 # 0-0"}),
    1002 : FacturasInDB(**{"facturaid": 1001, "userid":102, "fecha":"20201214","password":"carlos1234",
                    "telefono":315315, "direccion": "Calle 0 # 0-0"}),
    1003 : FacturasInDB(**{"facturaid": 1001, "userid":103, "fecha":"20201214","password":"david1234",
                    "telefono":316316, "direccion": "Calle 0 # 0-0"}),
}

def get_factura(facturaid: int):
    if facturaid in database_facturas.keys():
        return database_facturas[facturaid]
    else:
        return None

# def update_user(user_in_db: UserInDB):
#     database_users[user_in_db.userid] = user_in_db
#     return user_in_db