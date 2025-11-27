Open a new terminal and run the following commands:
-> 1.pip install flask
-> 2.pip install psycopg2-binary

create a new database called myduka_db:
-->

Prerequisites: -
SQL - sql queries (crud), pk & fk , joins , where
Python - data types, type conversion, data structures (lists & tuples) , loops, if , functions


PSYCOPG2 
-> A PostgresQL adapter (driver) used to connect Python to a Postgres database
-> Connects Postgres to your Python code

server, database, port ,username, password

**psycopg2.connect() - a function used to establish a connection between Python and Postgres
-> It has the following arguments:
**host** - where is my Postgres database located?
    host='localhost'
    localhost -> my own device / computer
**port** - where exaclty in my device is the Postgres service running?
        - default port of Postgres = 5432
**user** - username of the Postgres user - default user is => postgres
**password** - password attached to username to authenticate Postgres login
**dbname** - the database you want t connect to

**cur -> on object used to manipulate the database / perform db operation
cur.execute() -> a function used to execute the actual sql queries
cur.fetchall() -> fetches data from the query and gives it to Python