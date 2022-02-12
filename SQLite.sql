create table productos (
id_producto INTEGER PRIMARY KEY NOT NULL,
producto varchar(50),
descripcion varchar(150),
precio double(5,2),
stock tinyint
);

CREATE TABLE clientes(
dni char(9),
nombre varchar(25),
apellido1 varchar(25),
apellido2 varchar(25),
PRIMARY key (dni)
);

INSERT into productos values ("1", "Caja Extended ATX con Cristal Templado","Caja",120.43,5);
INSERT into productos values ("2", "RTX 3090 Titan 24GB","Grafica",999.99,2);
INSERT into productos values ("3", "AMD Ryzen 5 3600","Procesador",200.83,7);
INSERT into productos values ("4", "Fuente de Alimentacion 850w","FA",110.13,23);

INSERT into clientes values ("49615646T", "Jose Antonio","Castaneda","Pavon");
INSERT into clientes values ("62664666P", "Pepe","Llejos","");