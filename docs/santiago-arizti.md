What is SQL
===========

_By Santiago Arizti_.

[Back to home](./)

Introduction
------------

Sql is...

Sql vs. Other Storage Solutions
-------------------------------

...

Sql Commands
------------

### The SELECT Statement

The `SELECT` statement is for...

Example:

```sql
select * from users;
```

### The INSERT Statement

...

### The UPDATE Statement

...

### The DELETE Statement

...

Sql Clauses
-----------

### The WHERE Clause

The `WHERE` clause...

Example:

```sql
SELECT name FROM users WHERE active=1;
```

### The ORDER BY Clause

...

### The GROUP BY Clause

...

### The LIMIT Clause

...

Other Sql Commands
------------------

### The CREATE TABLE Command

The `CREATE TABLE` command...

Example:

```sql
CREATE TABLE users (
    id int primary key,
    name varchar(255),
    active tinyint
)
```

### The ALTER TABLE Command

...

### The DROP TABLE Command

...
