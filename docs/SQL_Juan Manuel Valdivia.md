#**¿SQL?** 
##By Juan Manuel Valdivia

SQL (Structured Query Language) es un lenguaje de programación diseñado para administrar y consultar bases de datos relacionales. Se utiliza para crear, modificar y manipular datos almacenados en una base de datos relacional. SQL es un lenguaje declarativo, lo que significa que los usuarios especifican lo que quieren que haga el motor de la base de datos, y este se encarga de determinar la mejor manera de hacerlo.
---

#**¿Qué hace SQL?**
* Crear tablas y definir su estructura y relaciones
* Insertar, actualizar y eliminar registros en una tabla
* Recuperar datos de una o varias tablas utilizando diferentes filtros y criterios
* Agrupar y resumir datos utilizando funciones de agregación como SUM, COUNT, AVG, MAX, MIN, entre otras
* Unir dos o más tablas utilizando JOIN para obtener datos de ambas
* Crear vistas y procedimientos almacenados para simplificar la complejidad de las consultas y automatizar tareas

---
##Conceptos importantes de SQL:
###SELECT
La sentencia SELECT es utilizada para recuperar datos de una o más tablas de una base de datos. La sintaxis básica de la sentencia SELECT es la siguiente:
```
SELECT column1, column2, ...
FROM table_name;
```
Por ejemplo, si tenemos una tabla de empleados con las columnas "id", "nombre", "apellido" y "edad", podemos recuperar todos los registros utilizando la siguiente sentencia SQL:
```
SELECT * FROM empleados;
```
---
##WHERE:
La cláusula WHERE es utilizada para filtrar registros de una tabla que cumplan ciertas condiciones. La sintaxis básica es la siguiente:
```
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```
Por ejemplo, si queremos recuperar los registros de empleados que tengan una edad mayor a 30 años, podemos utilizar la siguiente sentencia SQL:

```
SELECT * FROM empleados WHERE edad > 30;

```


---
##JOIN:
La cláusula JOIN es utilizada para combinar dos o más tablas en una sola consulta. La sintaxis básica es la siguiente:
```
SELECT column1, column2, ...
FROM table1
JOIN table2 ON condition;
```
Por ejemplo, si tenemos una tabla de empleados y una tabla de departamentos, y queremos recuperar el nombre del empleado y el nombre del departamento al que pertenece, podemos utilizar la siguiente sentencia SQL:
```
SELECT empleados.nombre, departamentos.nombre
FROM empleados
JOIN departamentos ON empleados.id_departamento = departamentos.id;
```
---
##INSERT:
La sentencia INSERT es utilizada para insertar nuevos registros en una tabla. La sintaxis básica es la siguiente:
```
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);
```
Por ejemplo, si queremos insertar un nuevo empleado en la tabla "empleados" con los valores "Juan", "Pérez", 25 y "Ventas" en las columnas "nombre", "apellido", "edad" y "departamento" respectivamente, podemos utilizar la siguiente sentencia SQL:
```
INSERT INTO empleados (nombre, apellido, edad, departamento)
VALUES ('Juan', 'Pérez', 25, 'Ventas');

```
---
##UPDATE:
La sentencia UPDATE es utilizada para actualizar registros existentes en una tabla. La sintaxis básica es la siguiente:
```
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```
Por ejemplo, si queremos actualizar la edad de todos los empleados de la tabla "empleados" que tengan un departamento igual a "Ventas" a 30 años, podemos utilizar la siguiente sentencia SQL:
```
UPDATE empleados
SET edad = 30
WHERE departamento = 'Ventas';

```
---
##DELETE:
La sentencia DELETE es utilizada para eliminar registros existentes en una tabla. La sintaxis básica es la siguiente:
```
DELETE FROM table_name
WHERE condition;

```
Por ejemplo, si queremos eliminar todos los empleados de la tabla "empleados" que tengan un departamento igual a "Marketing", podemos utilizar la siguiente sentencia SQL:
```
DELETE FROM empleados
WHERE departamento = 'Marketing';
```
---
GROUP BY:
La cláusula GROUP BY es utilizada para agrupar registros según los valores de una o más columnas, y realizar operaciones de agregación como COUNT, SUM, AVG, entre otras. La sintaxis básica es la siguiente:
```
SELECT column1, column2, ..., aggregate_function(columnX)
FROM table_name
WHERE condition
GROUP BY column1, column2, ...;
```
Por ejemplo, si queremos contar cuántos empleados hay en cada departamento de la tabla "empleados", podemos utilizar la siguiente sentencia SQL:
```
SELECT departamento, COUNT(*) as cantidad_empleados
FROM empleados
GROUP BY departamento;

```