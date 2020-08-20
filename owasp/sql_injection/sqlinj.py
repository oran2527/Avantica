#!/usr/bin/python3

import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

DB_HOST = 'localhost' 
DB_USER = 'root' 
DB_PASS = 'root'
DB_NAME = 'prueba' 

def run_query(query=''): 
    datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME] 
            
    conn = MySQLdb.connect(*datos) # Conectar a la base de datos 
    cursor = conn.cursor()         # Crear un cursor 
    cursor.execute(query)          # Ejecutar una consulta 

    if query.upper().startswith('SELECT'): 
        data = cursor.fetchall()   # Traer los resultados de un select 
    else: 
        conn.commit()              # Hacer efectiva la escritura de datos 
        data = None 
                                                                    
    cursor.close()                 # Cerrar el cursor 
    conn.close()                   # Cerrar la conexión 
    return data

dato = input("Tabla para seleccionar datos: ")

while dato is None or dato == '':
    print("No debes dejar en blanco este campo")
    dato = input("Tabla para seleccionar datos: ")

query = "SELECT * FROM {}".format(dato)
print(run_query(query))
