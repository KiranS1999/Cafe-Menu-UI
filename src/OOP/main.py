#PROGRAM: A menu system that allows user to view, create, amend and delete 
#the products, couriers and orders for a cafe using either CSV files or a MySQL database

from csv_functions.csv_main import MenuCSV
from db_functions.db_main import MenuDB
from time import sleep
import os

#FUNCTION: clear screen
def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
         os.system('cls')   


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
    

            user_input = int(input("Please enter menu number: "))
            
            if user_input == 0:
                continue

            elif user_input == 1:
                MenuCSV.product_menu_csv()
                 
            elif user_input == 2:
                MenuCSV.couriers_menu_csv()
                
            elif user_input == 3:
                MenuCSV.orders_menu_csv()
                
            else:
                print('You have not entered a valid menu number, please try again')             

        elif data_store_option == 2:

            print ('''Main menu
            [0] Return to Mani Menu
            [1] Products
            [2] Couriers
            [3] Orders
            [4] Customers''')
            

            user_input = int(input("Please enter menu number: "))
            
            if user_input == 0:
                continue

            elif user_input == 1:
                MenuDB.product_menu_db()

            elif user_input == 2:
                MenuDB.courier_menu_db()
                
            elif user_input == 3:
                MenuDB.order_menu_db()
            
            elif user_input == 4:
                MenuDB.customer_menu_db()           
    
            else:
                    print('You have not entered a valid menu number, please try again') 
        else:
            print('You have not entered a valid menu number, please try again')

if __name__ == "__main__": 
    mainmenu()
