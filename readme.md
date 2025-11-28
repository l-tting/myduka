Open a new terminal and run the following commands:
-> 1.pip install flask
-> 2.pip install psycopg2-binary

create a new database called myduka_db:
-->

Prerequisites: -
SQL - sql queries (crud), pk & fk , joins , where
Python - data types, type conversion, data structures (lists & tuples) , loops, if , functions


**Internet** - global network of connected devices or computers
**www** - a service running on the internet that connects users to the internet via the browser
**server** - a computer device used for receiving / sending data from a client
**hosting** - uploading application files to a server to make the application available or visible online

1.build your application
2.send your files to a server
3.ip address is assigned to your application

**ip address** -> a number used to uniquely identify a device on a network e.g. 170.100.82.80
**domain name** -> a user friendly name attached to an ip address to enable users access applications e.g. www.google.com , www.netflix.com

developer uploads app files to a server 
that server has an assigned ip address
now to access the app hosted on the server , we use the server ip address -> 

**DNS** - domain name system - the internet's phonebook used to translate domain names into ip addresses

127.0.0.1 -> the ip address of your device / computer
localhost -> domain name for 127.0.0.1


User Applications / Hardware <------>.   Drivers.   <------------> OS (KERNEL)
                                    (Keyboard driver)
                                    (Bluetooth driver)

Python code <--------> DB-API Interface <--------------> Drivers (psycopg2) <------------> DB (Postgres)


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
C - create - insert
R - Read - select
U -Update - Update
D - Delete - Delete
cur.fetchall() -> fetches data from the query and gives it to Python -> list of tuples

conn.commit() -updates the database with the new state

12-> products -> initial state
---> add 5 products
17.   ---> new state ---enabled by commit()


**Task**
1.Brush up on the following
-> sql queries, joins , where etc
-> python functions , data types, type conversion, loops , if statements , lists and tuples

2.research on another method apart from f-string to add products dynamically
----> hint --use=> %s

3.create two functions to do the following:
       -> insert 2 sales using psycopg2 -> insert_sales()
       -> view my sales data using psycopg2 -> get_sales()