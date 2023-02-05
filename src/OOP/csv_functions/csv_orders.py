#ORDER-RELATED FUCNTIONS#

import pandas as pd 
from datetime import date
from csv_products import ProductMenu
from csv_load import SaveLoad
    

class OrderLog:
    def __init__(self):
        '''Initialise the user log info

        '''
        self.name = input('Please enter your name: ')
        self.date = self.current_date()
        self.action = '*No Action*'

    def update_order__status_log(self, order: str, new_status: str):
        '''Log updated order status
        Arg:
            order: order info 
            old_status: previous order status
            new_status: new status of order'''  
        self.action = f"Updated an order status: Order:{order}, New Status: {new_status}"

    def update_order_log(self, order_changed: str):
        '''Log affected order 
        Arg:
            order: order info '''  
        self.action = f"Updated this order:{order_changed}"

    def create_order_log(self, customer_name, customer_address, customer_phone, courier_add, prod_index_str ):
        '''Log order creation'''
        self.action = f"Created a new order, Name:{customer_name}, Address:{customer_address}, Phone Number:{customer_phone}, Courier Index:{courier_add}, Product Index/Indices:{prod_index_str} "

    def delete_order_log(self, order: str):
        '''Log order deletion'''
        self.action = f"Deleted {order}"
   
    def current_date(self):
        today = str(date.today())
        return today   

    def useraccess(self):
        return f"\n{self.name} {self.action} at {self.date}"

    def writelog(self):
        with open("log.txt", "a") as file:
            log = self.useraccess()
            file.write(log)
            print('Successfully logged action!')


class OrderMenu(OrderLog, SaveLoad):
    '''Class OrderMenu implements a order menu with a functionality to CRUD orders
        and save changes to a CSV'''
    def __init__(self, filename: str):
        OrderLog.__init__(self)
        SaveLoad.__init__(self, filename)
        self.order_list = []
        self.load_data()

    def load_data(self):
        return super().load_data(info_type = self.order_list)

    def save_data(self):
        return super().save_data(fieldnames = ['customer_name', 'customer_address', 'customer_phone', 'courier_index', 'order_status', 'product_index'], info_type = self.order_list )    

    def view_order(self):
        '''Display orders that have been loaded
        Returns:
            dataframe of current orders'''
        
        print('Order information:')
        try:
            df = pd.read_csv(self.filename)
            print(df.to_string())
        except Exception as e:
            print(f"Error: {e}")
            raise Exception

    def sort_orders_csv(self):

        list_orders= ['Status', 'Courier', 'Original']
        list_options = ['0','1', '2']
        for index, value in enumerate(list_orders):
            print(index, value)
        
        while True:
            user_input = input('What key would you like to sort by?: ')

            if user_input == '0':
                df = pd.read_csv(self.filename)
                df = df.sort_values(by=['order_status'])
                print(df.to_string())
                print()
                break  

            elif user_input == '1':
                df = pd.read_csv(self.filename)
                df = df.sort_values(by=['courier_index'])
                print(df.to_string())
                print()
                break 

            elif user_input == '2':
                df = pd.read_csv(self.filename)
                print(df.to_string())
                break

            elif user_input not in list_options:
                print('You have selected an invalid index number, please try again!')
                continue

    def create_order(self):
        '''User input to create a new order
        Returns: 
        Boolean value indicating if order has been successfully added or not'''
        
        try:
            new_orders = {}
            customer_name = input('Please type the customer name: ').title()
            new_orders['customer_name'] = customer_name
            customer_address = input('Please type the customer address: ').title()
            new_orders['customer_address'] = customer_address
            customer_phone = input('Please type the customer phone number: ')
            new_orders['customer_phone'] = customer_phone
            

            #add courier to the order 
            print ("Courier list index-value are : ")  
            self.view_order()
            courier_add = input('Index of the courier you would like to attach to this order: ').title()
            new_orders['courier_index']= courier_add 

            #order status to preparing
            new_orders['order_status'] = 'Preparing'  

            #print products list with index values and get user input for what products they want
            print ("Product list index-value are : ")
            ProductMenu.view_products()
            
            product_index = []
            while True:
                user_input = input('What products would you like to add to this order? Type done to exit: ')
                if user_input == 'done':
                    break
                else:
                    product_index.append(user_input)
            prod_index_str = ','.join(str(item) for item in product_index)
            new_orders['product_index'] = prod_index_str     
            self.order_list.append(new_orders)

        except (IndexError, ValueError):
            print('You have selected an invalid index number.')
            return False
        else: 
            print('You have successfully created an order!')
            super().create_order_log(customer_name, customer_address, customer_phone, courier_add, prod_index_str )
            return True       

    def update_order_status(self):
        '''Updates existing orders status
        
        Returns:
        
        Boolean value indicating if orders' status has been successfully updated
        '''
        try:
            print ("Order list index-values are : ")
            self.view_order()
            user_index = int(input('Index value of the order you wish to update: '))
            order_to_change = self.order_list[user_index] 
            for key, value in order_to_change.items():
                print(key, ':', value)
            
            order_status_list = ['Preparing', 'Ready for dispatch', 'Delivered', 'Arrived']
            
            print('Order status options:')
            for index, value in enumerate(order_status_list):
                print(index, value)
            
            new_status = int(input('What is the new order status?(Type 0-3): '))
            updated_status = order_status_list[new_status]
            order_to_change.update({'order_status': updated_status})
            
            print('The current order list:')    
            self.view_order()

        except (IndexError, ValueError):
            print('You have selected an invalid index number.')
            return False
        else: 
            super().update_order_status_log(order_to_change, updated_status )
            print('You have successfully updated this order status!')
            return True   

    def update_order(self):
        '''Updates each value of existing order
        
        Returns:
        
        Boolean value indicating if orders' status has been successfully updated
        '''
        try:
            self.view_order()
            user_index = int(input('Index value of the order you wish to change: '))    
            order_to_change = self.order_list[user_index]
            
            for key, value in order_to_change.items():
                print(key, ':', value)
            
                user_input = input('What would you like to change the value to?: ')
                
                if user_input == '': 
                    print('Property will not be updated')
                else:
                    order_to_change[key] = user_input      
        
        except (IndexError, ValueError):
            print('You have selected an invalid index number.')
            return False
        else: 
            super().update_order_log(order_to_change)
            print('You have successfully updated this order!')
            return True
            
    def delete_order(self):
        try:
            self.view_order()
            user_index = int(input('Index value of the product you wish to delete: '))    
            del self.order_list[user_index] 

        except (IndexError, ValueError):
            print('You have selected an invalid index number.')
            return False
        else: 
            super().delete_order_log(self.order_list[user_index])
            print('You have successfully deleted this order!')
            return True    
            


