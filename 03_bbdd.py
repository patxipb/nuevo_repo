### conexion a bbdd ###
import sqlite3 as dbapi

bbdd = dbapi.connect("bbdd.dat") #creamos la conexion con el fichero donde esta la bbdd

c = bbdd.cursor()

c.execute("""create table users (id int, nombre str, apellido str)""") 
c.execute("""insert into users values(1, 'Patxi', 'PB')""")
c.execute("""insert into users values(2, 'PB', 'Patxi')""")
bbdd.commit()
c.execute("""select * from users""")

for my_tuple in c.fetchall():
    print(type(my_tuple))
    print(my_tuple)

c.close()
bbdd.close()
