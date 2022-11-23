#PROGRAM: A menu system that allows user to view, create, amend and delete 
#the products, couriers and orders for a cafe 
#using either CSV files or a database


#Libraries
import csv
import pandas as pd
import pymysql
import os
from time import sleep
from dotenv import load_dotenv

from csv_functions import product_menu_csv, orders_menu_csv, couriers_menu_csv, load_product_data, load_courier_data,load_order_data

from db_functions import product_menu_db, order_menu_db, courier_menu_db, customer_menu_db


#FUNCTION: clear screen
def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
         os.system('cls')   


######DATABASE-RELATED FUNCTIONS######


#SET UP DB CONNECTION


# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# Establish a database connection
connection = pymysql.connect(
    host,
    user,
    password,
    database
)

cursor = connection.cursor()



#### MAIN MENU FUNCTION ####
  
def mainmenu():
    while True:
        sleep(2)
        clear_screen()
        print ('''Menu
        [0] Exit 
        [1] Main Menu: CSV
        [2] Main Menu: Database''')

        data_store_option = int(input("Please enter menu number: "))
        
        if data_store_option == 0:
            print('Exiting application')
            exit() 

        elif data_store_option == 1:

            print ('''Main menu
            [0] Return to Main Menu
            [1] Products
            [2] Couriers
            [3] Orders''')
    

            load_product_data()
            load_courier_data()
            load_order_data()

            user_input = int(input("Please enter menu number: "))
            
            if user_input == 0:
                continue

            elif user_input == 1:
                product_menu_csv()
                 
            elif user_input == 2:
                couriers_menu_csv()
                
            elif user_input == 3:
                orders_menu_csv()
                
            else:
                print('You have not entered a valid menu number, please try again')             

        elif data_store_option == 2:

            print ('''Main menu
            [0] Exit Database
            [1] Products
            [2] Couriers
            [3] Orders
            [4] Customers''')
            

            user_input = int(input("Please enter menu number: "))
            
            if user_input == 0:
                #exit database
                cursor.close()
                connection.close()
                print('You have successfully closed the connection to the database!')            

            elif user_input == 1:
                product_menu_db()

            elif user_input == 2:
                courier_menu_db()
                
            elif user_input == 3:
                order_menu_db()
            
            elif user_input == 4:
                customer_menu_db()           
    
            else:
                    print('You have not entered a valid menu number, please try again') 
        else:
            print('You have not entered a valid menu number, please try again')

if __name__ == "__main__":
    mainmenu()
