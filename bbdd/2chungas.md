Hacer una busqueda de todos los productos que tengan menos de 20 existencias, indicando su precio y id de producro y fabricante para poder hacer un pedido a la empresa que lo suministra
```
ELECT id_fab || '-' || id_producto AS id, descripcion AS producto, precio || '€' AS precio, existencias
FROM productos
WHERE existencias <20
ORDER BY existencias DESC, descripcion ASC;
```
