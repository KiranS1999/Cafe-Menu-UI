#CSV specific fucntions referenced in current_project.py, cafe project


#import libraries
import csv
import pandas as pd
from csv_functions.csv_orders import  sort_orders_csv, new_order_csv, update_order_status_csv, update_full_order_csv, del_order_csv
from csv_functions.csv_products import view_products_csv, create_product_csv, update_product_csv, delete_product_csv
from csv_functions.csv_couriers import view_couriers_csv, new_courier_csv, update_courier_csv, del_courier_csv



#### MAIN PRODUCT CSV MENU ####
def product_menu_csv():

    while True:
        print('''Product Menu:
        [0] Return to main menu
        [1] View products
        [2] Create a new product
        [3] Update a product
        [4] Delete a product''')
        
        

        x = int(input("Please enter menu number: "))
        
        if x == 0:
            break
        
        elif x == 1: 
        #view products    
            view_products_csv()
            continue
            
        
        elif x == 2:
        #create a new product    
            create_product_csv()
            continue
    
        
        elif x == 3:
        #update an existing product    
            update_product_csv()
            continue
            
        
        elif x == 4:
        #delete a product    
            delete_product_csv()
            continue
                
        else:
            print('You have not entered a valid sub-menu number, please try again')
            continue 

#### MAIN COURIERS CSV MENU ####
def couriers_menu_csv():

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
            #view couriers
            view_couriers_csv()
            continue

        elif x == 2:
            #create a new courier
            new_courier_csv()
            continue
        
        elif x == 3:
            #update exisitng courier
            update_courier_csv()
            continue
            
        elif x == 4:
            #delete a courier
            del_courier_csv()
            continue
        
        else:
            print('You have not entered a valid sub-menu number, please try again')
            continue  

#### MAIN ORDERS CSV MENU ####
def orders_menu_csv():

    while True:    
        print('''Order Menu:
            [0] Return to main menu
            [1] View and Sort orders
            [2] Create a new order
            [3] Update order status
            [4] Update existing order
            [5] Delete an order''')

        x = int(input("Please enter menu number: "))

        if x == 0:
            break

        elif x == 1:
            #view and sort orders
            sort_orders_csv()              
            continue

        elif x == 2:
            #create a new order
            new_order_csv()
            continue

        elif x == 3:
            #update order status                    
            update_order_status_csv()
            continue

        elif x == 4:
            #update an existing order
            update_full_order_csv()
            continue        

        elif x==5:
            #delete an existing order
            del_order_csv()
            continue
        
        else:
            print('You have not entered a valid sub-menu number, please try again')
            continue 