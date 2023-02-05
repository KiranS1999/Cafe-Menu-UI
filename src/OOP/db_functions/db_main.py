#DATABASE specifc functions referenced in current_project.py, cafe project

#import libraries
from db_orders import OrderDB
from db_couriers import CourierDB
from db_products import ProductDB
from db_customers import CustomerDB


class MenuDB:

    def product_menu_db():
        '''
        Product Menu loop for DB option
        '''

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
                ProductDB.view_products()
                continue
            
            elif x == 2:
            #create a new product    
                ProductDB.create_product()
                continue
            
            elif x == 3:
            #update an existing product    
                ProductDB.update_product()
                continue
            
            elif x == 4:
            #delete a product    
                ProductDB.delete_product()
                continue

            elif x == 5:
                ProductDB.track_prod_inventory()
                continue    
            
            else:
                print('You have not entered a valid sub-menu number, please try again')
                continue 

    def courier_menu_db():
        '''
        Courier Menu loop for DB option
        '''

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
                CourierDB.view_couriers()
                continue

            elif x == 2:
                #create a new courier
                CourierDB.new_courier()
                continue
            
            elif x == 3:
                #update exisitng courier
                CourierDB.update_courier()
                continue
                
            elif x == 4:
                #delete a courier
                CourierDB.del_courier()
                continue

            else:
                print('You have not entered a valid sub-menu number, please try again')
                continue
        
    def order_menu_db():
        '''
        Order Menu loop for DB option
        '''

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
                OrderDB.sort_orders()  
                continue

            elif x == 2:
                #create a new order
                OrderDB.new_order()
                continue

            elif x == 3:
                #update order status                    
                OrderDB.update_order_status()
                continue

            elif x == 4:
                #update an existing order
                OrderDB.update_full_order()
                continue      

            elif x==5:
                #delete an existing order
                OrderDB.del_order()
                continue

            else:
                print('You have not entered a valid sub-menu number, please try again')
                continue

    def customer_menu_db(): 
        '''
        Customer Menu loop for DB option
        '''   

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
                CustomerDB.view_customer_list()
                continue

            elif x == 2:
                #update customers
                CustomerDB.update_customer_list()
                continue

            elif x == 3:
                #delete customers
                CustomerDB.delete_customer_list()
                continue
            
            else:
                print('You have not entered a valid sub-menu number, please try again')
                continue                    
        
