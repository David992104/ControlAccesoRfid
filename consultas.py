from conexion import *

def saveUser(nombre, ape1, ape2, mat, car, ocu, imagen, clave, serie):
    print(clave)
    print(serie)
    img = convertToBinary(imagen)    
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
    
