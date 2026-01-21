CREATE TABLE Producto(
    id INT PRIMARY KEY,
    name VARCHAR(25) NOT NULL,
    price FLOAT DEFAULT 0,
    arrive_date DATE,
    brand VARCHAR(25) NOT NULL
);

CREATE TABLE Usuario(
    email VARCHAR(30) PRIMARY KEY,
    name VARCHAR(25) NOT NULL
);

CREATE TABLE Facturas(
    id INT PRIMARY KEY,
    purshed_date DATE,
    user_email VARCHAR REFERENCES Usuario(email),
    total FLOAT DEFAULT 0
);

CREATE TABLE Carrito(
    id_producto INT REFERENCES Producto(id),
    id_usuario  VARCHAR(30) REFERENCES Usuario(email),
    amount INT DEFAULT 0,
    total FLOAT DEFAULT 0
);

CREATE TABLE Producto_Factura(
    id_factura INT REFERENCES Factura(id),
    id_producto INT REFERENCES Producto(id),
    amount INT DEFAULT 0,
    total FLOAT DEFAULT 0
);

ALTER TABLE Facturas
    ADD COLUMN owner_phone INT NOT NULL,
    ADD COLUMN employee_id VARCHAR(25) NOT NULL;

SELECT *
    FROM Producto;

SELECT *
    FROM Producto
    WHERE price > 5000;  
    
SELECT *
    FROM Producto_Factura
    WHERE id_producto = 4;

SELECT 
    id_producto,
    id_usuario,
    SUM(amount) as cantidad,
    SUM(total) as total_final
    FROM Carrito
    GROUP BY id_producto

SELECT *
    FROM Facturas
    WHERE user_email = 'd-vargas08@hotmail.com'

SELECT *
    FROM Facturas
    ORDER BY total DESC;

SELECT *
    FROM Facturas
    WHERE id = 2