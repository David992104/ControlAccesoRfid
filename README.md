Instalar lo siguiente 

instalar gpio
intalar pymysql

Los procedures son: 'Posteriormente se cargara el .sql de la base de datos
  Para los combo box:
    create PROCEDURE getCarrera()
    begin
	      select nombrecarrera from carrera ;
    END
    create procedure getOcupacion()
    begin 
      select nombrearea from area;
    end
    
  Para añadir usuario:
  
CREATE PROCEDURE guardarUsuario(
    IN nombre VARCHAR(50),
    IN ape1 VARCHAR(50),
    IN ape2 VARCHAR(50),
    IN mat VARCHAR(10),
    IN carreraView VARCHAR(100),
    IN ocupacion VARCHAR(50),
    IN imagen LONGBLOB,
    IN clave VARCHAR(10),
    IN serie VARCHAR(50))
BEGIN 
    DECLARE idcar INT;
    DECLARE idocu INT;
    DECLARE idusuario INT;
		
    SELECT idcarrera into idcar FROM carrera WHERE nombrecarrera = carreraView;
    SELECT idarea into idocu FROM area WHERE nombrearea = ocupacion;    
		
    INSERT INTO usuario VALUES( NULL, nombre, ape1, ape2, mat, idcar, idocu, imagen, 1);
    COMMIT;
		
		SELECT iduser into idusuario FROM usuario WHERE matricula = mat;
		
		INSERT INTO sensores VALUES(NULL, serie, idusuario, clave);
		select "ok";
END


   

    
