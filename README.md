# Cafe Management UI Via CLI

## Introduction

Client has a created a pop-up cafe within a busy business district. They offer a variety of products, with menu changes on a day to day basis. Although they only currently have one store, they want a way to log and track their transactions to support thier upscale.

## Project Background
Current SetUp:
- No data management system within the cafe
- Courier, customer, product and order data are stored together in Excel Notebook
- Time consuming process to add information
- Transactions do not adhere to ACID guidelines

User Story:
As an administrator of a cafe I would like to persist my courier, customer, order and product information so that I can monitor inventory and derive business metrics.

### Use Case
- Title: Cafe Data Management 
- Primary Actor: Administrator
- Success Scenario: 
1. Adminstrator uploads raw CSV files. 
2. CSV data is extracted, tranformed and persisted through both CSV and MySQL database (localhost). 
3. Through CLI, Adminstrator can CRUD products, orders, couriers and customers(db exclusive) through a menu system. 
4. UI is clear and intuitive. 
5. User's name, their action (i.e CRUD) and the specific date is logged.
6. SQL can be used on DB data to derive business insights.

## Code 
- Functional Programming (FP): src\functional 
- Object Orientated Programming (OOP): src\OOP

### OOP Class diagram

![ClassDiagram](https://user-images.githubusercontent.com/114569343/216828196-496b1ade-8390-418a-b021-4bf6cbb7b2c2.png)


## Testing
Unit testing with pythons' unittest module

## Start: CSV
1. cd src\OOP
2. py main.py
3. Select CSV Menu

## Start: DB
1. create .env file with mysql host, user, password and db name (example in docker\.env)
2. cd docker

3. To run MySQL/Adminer services:
- docker-compose up 
4. URL: http://localhost:8080/
5. Sign in with .env details and set up database tables
    - products: 
        columns: id(primary key: autoincrement), name, price
    - couriers:
        columns: id(primary key: autoincrement), phone, name
    - orders:
        columns: id, customer_name, customer_address, customer_phone, courier (foreign key: couriers.id), products(foreign key: products.id)

6. cd src\OOP
7. py main.py
8. Select DB Menu

