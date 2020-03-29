# Learning Cassandra
```

CREATE KEYSPACE FirstKeySpace WITH REPLICATION = { 'class':'SimpleStrategy', 'replication_factor': '1' };

DESCRIBE keyspaces;

USE FirstKeySpace;

CREATE TABLE emp (
emp_id int,
emp_name text,
emp_age int,
PRIMARY KEY((emp_id)));

DESCRIBE Table emp;

INSERT INTO emp (emp_id, emp_name, emp_age)  VALUES(20, 'Mike', 30);
INSERT INTO emp (emp_id, emp_name, emp_age)  VALUES(10, 'John', 28);

SELECT * FROM emp;

UPDATE emp SET emp_age=40 WHERE emp_id=10;

SELECT * FROM emp where emp_id=10; // where clause can be used only on the columns that are part of a primary key or have a secondarty index on them)


DELETE FROM emp where emp_id=10;

truncate table emp; // delete all rwowsDROP

DROP keyspace FirstKeySpace;
DESCRIBE keyspace;




```
