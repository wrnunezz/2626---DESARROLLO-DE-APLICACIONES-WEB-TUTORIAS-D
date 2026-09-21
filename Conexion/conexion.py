# conexión con mysql 
import mysql.connector

def obtener_conexion():
    conexion= mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='clase_hoy'

    )
    return conexion

