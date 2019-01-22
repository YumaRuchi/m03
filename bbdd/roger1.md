Mostrar todas las columnas y filas de la tabla clientes en orgen de llegada |
--- |
SELECT *
FROM clientes;|

Muestra las columnas id_producto y existencias de todas las filas de la tabla productos |
--- |
SELECT id_producto, existencias
FROM productos;|

Mostrar el numero total de las filas de la tabla productos (sin contar la cabecera), devuelve un numero (ej 15 |
--- |
SELECT COUNT (*)
FROM productos;|

Muestra todos los valores de la columna existencias que no sean NULL |
--- |
SELECT COUNT(existencias)
FROM productos;|

Muestra todos los clientes ordenados por la columna "empresa" en orden alfabetico |
--- |
SELECT *
FROM clientes
ORDER BY limite_credito ASC;|

Muestra todos lños clientes ordenados por la columna "empresa" en orden alfabetico inverso |
--- |
SELECT *
FROM clientes
ORDER BY limite_credito DESC;|

Muestra todos los pedidos ordenados por: "num_pedido" en orden ascendiente y "importe" en orden descendiente |
--- |
SELECT *
FROM pedidos
ORDER BY num_pedido ASC, importe DESC;|

Muestra los 7 primeros pedidos ordenados por: "num_pedido" en orden ascendiente y "importe" en orden descendiente |
--- |
SELECT *
FROM pedidos
ORDER BY num_pedido ASC, importe DESC
LIMIT 7;|
