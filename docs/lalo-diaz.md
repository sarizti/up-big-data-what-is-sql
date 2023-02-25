What is SQL
===========

_By Eduardo Díaz_.

[Back to home](./index.md)

Introduction
------------

SQL stands for Structured Query Language. It is a programming language used to manage and manipulate relational databases.

SQL is used to create, modify, and query databases. It provides a set of commands and syntax for performing operations on the data stored in a relational database. With SQL, you can create tables to store data, insert data into tables, retrieve data from tables based on specified criteria, update existing data in tables, and delete data from tables.

SQL is used by database administrators, developers, data analysts, and other professionals who work with data. It is an essential tool for working with large and complex datasets, and is widely used in industries such as finance, healthcare, e-commerce, and many others.

Sql vs. Other Storage Solutions
-------------------------------
Here are some key differences between SQL and other storage solutions:

Data model: SQL uses the relational data model, which organizes data into tables with columns and rows. NoSQL databases use different data models, such as document-oriented, key-value, or graph-based data models, to store and manage data.
Query language: SQL uses a standard language called Structured Query Language to query and manipulate data. Other storage solutions may use different query languages or APIs for accessing and querying data.
Scalability: NoSQL databases are designed for horizontal scalability, meaning they can scale out to multiple nodes and handle large amounts of data and traffic. SQL databases can also be scaled out, but they are typically limited by the capabilities of the underlying hardware.
Data consistency: SQL databases use ACID (Atomicity, Consistency, Isolation, and Durability) transactions to ensure data consistency and integrity. NoSQL databases may sacrifice consistency in favor of other factors such as scalability or availability.
Use cases: SQL databases are well-suited for applications that require complex queries, transactions, and relational data structures. NoSQL databases are often used for applications that require high performance, scalability, and flexibility in data models.
Ultimately, the choice between SQL and other storage solutions depends on the specific needs of your application, including performance, scalability, data complexity, and query requirements.

Sql Commands
------------

### The SELECT Statement

The SELECT statement is used in SQL to retrieve data from one or more tables in a database. The SELECT statement is the most commonly used statement in SQL and is used to extract data based on specified criteria.

The SELECT statement includes the following components:

SELECT: This is the first keyword of the SELECT statement and specifies the columns that will be retrieved.
FROM: This keyword specifies the table or tables from which the data will be retrieved.
WHERE: This optional keyword specifies the conditions that must be met in order for a row to be included in the result set.
GROUP BY: This keyword is used to group rows based on a specified column or set of columns.
HAVING: This optional keyword is used to filter groups based on specified conditions.
ORDER BY: This keyword is used to sort the result set based on specified columns.
For example, the following SELECT statement retrieves all rows from the "customers" table where the "city" column is equal to "New York":

Example:

```sql
SELECT * FROM customers WHERE city = 'New York';
```

The result set of this query will include all columns from the "customers" table for all rows where the "city" column is equal to "New York".

### The INSERT Statement

The INSERT statement is used in SQL to insert data into a table in a database. The INSERT statement is used to add new rows of data to an existing table or to create a new table with data.

The INSERT statement includes the following components:

INSERT INTO: This is the first keyword of the INSERT statement and specifies the name of the table into which data will be inserted.
VALUES: This keyword specifies the values to be inserted into the table. The values must be specified in the same order as the columns in the table.
For example, the following INSERT statement inserts a new row of data into the "customers" table:

INSERT INTO customers (first_name, last_name, email, phone)
SELECT first_name, last_name, email, phone
FROM new_customers;

This statement inserts data into the "customers" table from the "new_customers" table for the columns specified in the SELECT statement.

### The UPDATE Statement

The UPDATE statement is used in SQL to modify existing data in a table in a database. The UPDATE statement is used to change the values of one or more columns in one or more rows of a table.

The UPDATE statement includes the following components:

UPDATE: This is the first keyword of the UPDATE statement and specifies the name of the table to be updated.
SET: This keyword specifies the new values for the columns to be updated.
WHERE: This keyword specifies the conditions that must be met in order for a row to be updated. If the WHERE clause is omitted, all rows in the table will be updated.
For example, the following UPDATE statement updates the phone number of a customer in the "customers" table where the "customer_id" is 1:

UPDATE customers
SET phone = '555-5678'
WHERE customer_id = 1;

### The DELETE Statement

The DELETE statement is used in SQL to remove one or more rows from a table in a database. The DELETE statement is used to permanently remove data from a table.

The DELETE statement includes the following components:

DELETE FROM: This is the first keyword of the DELETE statement and specifies the name of the table from which data will be deleted.
WHERE: This keyword specifies the conditions that must be met in order for a row to be deleted. If the WHERE clause is omitted, all rows in the table will be deleted.
For example, the following DELETE statement deletes a row from the "customers" table where the "customer_id" is 1:

DELETE FROM customers
WHERE customer_id = 1;

This statement deletes the row from the "customers" table where the "customer_id" is 1.

If you want to delete all rows from a table, you can omit the WHERE clause:

DELETE FROM customers;

Sql Clauses
-----------

### The WHERE Clause

The WHERE clause is used in SQL to specify a condition that must be met in order for a row to be returned in a SELECT statement, or updated or deleted in an UPDATE or DELETE statement.

The WHERE clause is used to filter the data based on a specific condition or set of conditions. It can be used to filter data based on one or more columns in a table, and can include operators such as equals (=), greater than (>), less than (<), and not equal to (<>), among others.

For example, the following SELECT statement retrieves all the rows from the "customers" table where the "city" is 'New York':

SELECT *
FROM customers
WHERE city = 'New York';

### The ORDER BY Clause

The ORDER BY clause is used in SQL to sort the result set of a SELECT statement by one or more columns in ascending or descending order.

The ORDER BY clause is used to sort the rows returned by a SELECT statement in a specific order based on the values in one or more columns. It can be used to sort data in ascending (default) or descending order, and can also be used to sort data by multiple columns.

For example, the following SELECT statement retrieves all the rows from the "customers" table and sorts them in ascending order by the "last_name" column:

SELECT *
FROM customers
ORDER BY last_name;

### The GROUP BY Clause

The GROUP BY clause is used in SQL to group the result set of a SELECT statement by one or more columns, and to apply aggregate functions such as SUM, COUNT, AVG, MIN, and MAX to each group.

The GROUP BY clause is used to group the rows returned by a SELECT statement into sets of rows based on the values in one or more columns. It is often used in combination with aggregate functions to compute summary statistics for each group of rows.

For example, the following SELECT statement retrieves the total sales for each salesperson in the "orders" table:

SELECT salesperson, SUM(order_total) as total_sales
FROM orders
GROUP BY salesperson;

### The LIMIT Clause

The LIMIT clause is used in SQL to limit the number of rows returned by a SELECT statement to a specified number.

The LIMIT clause is used to restrict the number of rows returned by a SELECT statement to a specified number. It is often used in combination with the ORDER BY clause to retrieve a specific subset of rows from a result set.

For example, the following SELECT statement retrieves the first 10 rows from the "customers" table in alphabetical order by the "last_name" column:

SELECT *
FROM customers
ORDER BY last_name
LIMIT 10;

This statement returns the first 10 rows from the "customers" table in alphabetical order by the "last_name" column.

Other Sql Commands
------------------

### The CREATE TABLE Command

The CREATE TABLE command in SQL is used to create a new table in a database.

The syntax for the CREATE TABLE command is as follows:

CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype,
    ...
);

In this syntax, table_name is the name of the table that you want to create, and column1, column2, column3, and so on, are the names of the columns in the table. The datatype specifies the type of data that each column can store.

After you execute the CREATE TABLE command, a new table is created in the database, with the specified columns and datatypes. You can then use other SQL commands like INSERT, SELECT, UPDATE, and DELETE to manipulate the data in the table.

### The ALTER TABLE Command

The ALTER TABLE command in SQL is used to modify the structure of an existing table in a database. It allows you to add, modify, or delete columns in a table, change the data type of columns, add or remove constraints, and more.

The syntax for the ALTER TABLE command varies depending on the specific modification that you want to make. Here are some examples:

To add a new column to an existing table:

ALTER TABLE table_name
ADD COLUMN column_name datatype;

### The DROP TABLE Command

The DROP TABLE command in SQL is used to delete a table and all of its data from a database. When you execute the DROP TABLE command, you permanently remove the entire table, including all of its rows, columns, constraints, and indexes.

The syntax for the DROP TABLE command is as follows:
DROP TABLE table_name;

In this syntax, table_name is the name of the table that you want to delete. After you execute the DROP TABLE command, the table is permanently deleted from the database.

It's important to be careful when using the DROP TABLE command, as it can have unintended consequences if you accidentally delete a table that you still need. Always make sure to double-check the table name and make a backup of the table data before using the DROP TABLE command.
