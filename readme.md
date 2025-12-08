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



                        OBJECT ORIENTED PROGRAMMING
--> We have the following broad categories of classifying data types:\
1.Inbuilt data types - data types that come with the programming language
    e.g. Python ---> int,float,str,bool,list,tuple,set,dict

2.User defined data types - are data types created by the programmer -enabled by the
use of classes and objects e.g. Person, Student, Car

**OOP** -A programming paradigm that builds programs around classes and objects
**Classes**
-->A blueprint or a template for creating objects
**Objects**
-->An instance of a class

--> A class has the following 2 things:
1.Attributes 
    ->Variables holding data in a class
    -> Answers the question : what does a class have?
    e.g. class Person - name, age, height, weight,marital_status, address etc
        class Car - engine, yom, make, model, colour etc
        class Laptop - width, ram, processors

2.Behaviour 
    -> Defined by methods
    -> Methods are simply functions inside classes
    ->Behaviour answers the question: what can a class do?
    e.g class Person - walk , talk, eat, sleep, work
        class Car - start, move, stop
        class Laptop - start,power off, code, send mail

**Methods** - functions inside classes
**Constructor** - a special method used to initialize objects
-> It is automatically called when an object is created
-> Python's constructor is __init__
** def __init__(self,parameters)
**Self** - refers the object itself
**parameters** -attributes of the class


OOP Task
1.Create a class called BankAccount with the following attributes:
 -account number
 -balance
 -owner name
 -date opened
2.Give the above BankAccount class the following behaviour or methods:
 -deposit()
 -withdraw()
 -display_info()
3.Create 2 BankAccount objects that can deposit, withdraw and display_info


**Inheritance**
-> This is the concept whereby one class (child) acquires / inherits / borrow properties from another class (parent)
-> It allows you to reuse code instead of rewriting everything from scratch

**Parent class** 
-> The class from which properties are inherited
-> also referred to as Base class / Super class
**Child class**
-> The class inheriting properties from another class
-> Also referred to as Derived class / Sub class

**Why use Inheritance?**
1.Avoids duplicated code
2.Adds new features to an existing class
3.Allows behaviour modification - method overriding

**Types of Inheritance**
1.Single Inheritance - a child class inherits from a single parent class
2.Multiple Inheritance - a child class inherits from more than one parent class
3.Multilevel Inheritance - a child class inherits from a parent and the parent also inherits 
from another class
4.Hierrachial Inheritance - multiple child classes from a single parent class


**Method Overriding**
-> This is where a child class provides its own implementation of a method that already exists in the parent class
-> The child's method replaces the parent's method when called by a child object
-> This is part of the POLYMORPHISM concept


OOP TASK 
1.Create a Car Class
Have the following attributes
- brand - model - year -fuel_capcity - fuel_level -is_running(boolen value)
Have the methods
- start()
- stop()
- refuel()
- drive()
- display_car_info()


2.Create a School system program using Python classes to demnstraate inheritance
-Create a parent class called Person with:
    attributes - name , age 
    method : display_info()

-> Create child classes that inherit the parent class:
       a)Student class with:
             -additional attributes - student_id, course
             -override display_info() to include student_id and course
       b)Teacher class with:
              -additional attributes - subject, salary
              -override display_info() to include subject and salary


**super()** - a keyword used by a child class to access methods and attributes from a parent class

**__str__** - a special method used to display objects in a user-friendly string form when a user tries to print the object directly
-> It is part of a broader class of methods called dunder (double underscore) methods which contain leading and trailing underscores to make the appear like in-built methods

**Inheritance**
**Polymorphism** --*method overriding + method overloading*
**Abstraction**
**Encapsulation**


FLASK 
Flask is a Python framework used to build web applications

**Understanding Frameworks vs Libraries**
Analogy : BUILDING A HOUSE

Scenario 1 ----> FRAMEWORK
Henry wants to build a house. Henry is not an expert in building or construction. Knowing this 
he enlists the help of construction experts (architect,engineer,pm,construction workers). These experts play a key role in building the house and make the process easier since they have more experience. But for this house to be built successfully to completion, Henry has to follow strict guidelines / rules as laid out by these experts e.g. materials needed 
Note ---> The process is easier but has very strict guidelines to be followed

Scenario 2 ----> LIBRARY
Peace wants to build a house. Peace is a construction expert and he decides he doesn't need the help of experts, he's going to build the house himself from scracth. He has to design and know and purchase all materials himself.Since he oversees the process himself , there is no strict guideline or timeline. 
Note ---> The process is hard but flexible

*Framework* - A prebuilt structure of code and tools used to help developers build applications
by not having to create them from scratch --- they easen development but have very strict guidelines on usage

Examples of frameworks:
Python --> Flask , FastAPI, Django 
JavaScript -> React, Angular , Vue, Svelte
Java -> Spring
C# -> .NET
Ruby -> Ruby on Rails
Go -> Gin
NodeJS -> Express

**FLASK**
1.ROUTING
--> A mechanism that maps / connects URLs to Python functions. It is a system for resource navigation  ---> Connects a URL to functions in your Flask app

**URL** - the full address that is used to access a web application
e.g.https://meet.google.com/dsh-idtb-oqb

*Parts of a URL*
1.Protocol - tells the browser how to communication
    ---> http (sends data as raw text)  && https (encryption of data)
2.Domain name - name of the website
3.Port (optional) -where exactly on a server is the app running
4.Path - the path to access a specific resource

**Routing in Flask**
--> To execute routing mechanisms in Flask we use a decorator function called @app.route()
*decorator function* -> a function that modifies or determines the behaviour of another function
@app.route() can take some parameters:
a)Rule / Path - the path to access a specific resource
b)Method

*view function* - function responsible for returning resources to the client

@app.route("/") ---> decorator function
def home():    ---> view function
    return "This is the index route" ---> resource / data to be accessed

**Index route** - the default landing route when an application is opened /accessed --> "/"

N/B:- **Every view function must have its own unique name**

**TASK**

1.Import get_sales() to main and display sales in your browser

2. Adjust your project structure to have the structure below:
MyDuka
->database.py ---> db connection
->main.py. ---> running Flask app
->static (folder) 
    **contains all static files - css, images , videos, icons , favicons
->templates (folder) -> contains all your html files
        *a single html file is called a template*
       -index.html
       -products.html
       -sales.html
       -dashboard.html
       -login.html
       -register.html


*Instead of returning raw data in our routes , we instead return / render full html pages and the subsequently render our
data in those pages
*To render /return html pages in Flask , we use a function called render_template() which is imported from Flask
*The render_template() function takes as an argument the name of a html file in string format
e.g. render_template("index.html")

**TEMPLATE INHERITANCE**
A mechanism of reducing redundancy in creating html files by having one base template which contains all common
html components e.g navbar , footer
-> Uses Jinja syntax
-> Create one base template -> base.html, layout.html
-> Have the other html files inherit common features from it

{% extends 'base.html' %} ---> inherit features from base template
{% block title  %} {% endblock %} ---> where to put my title for child templates
{% block content  %} {% endblock %} ---> block where you place each page's unique content

Task: - Apply template inheritance to the remaining html files 


Rendering Data to a Browser using Tables
Database -----> Python -----> Client (browser)

To render data with Flask we have to use Jinja

**Jinja**
-> A templating engine integrated with Flask to render dynamic html pages
-> A syntax inbuilt with Flask to render Python data

**Key features of Jinja**
1.When handling variables: --we use the following Jinja syntax :- {{}}
2.When using control structures: we use the following sytnax : {% %}
*Control Structures*
-> Are the building blocks that determine then flow and execution of a program
a)Sequence
-> A program will execute top to bottom, left to right
b)Selection
-> Allows a program to make decisions
-> Conditional statements --> if...else...
c)Repitition
--> A block of code can be executed repeatedly
--> Loops (for & while loop)

        {% for... %} ----> initialization


        {% endfor %} ----> termination 

        {% if ... %}


        {% endif %}