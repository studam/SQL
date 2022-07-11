# SQL-challenge


What is SQLite and why use it?
SQLite is a dialect for using an SQL database. The syntax is very similar to the PostgreSQL syntax, with the main difference between the two being that SQLite is entirely serverless. SQLite allows for the power of database storage but with a tiny footprint. SQLite is also conveniently part of the standard Python library, so no additional setup is needed to get it up and running.
SQLite is not comparable with PostgreSQL or any other SQL language, rather it focuses on providing local data storage for individual applications.

What does ORM mean?
ORM stands for Object-Relational Mapper. Object-relational mapping allows us to write SQL queries using the object-oriented paradigm of the language with which you prefer to work. In other words, for our purposes in class, it allows us to interact with our database using Python.

How are classes relevant?
Python is an "Object-Oriented Programming (OOP) language", which means that it is highly concerned with organization and reusability. Classes are crucial to OOP in that they allow us to group related things and keep them together.
A class is essentially a template that allows us to create objects, which have variables and behaviors associated with them. It helps streamline our code and create efficiencies whenever something needs to be used various times.



Objectives:

Connect to a SQL database using SQLAlchemy.
Perform basic SQL queries using engine.execute().
Create Python classes and objects.
Create, read, update, and delete data from a SQL database using SQLAlchemy's ORM.
Reflect existing databases.
Use the SQLAlchemy ORM to create classes that model tables.
Use the ORM define relationships and foreign key constraints.
Use joins to query related data.
Use Flask to create and run a server.
Define endpoints using Flask's @app.route decorator.
Extract query variable path values from GET requests.
Use variable paths to execute database queries on behalf of the client.
Return JSONified query results from API endpoints.
