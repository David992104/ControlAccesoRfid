import pymysql

db = pymysql.connect('osda.com.mx', 'osdacomm_raspberry', 'qaz plm 10 &', 'osdacomm_control_acceso')

def conectar():
    cursor = db.cursor()
    return cursor
    
def cerrar(cursor):
    db.commit()
    cursor.close()
    db.close()
    print('Conexion cerrada')
    
    
