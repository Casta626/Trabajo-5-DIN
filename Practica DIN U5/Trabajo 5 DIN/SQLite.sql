create database if not exists CASTAPC;
use CASTAPC;
create table productos {
id_producto varchar(3),
producto varchar(50),
descripcion varchar(150),
precio double(5,2)
stock tinyint,
PRIMARY key (id_producto)
}

CREATE TABLE clientes{
dni char(9),
nombre varchar(25),
apellido1 varchar(25),
apellido2 varchar(25),
PRIMARY key (dni)
}

INSERT into productos values ("001", "Caja Extended ATX con Cristal Templado","Caja",120.43,5);
INSERT into productos values ("002", "RTX 3090 Titan 24GB","Grafica",999.99,2);
INSERT into productos values ("003", "AMD Ryzen 5 3600","Procesador",200.83,7);
INSERT into productos values ("004", "Fuente de Alimentacion 850w","FA",110.13,23);

INSERT into clientes values ("49615646T", "Jose Antonio","Castaneda","Pavon");