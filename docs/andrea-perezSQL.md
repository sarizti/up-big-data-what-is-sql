What is SQL
===========

_By Andrea Perez_.

[Back to home](./index.md)

All this information was taken from ChatGPT.

Introduction
------------

SQL (Structured Query Language) is a programming language used 
to manage and manipulate data stored in relational databases. 
SQL is used to create, modify, and query databases, and is widely 
used in data-driven applications such as websites and enterprise software.
Is based on a set of commands called statements, which are used to interact with the database.

SQL is a powerful language that can be used to manipulate and analyze large 
datasets. It is commonly used in industries such as finance, healthcare, and 
e-commerce to manage and analyze customer data, inventory, and other business-critical information.

SQL vs. Other Storage Solutions
-------------------------------

SQL is a relational database management system (RDBMS) that stores data in a structured manner, using tables with rows and columns to organize data. Other storage solutions include NoSQL databases, file systems, and key-value stores.

One of the main differences between SQL and other storage solutions is the way data is organized and stored. In SQL, data is structured and organized in tables with well-defined relationships between them, allowing for efficient querying and analysis. In contrast, NoSQL databases typically store data in a non-relational manner, such as using key-value pairs or document-oriented storage, which can be more flexible for certain types of data but may be less efficient for complex queries.

Another difference is the way data is accessed and queried. SQL databases use SQL, a declarative language, to query data and retrieve results. NoSQL databases may use a variety of query languages, depending on the type of data being stored.

SQL databases also offer strong consistency guarantees, meaning that data is always up-to-date and accurate, whereas some NoSQL databases may provide eventual consistency, which means that data may not be immediately consistent across all nodes in the database system.

Overall, the choice between SQL and other storage solutions depends on the specific needs of the application and the type of data being stored. SQL is often used for structured data and applications that require strong consistency guarantees, while NoSQL databases are often used for unstructured or semi-structured data and applications that require flexibility and scalability.






SQL Commands
------------

### The SELECT Statement

The `SELECT` statement is used to retrieve data from a table or view in the database.

The basic syntax of a `SELECT` statement is:

```sql
SELECT column1, column2 FROM tablename;
```
You can also use the `*` operator to select all columns in a table:

```sql
SELECT * FROM users;
```


### The INSERT Statement

The `INSERT` statement is used to add new data to a table in the database.

The basic syntax of an `INSERT` statement is:
```sql
INSERT INTO tablename (column1, column2, ...) VALUES (value1, value2, ...);
```
If you want to insert data into all columns in the table, you can omit the column list:
```sql
INSERT INTO tablename VALUES (value1, value2, ...);
```


### The UPDATE Statement

The `UPDATE` statement is used to modify existing data in a table in the database.

The basic syntax of an `UPDATE` statement is:
```sql
UPDATE tablename SET column1 = value1, column2 = value2 WHERE condition;
```
Here, _table_name_ is the name of the table that you want to update, and _column1, column2_, and so on are the columns in the table that you want to update. _value1, value2_, and so on are the new values that you want to set for those columns. _condition_ is a logical expression that specifies the condition that a row must meet to be updated.


### The DELETE Statement

The `DELETE` statement is used to remove data from a table in the database.

The basic syntax of a `DELETE` statement is:
```sql
DELETE FROM tablename WHERE kondition;
```
Here, _table_name_ is the name of the table that you want to delete data from, and _condition_ is a logical expression that specifies the condition that a row must meet to be deleted.

You can also delete all rows in a table by omitting the `WHERE` clause:
```sql
DELETE FROM tablename;
```

Sql Clauses
-----------

### The WHERE Clause

The `WHERE` clause in SQL is used to filter data based on specified criteria. It is used in conjunction with `SELECT`, `UPDATE`, and `DELETE` statements to restrict the rows that are returned or modified by the query.

The basic syntax of the `WHERE` clause is as follows:
```sql
SELECT column1, column2
FROM tablename
WHERE kondition;
```
Example:
```sql
SELECT nname FROM users WHERE active=1;
```
In this syntax, _table_name_ is the name of the table that you want to query, and _condition_ is the expression that evaluates to true or false for each row in the table. Rows that evaluate to true are included in the query result, while rows that evaluate to false are excluded.

The condition in the `WHERE` clause can use various comparison operators, logical operators, and functions to compare the values in the columns and return the desired result.


### The ORDER BY Clause

The `ORDER BY` clause in SQL is used to sort the result set of a query in ascending or descending order based on one or more columns. It can be used with `SELECT`, `UPDATE`, `DELETE`, and other SQL statements to sort the rows returned by the query.

The basic syntax of the `ORDER BY` clause is as follows:
```sql
SELECT column1, column2, /*...*/
FROM tablename
ORDER BY column1 [ASC|DESC], column2 [ASC|DESC], ...;
```
The `ORDER BY` clause is a powerful tool for organizing and analyzing data and can be used to sort data in any desired order.


### The GROUP BY Clause

The `GROUP BY` command in SQL is used to group rows that have the same values in one or more columns and aggregate the data in the remaining columns. It is commonly used with aggregate functions such as `SUM`, `AVG`, `COUNT`, `MAX`, and `MIN` to compute summary statistics for each group.

The basic syntax of the `GROUP BY` clause is as follows:
```sql
SELECT column1, column2, /*...,*/ aggregate_function(column)
FROM tablename
GROUP BY column1, column2, ...;
```
Example:
```sql
SELECT product_category, SUM(sales_amount)
FROM sales
GROUP BY product_category;
```
This query groups the rows by product category and computes the sum of the sales amount for each category.


### The LIMIT Clause

The `LIMIT` clause in SQL is used to limit the number of rows returned by a query. It is commonly used with the `SELECT` statement to control the size of the result set.

The basic syntax of the `LIMIT` clause is as follows:
```sql
SELECT column1, column2 
FROM tablename
LIMIT numberofrows;
```
In this syntax, _table_name_ is the name of the table that you want to query, _column1, column2_, etc. are the names of the columns that you want to select, and _number_of_rows_ is the maximum number of rows to return.

Example:
```sql
SELECT *
FROM customers
LIMIT 10;
```


Other Sql Commands
------------------

### The CREATE TABLE Command

The `CREATE TABLE` command is used to create a new table in a relational database. The command specifies the name of the table and defines the columns and their data types that should be present in the table. You can also define constraints like primary key, foreign key, unique, not null, check, and default values while creating the table.

The `CREATE TABLE` command is one of the most fundamental SQL commands and is used extensively while designing a database schema.

Example:

```sql
CREATE TABLE users (
    id int primary key,
    nname varchar(255),
    active tinyint
);
```

### The ALTER TABLE Command

The `ALTER TABLE` command in SQL is used to modify an existing table in a database schema. It allows you to add, modify or remove columns from a table, change the data type of a column, add or drop constraints, and more.

Here are some examples of how you can use the `ALTER TABLE` command:
```sql
ALTER TABLE tablename ADD columnname datatype;
```
```sql
ALTER TABLE tablename MODIFY columnname datatype;
```
```sql
ALTER TABLE tablename RENAME COLUMN oldcolumnname TO newcolumnname;
```
```sql
ALTER TABLE tablename DROP COLUMN columnname;
```
```sql
ALTER TABLE tablename ADD CONSTRAINT constraintname constraintdefinition;
```
```sql
ALTER TABLE tablename DROP CONSTRAINT constraintname;
```
It is important to note that altering a table can potentially have an impact on the data stored in the table, as well as any dependent objects like views, indexes, and stored procedures. Therefore, it is important to thoroughly test any changes before implementing them in a production environment.


### The DROP TABLE Command

The `DROP TABLE` command in SQL is used to remove an existing table from a database schema. The command deletes the table and all its associated data, indexes, triggers, and constraints. Once a table is dropped, it cannot be recovered, so it is important to use this command with caution.

Here is the basic syntax for the `DROP TABLE` command:
```sql
DROP TABLE tablename;
```
In this syntax, table_name is the name of the table that you want to drop. You can also use the IF EXISTS option to avoid getting an error if the table does not exist:
```sql
DROP TABLE IF EXISTS tablename;
```
Some databases may also have additional options or variations for the `DROP TABLE` command, such as dropping multiple tables at once or specifying a cascade option to automatically drop dependent objects.

Before dropping a table, it is important to ensure that you have a backup of the data or that you have migrated any important data to a new table or database. It is also important to check for any dependent objects like views or stored procedures that may be affected by the drop operation.
