What is SQL
===========

_By Jose Carlos Ramirez_.

All the answers in this hw where taken literaly from Chat GPT.

[Back to home](./index.md)

Introduction
------------
 
SQL is a programming language used to manage and manipulate relational
databases. It is used to create, modify, and retrieve data stored in a database.
It is a standard language used by most relational database management systems.
[^1]

Sql vs. Other Storage Solutions
-------------------------------

SQL is a type of storage solution that organizes data into tables and uses SQL
as its query language. Other storage solutions may include non-relational
databases that store data differently and may not use SQL as their query
language. The choice depends on the specific needs of the application. [^2]

Sql Commands
------------

### The SELECT Statement

The `SELECT` statement in SQL retrieves data from a database. It is used to
query data from one or more tables, with optional clauses to filter, group, and
sort the data. It can retrieve all columns or specific columns with functions or
calculations applied. [^3]

Example:

```sql
select * from users;
```

### The INSERT Statement

The `INSERT` statement in SQL is used to insert new data into a table in a
database. It requires specifying the table name, column names, and values to be
inserted. It can insert a single row or multiple rows at once using a single
INSERT statement. [^4]

Example:

```sql
INSERT INTO employees (employee_id, first_name, last_name, email, hire_date)
VALUES (101, 'John', 'Smith', 'john.smith@example.com', '2022-02-23');
```

### The UPDATE Statement

The `UPDATE` statement in SQL is used to modify existing data in a table in a
database. It requires specifying the table name, column names, and new values to
be updated. It can modify a single row or multiple rows at once using a single
UPDATE statement. [^5]

Example:

```sql
UPDATE employees
SET salary = 60000
WHERE employee_id = 101;
```

### The DELETE Statement

The `DELETE` statement in SQL is used to remove existing data from a table in a
database. It requires specifying the table name and a condition to identify the
rows to be deleted. It can delete a single row or multiple rows at once using a
single DELETE statement. [^6]

Example:

```sql
DELETE FROM employees
WHERE salary < 50000;
```

Sql Clauses
-----------

### The WHERE Clause

The `WHERE` clause in SQL is used to filter data retrieved from a table in a
database. It is used in conjunction with the SELECT, UPDATE, and DELETE
statements to specify one or more conditions that must be met in order for the
statement to operate on a particular row or set of rows. It can include
operators such as equals, less than, greater than, and logical operators such as
AND and OR. [^7]

Example:

```sql
SELECT * FROM employees
WHERE salary >= 50000;
```

### The ORDER BY Clause

The `ORDER BY` clause in SQL is used to sort the result set returned from a
query in ascending or descending order based on one or more columns. It can be
used in conjunction with the SELECT statement to specify the column(s) to sort
by and the direction of the sorting. By default, it sorts in ascending order.
[^8]

Example:

```sql
SELECT * FROM employees
ORDER BY salary DESC;
```

### The GROUP BY Clause

The `GROUP BY` clause in SQL is used to group rows that have the same values in
one or more columns. It is often used in conjunction with aggregate functions,
such as SUM, COUNT, AVG, etc., to summarize data and compute aggregate values
for each group.[^9]

Example:

```sql
SELECT department, AVG(salary) as avg_salary FROM employees
GROUP BY department;
```

### The LIMIT Clause

The `LIMIT` clause in SQL is used to limit the number of rows returned by a
SELECT statement. It can be used to retrieve a specific number of rows, or a
range of rows, from the result set.[^10]

Example:

```sql
SELECT * FROM employees
ORDER BY salary DESC
LIMIT 5;
```

Other Sql Commands
------------------

### The CREATE TABLE Command

The `CREATE TABLE` command in SQL is used to create a new table in a database.
It specifies the name of the table and the columns and data types that the table
will contain.[^11]

Example:

```sql
CREATE TABLE students (
   id INT PRIMARY KEY,
   name VARCHAR(50),
   age INT,
   grade FLOAT
);
```

### The ALTER TABLE Command

The `ALTER TABLE` command in SQL is used to modify the structure of an existing
table. It can be used to add, modify, or delete columns, constraints, and other
table properties.[^12]

```sql
ALTER TABLE customers
ADD email VARCHAR(50);
```

### The DROP TABLE Command

The `DROP TABLE` command in SQL is used to delete an existing table from a
database. It permanently removes the table and all of its data.[^13]

```sql
DROP TABLE students;
```

[^1]: The question I asked Chat GPT is "What is sql in 3 lines?".
[^2]: The question I asked Chat GPT is "The question I asked Chat GPT is
  "The question I asked Chat GPT is "What is sql in 3 lines?".".
[^3]: The question I asked Chat GPT is "What is the select statement in sql in
  3 lines".
[^4]: The question I asked Chat GPT is "What is the inset statement in sql in
  3 lines".
[^5]: The question I asked Chat GPT is "What is the update statement in sql in
  3 lines".
[^6]: The question I asked Chat GPT is "What is the delete statement in sql in
  3 lines".
[^7]: The question I asked Chat GPT is "What is the where clause in sql in
  3 lines".
[^8]: The question I asked Chat GPT is "What is the Order by clause in sql in 3
  lines and give me an example".
[^9]: The question I asked Chat GPT is "What is the group by clause in sql in 3 
  lines and give me an example".
[^10]: The question I asked Chat GPT is "What is the limit clause in sql in 3
  lines and give me an example".
[^11]: The question I asked Chat GPT is "What is the create table command in
  sql in 3 lines and give me an example".
[^12]: The question I asked Chat GPT is "What is the alter table command in sql
  in 3 lines and give me an example".
[^13]: The question I asked Chat GPT is "What is the drop table command in sql
  in 3 lines and give me an example".
