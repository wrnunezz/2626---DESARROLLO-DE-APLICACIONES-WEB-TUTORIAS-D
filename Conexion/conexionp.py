#conectar con bd postgresql

import psycopg2

def obtener_conexion():
    conexion = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='postgres',
        database='ferreteria12',
        port='5432'
    )

    return conexion   

