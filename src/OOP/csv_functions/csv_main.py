#CSV specific fucntions referenced in current_project.py, cafe project


#import libraries
from csv_orders import OrderMenu
from csv_couriers import CourierMenu
from csv_products import ProductMenu




#### MAIN PRODUCT CSV MENU ####
class MenuCSV:

    def __init__(self):
        '''Initialise the CSV Menu Object'''

        self.products = ProductMenu()
        self.couriers = CourierMenu()
        self.orders = OrderMenu()

    def main_csv(self):
        
        while True:
            print ('''Main menu
            [0] Return to Main Menu
            [1] Products
            [2] Couriers
            [3] Orders''')

            user_input = int(input("Please enter menu number: "))
            
            if user_input == 0:
                continue

            elif user_input == 1:
                self.product_menu_csv()
                 
            elif user_input == 2:
                self.couriers_menu_csv()
                
            elif user_input == 3:
                self.orders_menu_csv()
                
            else:
                print('You have not entered a valid menu number, please try again')             

    def product_menu_csv(sself):

        while True:
            print('''Product Menu: 
            [0] Return to main menu
            [1] View products
            [2] Create a new product
            [3] Update a product
            [4] Delete a product''')
        
            x = int(input("Please enter menu number: "))
            
            if x == 0:
                print('Exiting Products Menu')
                break
            
            elif x == 1: 
            #view products    
                ProductMenu.view_products()
                continue
        
            elif x == 2:
            #create a new product    
                ProductMenu.create_product()
                continue
            
            elif x == 3:
            #update an existing product    
                ProductMenu.update_product()
                continue
            
            elif x == 4:
            #delete a product    
                ProductMenu.delete_product()
                continue
                    
            else:
                print('You have not entered a valid sub-menu number, please try again')
                continue 

    #### MAIN COURIERS CSV MENU ####
    def couriers_menu_csv(self):

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
                CourierMenu.view_courier()
                continue

            elif x == 2:
                #create a new courier
                CourierMenu.create_couriers()
                continue
            
            elif x == 3:
                #update exisitng courier
                CourierMenu.update_couriers()
                continue
                
            elif x == 4:
                #delete a courier
                CourierMenu.delete_couriers()
                continue
            
            else:
                print('You have not entered a valid sub-menu number, please try again')
                continue  

    #### MAIN ORDERS CSV MENU ####
    def orders_menu_csv(self):

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
                OrderMenu.sort_orders_csv()             
                continue

            elif x == 2:
                #create a new order
                OrderMenu.create_order()
                continue

            elif x == 3:
                #update order status                    
                OrderMenu.update_order_status()
                continue

            elif x == 4:
                #update an existing order
                OrderMenu.update_order()
                continue        

            elif x==5:
                #delete an existing order
                OrderMenu.delete_order()
                continue
            
            else:
                print('You have not entered a valid sub-menu number, please try again')
                continue 