#ORDER-RELATED FUCNTIONS#

from csv_functions.csv_load import save_order_list
import pandas as pd

#FUNCTION: View orders with pandas
def view_orders_csv():
    print('Order information:')
    df = pd.read_csv('example_data\orders.csv')
    print(df.to_string())
    print() 

#FUNCTION: sort and view orders by csv
def sort_orders_csv():
    
    list_orders= ['Status', 'Courier', 'Original']
    list_options = ['0','1', '2']
    for index, value in enumerate(list_orders):
        print(index, value)
    
    while True:
        user_input = input('What key would you like to sort by?: ')

        if user_input == '0':
            df = pd.read_csv('orders.csv')
            df = df.sort_values(by=['order_status'])
            print(df.to_string())
            print()
            break  

        elif user_input == '1':
            df = pd.read_csv('orders.csv')
            df = df.sort_values(by=['courier_index'])
            print(df.to_string())
            print()
            break 

        elif user_input == '2':
            view_orders_csv()
            break

        elif user_input not in list_options:
            print('You have selected an invalid index number, please try again!')
            continue
        
#FUNCTION: create a new order to csv
def new_order_csv():

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
        view_couriers_csv()
        courier_add = input('Index of the courier you would like to attach to this order: ').title()
        new_orders['courier_index']= courier_add 

        #order status to preparing
        new_orders['order_status'] = 'Preparing'  

        #print products list with index values and get user input for what products they want
        print ("Product list index-value are : ")
        view_products_csv()
        
        product_index = []
        while True:
            user_input = input('What products would you like to add to this order? Type done to exit: ')
            if user_input == 'done':
                break
            else:
                product_index.append(user_input)
        prod_index_str = ','.join(str(item) for item in product_index)
        new_orders['product_index'] = prod_index_str     
        orders.append(new_orders)

        print('The current order list:')
        save_order_list()
        view_orders_csv()

    except (IndexError, ValueError):
        print('You have selected an invalid index number.')

    else: 
        print('You have successfully created an order!')

#FUNCTION: update the order status of a product to csv
def update_order_status_csv():
 
    try:
        print ("Order list index-values are : ")
        view_orders_csv()
        user_index = int(input('Index value of the order you wish to update: '))
        order_to_change = orders[user_index] 
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
        save_order_list()
        view_orders_csv()    

    except (IndexError, ValueError):
        print('You have selected an invalid index number.')

    else: 
        print('You have successfully updated this order status!')
        
#FUNCTION: update entire order to csv
def update_full_order_csv():
    
    try:
        view_orders_csv()
        user_index = int(input('Index value of the order you wish to change: '))    
        order_to_change = orders[user_index]
        
        for key, value in order_to_change.items():
            print(key, ':', value)
        
            user_input = input('What would you like to change the value to?: ')
            
            if user_input == '': 
                print('Property will not be updated')
            else:
                order_to_change[key] = user_input

        save_order_list()
        view_orders_csv()        
       
    except (IndexError, ValueError):
        print('You have selected an invalid index number.')

    else: 
        print('You have successfully updated this order!')

#FUNCTION: delete order to csv
def del_order_csv():
    
    try:
        view_orders_csv()
        user_index = int(input('Index vlaue of the product you wish to delete: '))    
        del orders[user_index]
        save_order_list()
        view_orders_csv() 

    except (IndexError, ValueError):
        print('You have selected an invalid index number.')

    else: 
        print('You have successfully deleted this order!')
