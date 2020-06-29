from conexion import *


def getCarreras():
    cursor = conectar()
    cursor.execute('call getCarrera();')
    data = []
    for row in cursor.fetchall():
        data.append(row[0])
    #cerrar()
    return data
    
def getOcupacion():
    cursors = conectar()
    cursors.execute('call getOcupacion();')
    data = []
    for row in cursors.fetchall():
        data.append(row[0])
    #cerrar()
    return data

def saveUser(nombre, ape1, ape2, mat, car, ocu, imagen, clave, serie):
    print(clave)
    print(serie)
    #img = convertToBinary(imagen)    
    with open(imagen, 'rb') as file:
        img = file.read()
        
    cursor = conectar()
    query = """call guardarUsuario(%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    valores = (nombre, ape1, ape2, mat, car, ocu, img, clave, serie)
    
    cursor.execute(query, valores)
    
    
    #necesitamos revisar el error para poder abiri y cerrar conexion
    #cerrar(cursor)
    
def convertToBinary(imagen):
    with open(imagen, 'rb') as file:
        binaryData = file.read()
        
    return binaryData
    


def searchData(serie, clave):
    cursor = conectar()
    query = """call searchData(%s, %s)"""
    valores = (serie, clave)
    cursor.execute(query, valores)
    data = []
    rows = cursor.fetchall()
    for row in rows:
        data.append(row)
    return data
    