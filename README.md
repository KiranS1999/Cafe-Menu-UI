# Cafe Management UI Via CLI

## INTRODUCTION

Current SetUp:
- No data management system within the cafe
- Courier, customer, product and order data are stored together in Excel Notebook
- Time consuming process to add information
- Transactions do not adhere to ACID guidelines

As an administrator of a cafe I would like to manage my courier, customer, order and product information so that I can monitor inventory and derive business metrics.

### Use Case
Title: Cafe Data Management
Primary Actor: Administrator
Success Scenario: Adminstrator uploads raw CSV files. CSV data is extracted, tranformed and persisted through both CSV and MySQL database (localhost). Through CLI, Adminstrator can CRUD products, orders, couriers and customers(db exclusive) through a menu system. UI is clear and intuitive. SQL can be used on db data to derive business insights.

## Code Diagram



## Testing
Unit testing with unittest module


