create database Lab_Inventario
use Lab_Inventario
create table registro_Autorizados(
   nombre VARCHAR(50) NOT NULL,
   apellido VARCHAR(50) NOT NULL,
   usuario VARCHAR(100) NOT NULL,
   password VARCHAR(50) NOT NULL,
   PRIMARY KEY ( usuario )
);
INSERT INTO registro_Autorizados (nombre, apellido,usuario,password)
VALUES ('Gina','Gonzalez','gstephaniegonz','123456');
INSERT INTO registro_Autorizados (nombre, apellido,usuario,password)
VALUES ('Ruby','Mateus','rubymateus','toby12');
INSERT INTO registro_Autorizados (nombre, apellido,usuario,password)
VALUES ('Diego','Espinosa','dig62','reg6271');
INSERT INTO registro_Autorizados (nombre, apellido,usuario,password)
VALUES ('Hector','Gonzalez','hecg','1234');
create table registro_equipos(
    Id INT NOT NULL AUTO_INCREMENT,
    serialeq VARCHAR(6) NOT NULL,
    nombreeq VARCHAR(64) NOT NULL,
    marcaeq VARCHAR(64) NOT NULL,
    caraceq VARCHAR(150) NOT NULL,
    obseq VARCHAR(150) NOT NULL,
    canteq int NOT NULL,
    PRIMARY KEY(Id)
);

INSERT INTO registro_equipos (serialeq,nombreeq,marcaeq,caraceq,obseq,canteq)
VALUES ('24277A','Rotaevaporador','Heidolph','precisión diagonal, pantalla digital, rampas de vacio, interfase usb para el manejo de datos, timer de apagado automático','timer dañado',1);
INSERT INTO registro_equipos (serialeq,nombreeq,marcaeq,caraceq,obseq,canteq)
VALUES ('17226A','Incubadora Con Refrigeración','VWR','Compresor y convección de aire forzada, incluye una cámara interior de acero inoxidable y un exterior con recubrimiento de acero inoxidable.','buen estado',3);
INSERT INTO registro_equipos (serialeq,nombreeq,marcaeq,caraceq,obseq,canteq)
VALUES ('35432C','Mufla De Calentamiento','MRC','Temperatura Máxima 1100 °C O 1200 °C, Calentamiento A Dos Lados Mediante Placas Calefactoras ','resistencia en mal estado',2);


create table registro_reactivos(
    Id INT NOT NULL AUTO_INCREMENT,
    codigoreac VARCHAR(6) NOT NULL,
    nombrereac VARCHAR(64) NOT NULL,
    ubireac VARCHAR(64) NOT NULL,
    pelireac VARCHAR(150) NOT NULL,
    pesoreac float,
    u_medida VARCHAR(150) NOT NULL,
    numcas VARCHAR(150) NOT NULL,
    cantreac int NOT NULL,
    PRIMARY KEY(Id)
);

INSERT INTO registro_reactivos (codigoreac,nombrereac,ubireac,pelireac,pesoreac,u_medida,numcas,cantreac)
VALUES ('87656R','Ácido Sulfúrico','mueble2','corrosivo', '108.10','gramos', '92112-69-1','14');


create table registro_materiales(
    Id INT NOT NULL AUTO_INCREMENT,
    codigomat VARCHAR(6) NOT NULL,
    nombremat VARCHAR(64) NOT NULL,
    ubimat	VARCHAR(64) NOT NULL,
    material VARCHAR(64) NOT NULL,
    obsmat VARCHAR(150) NOT NULL,
    cantmat int NOT NULL,
    PRIMARY KEY(Id)
);

INSERT INTO registro_materiales (codigomat,nombremat,ubimat,material,obsmat,cantmat)
VALUES ('87656M','Agitadores mágneticos','Almacen1','vidrio', 'buen estado','14');


select * from registro_Autorizados;
select * from registro_equipos;
select * from registro_reactivos;
select * from registro_materiales;
