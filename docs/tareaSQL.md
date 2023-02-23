What is SQL
===========

_By Andrea Escoto_.

[Back to home](./index.md)

Introduction
------------
SQL stands for Structured Query Language, and it's a programming language used for managing and manipulating relational databases. Relational databases are a type of database that organizes data into tables, which consist of columns and rows. SQL allows you to create, modify, and query these tables, and it's widely used in the tech industry for managing and analyzing large sets of data.


Sql vs. Other Storage Solutions
-------------------------------
There are several types of storage solutions used in the tech industry, including NoSQL databases, file storage systems, and key-value stores. While each of these solutions has its own strengths and weaknesses, SQL databases are often preferred for their ability to handle complex queries and large amounts of data, as well as their support for data consistency and transactional processing.

Unlike file storage systems, which store data in files on a disk, SQL databases use a relational model that allows for more efficient data retrieval and manipulation. Additionally, while NoSQL databases can be more flexible and scalable than SQL databases, they often sacrifice data consistency and transactional processing in favor of speed and scalability.



Sql Commands
------------
SQL commands are used to interact with and manipulate data in a SQL database. Some common SQL commands include:
- Select
- Insert
- Update
- Delete
- Create
- Alter


### The SELECT command
The `SELECT` command is used to retrieve data from a database table.Example:

```sql
select * from users;
```

* This query selects all columns (*) from the customers table.


### The INSERT command
The `INSERT` command is used to add new data to a database table.Example:

```sql
INSERT INTO customers (name, email) VALUES ('John Doe', 'john.doe@example.com');
```

* This query inserts a new row into the customers table, with the name "John Doe" and email "john.doe@example.com".


### The UPDATE command
The `UPDATE` command is used to modify existing data in a database table.Example:

```sql
UPDATE customers SET email = 'jane.doe@example.com' WHERE name = 'Jane Doe';
```
* This query updates the email address for the customer with the name "Jane Doe" to "jane.doe@example.com"


### The DELETE command
The `DELETE` command is used to remove data from a database table. Example:


```sql
DELETE FROM customers WHERE name = 'John Doe';
```
* This query deletes the row from the customers table where the name is "John Doe".


Sql Clauses
-----------

### The WHERE Clause
The `WHERE` clause to filter the rows returned by a SELECT statement based on a condition. Here's an example:

```sql
SELECT * FROM customers WHERE country = 'USA';
```
* This query selects all columns from the customers table where the country column is equal to "USA".


### The ORDER BY Clause
The `ORDER BY` clause is used to sort the rows returned by a SELECT statement based on one or more columns. Here's an example:

```sql
SELECT * FROM customers ORDER BY last_name ASC;
```
* This query selects all columns from the customers table and sorts the results by the "last_name" column in ascending order (i.e., A to Z).


### The GROUP BY Clause
The `GROUP BY` clause is used to group the rows returned by a SELECT statement based on one or more columns. Here's an example:

```sql
SELECT country, COUNT(*) FROM customers GROUP BY country;
```
* This query groups the rows from the customers table by the country column and returns the number of customers in each country.


### The LIMIT Clause
The `LIMIT` clause is used to limit the number of rows returned by a SELECT statement. Here's an example:

```sql
SELECT * FROM customers LIMIT 10;
```
* This query selects the first 10 rows from the customers table.


Other Sql Commands
------------------

### The CREATE TABLE Command

The `CREATE TABLE` command is used to create a new table in a database. Here's an example:

```sql
CREATE TABLE customers (
  id INT PRIMARY KEY,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  email VARCHAR(100)
);
```
* This query creates a new table called customers with four columns: id, first_name, last_name, and email. The id column is specified as the primary key.


### The ALTER TABLE Command
The `ALTER TABLE` command is used to modify an existing table in a database. Here's an example:

```sql
ALTER TABLE customers ADD COLUMN phone VARCHAR(20);
```
* This query adds a new column called phone to the customers table.


### The DROP TABLE Command
The `DROP TABLE` command is used to delete a table from a database. Here's an example:
```sql
DROP TABLE customers;
```
* This query deletes the customers table from the database.


Note that these examples assume that you already have a database set up and connected to your SQL client.


