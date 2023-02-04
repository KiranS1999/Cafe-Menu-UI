#DATABASE specifc functions referenced in current_project.py, cafe project

#import libraries
import pymysql
import os
from time import sleep
from dotenv import load_dotenv
from db_functions.db_orders import view_orders, sort_orders, new_order, update_order_status, update_full_order, del_order  
from db_functions.db_customers import view_customer_list, update_customer_list, delete_customer_list
from db_functions.db_couriers import view_couriers, new_courier, update_courier, del_courier
from db_functions.db_products import view_products, create_product, update_product, delete_product, track_prod_inventory

#### MAIN PRODUCT MENU FUNCTION ####
def product_menu_db():
    while True:
        print('''Product Menu:
                [0] Return to main menu
                [1] View products
                [2] Create a new product
                [3] Update a product
                [4] Delete a product
                [5] Track product inventory''')
                
        x = int(input("Please enter menu number: "))
        
        if x == 0:
            break
        
        elif x == 1: 
        #view products    
            view_products()
            continue
        
        elif x == 2:
        #create a new product    
            create_product()
            continue
        
        elif x == 3:
        #update an existing product    
            update_product()
            continue
        
        elif x == 4:
        #delete a product    
            delete_product()
            continue

        elif x == 5:
            track_prod_inventory()
            continue    
        
        else:
            print('You have not entered a valid sub-menu number, please try again')
            continue 

#### MAIN COURIER MENU FUNCTION ####
def courier_menu_db():
    while True:
        print('''Courier Menu:
                    [0] Return to main menu
                    [1] View couriers
                    [2] Create a new courier
                    [3] Update existing courier
                    [4] Delete courier
                ''')

        x = int(input("Please enter menu number: "))

        if x == 0:
            break

        elif x == 1:
            #View couriers
            view_couriers()
            continue

        elif x == 2:
            #create a new courier
            new_courier()
            continue
        
        elif x == 3:
            #update exisitng courier
            update_courier()
            continue
            
        elif x == 4:
            #delete a courier
            del_courier()
            continue

        else:
            print('You have not entered a valid sub-menu number, please try again')
            continue

#### MAIN ORDER MENU FUNCTION ####            
def order_menu_db():
    while True:
        print('''Order Menu:
                    [0] Return to main menu
                    [1] Sort and View orders
                    [2] Create a new order
                    [3] Update order status
                    [4] Update existing order
                    [5] Delete an order''')

        x = int(input("Please enter menu number: "))

        if x == 0:
            break

        elif x == 1:
            #view and sort orders
            sort_orders()  
            continue

        elif x == 2:
            #create a new order
            new_order()
            continue

        elif x == 3:
            #update order status                    
            update_order_status()
            continue

        elif x == 4:
            #update an existing order
            update_full_order()
            continue      

        elif x==5:
            #delete an existing order
            del_order()
            continue

        else:
            print('You have not entered a valid sub-menu number, please try again')
            continue

#### MAIN CUSTOMER MENU FUNCTION ####
def customer_menu_db():    
    while True:
        print('''Customer Menu:
                    [0] Return to main menu
                    [1] View customers
                    [2] Update customers
                    [3] Delete customers
                    ''')
        x = int(input("Please enter menu number: "))

        if x == 0:
            break
        
        elif x == 1:
            #view customers
            view_customer_list()
            continue

        elif x == 2:
            #update customers
            update_customer_list()
            continue

        elif x == 3:
            #delete customers
            delete_customer_list()
            continue
        
        else:
            print('You have not entered a valid sub-menu number, please try again')
            continue                    
    
