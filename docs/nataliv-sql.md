
# What is SQL?

---
*By Natalia Villalpando Chávez*

## Introduction

---
**SQL is** (Structured Query Language) a programming language 
used to manage and manipulate relational databases. It is used to create, 
read, update and delete data from databases. SQL commands can be used to 
retrieve specific data from a database, perform complex calculations, and 
sort and organize data. SQL is essential for working with databases and is 
used in a wide variety of applications, including web development, data analysis,
and business intelligence.
- **Chat GPT |** I am a data science student and my teacher asked me what is sql?

>**SQL is** a programming language used to store and process information on tables that
can have different characteristics and relationships among each other.
- Research → My words. 

---

## Sql vs. Other Storage Solutions

Here are some reasons why SQL is often considered a better way to store information 
than other storage solutions:

**Structured data storage |** SQL is designed to work with structured data, which means 
that the data is organized into tables and columns with clearly defined relationships. 
This makes it easier to organize and manage data, and allows for efficient querying 
and analysis.

**Flexibility |** SQL allows for a wide range of queries, from simple selects to 
complex multi-table joins and subqueries. This makes it a powerful tool for data 
analysis and reporting, as well as for managing and updating data.

**Scalability |** SQL is designed to work with large datasets, and can be scaled up 
to handle large volumes of data. This makes it a good choice for applications with 
growing data needs.

**Security |** SQL databases offer robust security features, including user authentication, 
access control, and encryption. This helps ensure that sensitive data is protected from 
unauthorized access or theft.

**Standardization |** SQL is a widely used language, and many tools and applications support it. 
This means that SQL databases can be easily integrated with other software and systems, making 
it a flexible and convenient option for data storage and management.

**"Overall, SQL provides a reliable and flexible way to store and manage structured data, making it 
a popular choice for many applications. However, it's important to note that other storage solutions, 
such as NoSQL databases, may be better suited for certain types of data and applications".**

- **Chat GPT |** I am a data science student and I want to know why is SQL a better way to storage 
information than other storage solutions?

> There are many advantages that make SQL a greater option than other storage solutions. These advantages
are listed below:
> 1. It is easier to make a fast query. 
> 2. It is accessible for users everywhere, because it uses a standard language.
> 3. It can incorporate different programming languages (R, Python, among others).
> 4. It works faster and simpler.

- Research → My words. 


---

## SQL Commands

---

### I. Select
The ```SELECT``` statement is used to retrieve data from one or more tables in a database. It is 
used to select a specific column or set of columns from a table and display the result set. The basic 
syntax for a ```SELECT``` statement is:

```sql
SELECT column_name1, /*...*/ FROM tablename;
```
For **example**, to retrieve all columns from a table called "students", you can use the following 
```SELECT``` statement:

```sql
SELECT * FROM students;
```

---
### II. Insert

The ```INSERT``` statement is used to add new rows to a table. It is used to insert a single record 
or multiple records into a table. The basic syntax for an ```INSERT``` statement is:

```sql
INSERT INTO tablename (column1, ...) VALUES (value1, ...);
```
For **example**, to insert a new row into a table called "students", you can use the following ```INSERT```
statement:

```sql
INSERT INTO students (name, age, gender) VALUES ('John', 22, 'Male');
```
---
### III. Delete

The ```DELETE``` statement is used to remove one or more rows from a table. It is used to delete records 
from a table based on specified conditions. The basic syntax for a ```DELETE``` statement is:

```sql
DELETE FROM tablename WHERE kondition;
```
For **example**, to delete a row from a table called "students" where the ID is 1, you can use the following 
```DELETE``` statement:

```sql
DELETE FROM students WHERE id = 1;
```
---
### IV. Update

The ```UPDATE``` statement is used to modify existing rows in a table. It is used to update one or more columns in 
a table based on specified conditions. The basic syntax for an ```UPDATE``` statement is:

```sql
UPDATE tablename SET column_name1 = value1, column_name2 = value2, /*(...)*/ WHERE kondition;
```

For **example**, to update the age of a student with ID 2 to 25 in a table called "students", you can use the following 
```UPDATE``` statement:

```sql
UPDATE students SET age = 25 WHERE id = 2;
```

> *All the information was obtained by asking ChatGPT the following question:
**I am a data science student and I want to understand how the SQL commands work, help me learn and understand the 
functions of the SELECT, INSERT, DELETE and UPDATE commands?***
---

## SQL Clauses

---

### I. Where
The ```WHERE``` clause is used to filter rows based on a specified condition. It is used to select specific rows that meet 
certain criteria. The basic syntax for a ```WHERE``` clause is:

```sql
SELECT column_name1, column_name2, /*...*/ FROM tablename WHERE kondition;
```
For **example**, to select all rows from a table called "students" where the age is greater than or equal to 18, you can 
use the following ```SELECT``` statement with a ```WHERE``` clause:

```sql
SELECT * FROM students WHERE age >= 18;
```
---
### II. Group By

The ```GROUP BY``` clause is used to group rows with the same values into summary rows. It is used to group the result 
set by one or more columns. The basic syntax for a ```GROUP BY``` clause is:

```sql
SELECT column_name1, column_name2, ... FROM tablename GROUP BY column_name1, column_name2, ...;
```

For **example**, to group the result set of a table called "students" by gender, you can use the following 
```SELECT``` statement with a ```GROUP BY``` clause:

```sql
SELECT gender, COUNT(*) FROM students GROUP BY gender;
```

*This will return the number of students grouped by gender.*

---
### III. Order By

The ```ORDER BY``` clause is used to sort the result set in ascending or descending order based on one or more columns. 
It is used to sort the result set by one or more columns. The basic syntax for an ```ORDER BY``` clause is:

```sql
SELECT column_name1, column_name2, ... FROM tablename ORDER BY column_name1 [ASC|DESC];
```

For **example**, to sort the result set of a table called "students" by age in descending order, you can use the following 
```SELECT``` statement with an ```ORDER BY``` clause:

```sql
SELECT * FROM students ORDER BY age DESC;
```
---
### IV. Limit
The ```LIMIT``` clause is used to limit the number of rows returned in the result set. It is used to limit the number 
of rows returned by a query. The basic syntax for a ```LIMIT``` clause is:

```sql
SELECT column_name1, column_name2, /*...*/ FROM tablename LIMIT number_of_rows;
```

For **example**, to limit the number of rows returned in the result set of a table called "students" to 10, you can 
use the following ```SELECT``` statement with a ```LIMIT``` clause:

```sql
SELECT * FROM students LIMIT 10;
```
> *All the information was obtained by asking ChatGPT the following question:
> ***I am a data science student and I want to understand how the SQL commands work, help me learn and understand the 
functions of the SELECT, INSERT, DELETE and UPDATE commands?***

---
## Other SQL Commands

---

### I. Create Table

The ```CREATE TABLE``` command is used to create a new table in a database. It is used to define the structure 
of the table, including the column names, data types, and any constraints. The basic syntax for 
a ```CREATE TABLE``` command is:

```sql
CREATE TABLE tablename (
   column1 datatype constraints,
   column2 datatype constraints,
   ...
   columnN datatype constraints
);
```


For **example**, to create a table called "students" with three columns (id, name, and age), you can use the 
following ```CREATE TABLE``` command:

```sql
CREATE TABLE students (
   id INT PRIMARY KEY,
   name VARCHAR(50) NOT NULL,
   age INT CHECK (age >= 0)
);
```
---
### II. Alter Table

The ```ALTER TABLE``` command is used to modify the structure of an existing table in a database. It is used to 
**add, modify, or delete columns or constraints.** The basic syntax for an ```ALTER TABLE``` command is:

```sql
ALTER TABLE tablename action;
```
> *where "action" can be ADD, ALTER, or DROP.*

For **example**, to add a new column called "gender" to a table called "students", you can use the 
following ```ALTER TABLE``` command:

```sql
ALTER TABLE students ADD gender VARCHAR(10);
```

---
### III. Drop Table
The ```DROP TABLE``` command is used to **delete an existing table in a database.**It is used to completely 
remove the table and all of its data. The basic syntax for a ```DROP TABLE``` command is:

```sql
DROP TABLE tablename;
```

For **example**, to delete a table called "students", you can use the following ```DROP TABLE``` command:

```sql
DROP TABLE students;
```
> *All the information was obtained by asking ChatGPT the following question:
> ***I am a data science student and I want to understand how the SQL commands work, help me learn and understand 
> the functions of the CREATE TABLE, ALTER TABLE and DROP TABLE commands?***
