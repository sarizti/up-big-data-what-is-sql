What is SQL?
===========

_By Juan Manuel Valdivia_.

[Back to home](./index.md)

Introduction
------------
SQL, or Structured Query Language, is a programming language used to manage and manipulate data stored in relational databases. SQL is a standardized language that allows users to interact with databases to perform various operations such as creating, retrieving, updating, and deleting data. SQL is used in a wide range of applications, from small personal databases to large enterprise-level systems.

Sql vs. Other Storage Solutions
-------------------------------
Compared to other storage solutions, SQL databases offer several advantages. First, they are highly structured and provide a well-defined data model, which makes it easy to organize and query data. SQL databases also support complex queries that can span multiple tables and use advanced filtering and aggregation techniques.

In addition, SQL databases provide strong data consistency and integrity guarantees, making them suitable for use in applications that require high reliability and data accuracy. Finally, SQL databases are widely used and have a large ecosystem of tools and resources available, which makes them accessible to a wide range of users and developers.


Sql Commands
------------
SQL commands are used to interact with and manipulate data in a SQL database. Some common SQL commands include:

- **SELECT**

- **INSERT**

- **UPDATE**

- **DELETE**

- **CREATE**

- **ALTER**

- **DROP**

- **JOIN**

- **GROUP BY**

- **ORDER BY**

- **WHERE**

- **HAVING**

### The SELECT command
The `SELECT` command is used to retrieve data from a database table.Example:

```sql
SELECT * FROM customers;
SELECT name, email FROM customers WHERE age > 30;
```

### The INSERT command
The `INSERT` command is used to add new data to a database table.Example:

```sql
INSERT INTO customers (name, email, age) VALUES ('John Smith', 'john@example.com', 25);
```


### The UPDATE command
The `UPDATE` command is used to modify existing data in a database table.Example:

```sql
UPDATE customers SET age = 30 WHERE name = 'John Smith';
```


### The DELETE command
The `DELETE` command is used to remove data from a database table. Example:


```sql
DELETE FROM customers WHERE age > 50;
```
### The CREATE TABLE Command

The `CREATE TABLE` command is used to create a new table in a database. Here's an example:

```sql
CREATE TABLE orders (
    id INT PRIMARY KEY, 
    customer_id INT, 
    order_date DATE, 
    total DECIMAL(10,2));
```
### The ALTER TABLE Command
The `ALTER TABLE` command is used to modify an existing table in a database. Here's an example:

```sql
ALTER TABLE customers ADD address VARCHAR(255);
```
### The DROP TABLE Command
The `DROP TABLE` command is used to delete a table from a database. Here's an example:
```sql
DROP TABLE orders;
```
### The JOIN Command
The `JOIN` command is used to combine data from two or more tables based on a common field. Here's an example:
```sql
SELECT customers.name, orders.order_date, orders.total
FROM customers
INNER JOIN orders
ON customers.id = orders.customer_id;
```

### The GROUP BY Clause
The `GROUP BY` clause is used to group the rows returned by a SELECT statement based on one or more columns. Here's an example:

```sql
SELECT category, COUNT(*) as num_products, AVG(price) as avg_price
FROM products
GROUP BY category;
```
### The ORDER BY Clause
The `ORDER BY` clause is used to sort the rows returned by a SELECT statement based on one or more columns. Here's an example:

```sql
SELECT name, age
FROM customers
ORDER BY age DESC;
```

### The WHERE Clause
The `WHERE` clause to filter the rows returned by a SELECT statement based on a condition. Here's an example:

```sql
SELECT name, email
FROM customers
WHERE age > 30;
```

### HAVING
The `HAVING` clause is used to filter grouped data based on specified conditions. Here's an example:
```sql
SELECT category, AVG(price) as avg_price
FROM products
GROUP BY category
HAVING AVG(price) > 1000;

```



