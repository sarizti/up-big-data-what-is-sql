#**What is SQL**
**by Jorge Arroyo**

---

##**SQL is...**

- SQL is like a special language that helps computers store and organize information in a way that makes it easy to find and use later. It's kind of like a big library where all the books are sorted into different categories so you can easily find the one you want to read. With SQL, you can ask the computer to find certain information for you, like all the books in the library that are about dogs, and it will give you a list of all the books that match your request.


---

## **SQL vs other solutions**
- SQL is a language that is used to communicate with relational databases, which are a specific type of storage solution. Relational databases organize data into tables that are connected to each other through relationships, and SQL is used to retrieve, modify, and delete data from those tables. Other storage solutions may use different data structures and have different ways of organizing data. For example, some storage solutions might use non-relational databases, which organize data differently and may not use SQL as a language for interacting with the database. There are also other types of storage solutions, such as file systems or key-value stores, that have different ways of storing and accessing data.

In general, the choice of storage solution depends on the specific needs of the application or system being developed. SQL and relational databases are often used for applications that require complex data relationships and querying capabilities, while other storage solutions may be better suited for applications with simpler data needs or specific performance requirements.

---

##**SQL Commands**

###*Select*

- The SELECT command is a SQL statement used to retrieve data from a database. It is the most commonly used command in SQL and is used to query a database table and retrieve specific data based on specified criteria.

- When using the SELECT command, you specify the name of the table you want to query and the columns you want to retrieve data from. You can also specify optional conditions to filter the results based on specific criteria, such as only retrieving rows where a certain column matches a particular value.

For example, the following SQL statement retrieves all the data from the "customers" table:

> SELECT * FROM customers;

- This statement retrieves all the columns and all the rows in the "customers" table. If you only wanted to retrieve the "name" and "email" columns for customers who live in a certain city, you could use a statement like this:

> SELECT name, email FROM customers WHERE city = 'New York';

- This statement retrieves only the "name" and "email" columns for customers who have the value "New York" in the "city" column. The WHERE clause is used to filter the results based on this criteria.

###*Insert*

- The INSERT command is a SQL statement used to insert new data into a table in a database. It is used to add one or more new rows of data to an existing table.

- To use the INSERT command, you specify the name of the table you want to insert data into and the values you want to add for each column. The values must match the data types of the corresponding columns in the table.

For example, if you have a "customers" table with columns for "name", "email", and "address", you can use the following SQL statement to insert a new row of data into the table:

> INSERT INTO customers (name, email, address) VALUES ('John Doe', 'johndoe@email.com', '123 Main St.');

- This statement inserts a new row into the "customers" table with values for the "name", "email", and "address" columns. The values are specified in the parentheses following the VALUES keyword and are separated by commas. Note that the values for text columns must be enclosed in single quotes.

You can also use the INSERT command to insert multiple rows of data at once by specifying multiple sets of values separated by commas, like this:

> INSERT INTO customers (name, email, address) VALUES ('John Doe', 'johndoe@email.com', '123 Main St.'), ('Jane Smith', 'janesmith@email.com', '456 Oak St.');

- This statement inserts two new rows into the "customers" table with values for the "name", "email", and "address" columns. Each set of values is enclosed in parentheses and separated by a comma.

###*Update*

- The UPDATE command is a SQL statement used to modify existing data in a table in a database. It is used to change the values of one or more columns in one or more rows of a table.

- To use the UPDATE command, you specify the name of the table you want to update, the columns you want to modify, and the new values you want to set for those columns. You can also use a WHERE clause to specify the rows you want to update based on specific criteria.

For example, if you have a "customers" table with columns for "name", "email", and "address", and you want to change the address for a customer with a specific email, you can use the following SQL statement:

> UPDATE customers SET address = '456 Oak St.' WHERE email = 'johndoe@email.com';

- This statement changes the value of the "address" column to "456 Oak St." for the row in the "customers" table where the value of the "email" column is "johndoe@email.com". The SET keyword is used to specify the column and the new value, and the WHERE clause is used to specify the row based on the criteria.

You can also update multiple columns at once by specifying multiple column and value pairs separated by commas, like this:

> UPDATE customers SET name = 'Jane Smith', address = '789 Elm St.' WHERE email = 'janesmith@email.com';

- This statement changes the values of the "name" and "address" columns for the row in the "customers" table where the value of the "email" column is "janesmith@email.com". The SET keyword is followed by multiple column and value pairs separated by commas, and the WHERE clause is used to specify the row based on the criteria.

###Delete

- The DELETE command is a SQL statement used to remove one or more rows of data from a table in a database. It is used to permanently delete data from a table.

- To use the DELETE command, you specify the name of the table you want to delete data from, and you can use a WHERE clause to specify the rows you want to delete based on specific criteria.

For example, if you have a "customers" table with columns for "name", "email", and "address", and you want to delete the row for a customer with a specific email, you can use the following SQL statement:

> DELETE FROM customers WHERE email = 'johndoe@email.com';

- This statement removes the row in the "customers" table where the value of the "email" column is "johndoe@email.com". The FROM keyword is used to specify the table to delete data from, and the WHERE clause is used to specify the row based on the criteria.

- If you omit the WHERE clause, the DELETE command will remove all the rows in the table, effectively deleting all the data in the table. Therefore, it is important to be careful when using the DELETE command and to make sure that you only delete the rows you intend to remove.

---

##**SQL Clauses**

###*Where*

- The WHERE clause is a SQL statement used to filter data based on specific criteria. It is used with SELECT, UPDATE, and DELETE statements to specify the rows that should be selected, updated, or deleted, respectively.

- When used with the SELECT statement, the WHERE clause allows you to retrieve only the rows that meet a certain condition. For example, if you have a "customers" table with columns for "name", "email", and "address", and you want to retrieve only the customers with a certain email address, you can use the following SQL statement:

> SELECT * FROM customers WHERE email = 'johndoe@email.com';

- This statement retrieves all the rows in the "customers" table where the value of the "email" column is "johndoe@email.com". The * symbol is used to specify all columns in the table should be returned.

- When used with the UPDATE statement, the WHERE clause allows you to modify only the rows that meet a certain condition. For example, if you want to update the address for a customer with a specific email, you can use the following SQL statement:

> UPDATE customers SET address = '456 Oak St.' WHERE email = 'johndoe@email.com';

- This statement changes the value of the "address" column to "456 Oak St." for the row in the "customers" table where the value of the "email" column is "johndoe@email.com".

When used with the DELETE statement, the WHERE clause allows you to delete only the rows that meet a certain condition. For example, if you want to delete the row for a customer with a specific email, you can use the following SQL statement:

>DELETE FROM customers WHERE email = 'johndoe@email.com';

- This statement removes the row in the "customers" table where the value of the "email" column is "johndoe@email.com".

###*Order by*
The ORDER BY clause is a SQL statement used to sort the result set of a SELECT statement in ascending or descending order based on one or more columns.

When you use the ORDER BY clause, you specify the column or columns to sort by, and whether to sort in ascending (ASC) or descending (DESC) order. For example, if you have a "customers" table with columns for "name", "email", and "address", and you want to retrieve all the customers in alphabetical order by name, you can use the following SQL statement:

SELECT * FROM customers ORDER BY name ASC;

This statement retrieves all the rows in the "customers" table and sorts them in ascending order based on the "name" column. The ASC keyword is used to specify ascending order. If you want to sort the rows in descending order, you can use the DESC keyword instead:

SELECT * FROM customers ORDER BY name DESC;

This statement retrieves all the rows in the "customers" table and sorts them in descending order based on the "name" column.

You can also sort by multiple columns at once by specifying multiple column names separated by commas. For example, if you want to sort the rows first by "name" in ascending order and then by "email" in descending order, you can use the following SQL statement:

SELECT * FROM customers ORDER BY name ASC, email DESC;

This statement retrieves all the rows in the "customers" table and sorts them in ascending order based on the "name" column, and then within each group of rows with the same "name", sorts them in descending order based on the "email" column.




###*Group by*
- The GROUP BY clause is a SQL statement used to group rows with the same values in one or more columns and perform calculations on those groups.

- When you use the GROUP BY clause, you specify one or more columns to group by. For example, if you have a "sales" table with columns for "product", "region", "month", and "amount", and you want to retrieve the total amount of sales for each product, you can use the following SQL statement:

> SELECT product, SUM(amount) FROM sales GROUP BY product;

- This statement retrieves all the distinct values of "product" from the "sales" table and groups the rows based on those values. Then, for each group, it calculates the sum of the "amount" column. The result set contains one row for each group, with the value of the "product" column and the total amount for that product.

You can also group by multiple columns at once by specifying multiple column names separated by commas. For example, if you want to retrieve the total amount of sales for each product and region, you can use the following SQL statement:

> SELECT product, region, SUM(amount) FROM sales GROUP BY product, region;

- This statement groups the rows based on the distinct values of "product" and "region" from the "sales" table. Then, for each group, it calculates the sum of the "amount" column. The result set contains one row for each combination of "product" and "region", with the values of those columns and the total amount for that combination.

- The GROUP BY clause is often used in conjunction with aggregate functions, such as SUM, COUNT, AVG, MAX, and MIN, to perform calculations on the groups of rows.

###*Limit*
- The LIMIT clause is a SQL statement used to limit the number of rows returned by a SELECT statement.

When you use the LIMIT clause, you specify the maximum number of rows to return. For example, if you have a "students" table with columns for "id", "name", "age", and "grade", and you want to retrieve the first 10 rows sorted by "grade" in descending order, you can use the following SQL statement:

> SELECT * FROM students ORDER BY grade DESC LIMIT 10;

- This statement retrieves all the rows in the "students" table, sorts them in descending order based on the "grade" column, and returns only the first 10 rows. The result set contains 10 rows, or fewer if the "students" table has fewer than 10 rows.

You can also use the LIMIT clause to retrieve a range of rows, starting from a specified offset. For example, if you want to retrieve the next 10 rows, starting from row number 11, you can use the following SQL statement:

> SELECT * FROM students ORDER BY grade DESC LIMIT 10 OFFSET 10;

- This statement retrieves all the rows in the "students" table, sorts them in descending order based on the "grade" column, skips the first 10 rows, and returns the next 10 rows. The result set contains 10 rows, or fewer if the "students" table has fewer than 20 rows.

- The LIMIT clause is supported by most relational databases, but the syntax may vary slightly between different database management systems.
---

##**Other SQL Commands**

###*Create table*

- The CREATE TABLE command is a SQL statement used to create a new table in a database.

- When you use the CREATE TABLE command, you specify the name of the table and the columns it will contain, along with their data types and any constraints on those columns. For example, if you want to create a "students" table with columns for "id", "name", "age", and "grade", you can use the following SQL statement:

>CREATE TABLE students (
id INT PRIMARY KEY,
name VARCHAR(50) NOT NULL,
age INT,
grade FLOAT
);

- This statement creates a new table named "students" with four columns: "id", "name", "age", and "grade". The "id" column is defined as an integer and marked as the primary key, which means that its values must be unique for each row. The "name" column is defined as a string with a maximum length of 50 characters and marked as NOT NULL, which means that it must have a value for each row. The "age" column is defined as an integer and can contain null values. The "grade" column is defined as a floating-point number and can also contain null values.

- You can also specify additional constraints on the columns, such as unique constraints, foreign key constraints, check constraints, and default values. The CREATE TABLE command allows you to create tables with complex structures and relationships between them, which is one of the key features of relational databases.
###*Alter table*

- The ALTER TABLE command is a SQL statement used to modify an existing table in a database.

- When you use the ALTER TABLE command, you can add, modify, or delete columns, as well as add or drop constraints. You can also rename the table itself, as well as rename individual columns.

For example, if you want to add a new column called "email" to the "students" table, you can use the following SQL statement:

> ALTER TABLE students ADD COLUMN email VARCHAR(100);

- This statement adds a new column to the "students" table, with a data type of VARCHAR(100), which means it can store up to 100 characters.

You can also modify an existing column, for example, to change its data type or add a constraint. For example, if you want to change the data type of the "age" column from INT to SMALLINT, you can use the following SQL statement:

> ALTER TABLE students ALTER COLUMN age TYPE SMALLINT;

- This statement modifies the "age" column in the "students" table to change its data type from INT to SMALLINT.

- Finally, you can use the ALTER TABLE command to drop columns or constraints, or to rename the table or columns. The ALTER TABLE command allows you to make changes to the structure of an existing table, which is important when you need to update or optimize your database schema.
###*Drop table*

- The DROP TABLE command is a SQL statement used to delete an existing table and all of its data from a database.

-When you use the DROP TABLE command, you specify the name of the table you want to delete. For example, if you want to delete the "students" table from your database, you can use the following SQL statement:

>DROP TABLE students;

- This statement deletes the "students" table and all of its data from the database.

- The DROP TABLE command is a powerful and potentially dangerous command, because it deletes all of the data in the table and removes the table definition from the database. Therefore, you should be careful when using this command, and make sure that you really want to delete the table before executing the command.

- In addition to the DROP TABLE command, there are other similar commands for deleting other database objects, such as indexes, views, and stored procedures. These commands typically have a similar syntax and usage to the DROP TABLE command.
