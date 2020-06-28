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

    
