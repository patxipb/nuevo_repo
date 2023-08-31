from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

#entidad ususario
class User(BaseModel):
    id: int
    name: str
    surname: str

### conexion a bbdd ###
import sqlite3 as dbapi

bbdd = dbapi.connect("API/bbdd/users.dat") #creamos la conexion con el fichero donde esta la bbdd

c = bbdd.cursor()

c.execute("""select * from users""")

list_user = c.fetchall()
print(list_user[1])
c.close()
bbdd.close()
