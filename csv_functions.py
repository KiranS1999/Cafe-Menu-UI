#CSV specific fucntions referenced in current_project.py, cafe project


#import libraries
import csv
import pandas as pd

#empty list of orders,products and couriers to be written to a csv file
orders = []
products = [] 
couriers = []


#### LOADING/SAVING CSV FILE ####

#FUNCTION: Loading data through csv
def load_product_data():
    # LOAD products from products.csv
    with open("products.csv", "r", newline = '') as file:
        product_file = csv.DictReader(file)
        for row in product_file:
            products.append(dict(row))
        file.close()    
                 
def load_courier_data():    
    # LOAD couriers from couriers.csv
    with open("couriers.csv", "r", newline = '') as file:
        courier_file = csv.DictReader(file)
        for row in courier_file:
            couriers.append(dict(row))       
        file.close() 

def load_order_data():            
    # LOAD orders from orders.csv
    with open("orders.csv", "r", newline = '') as file:
        order_file = csv.DictReader(file)
        for row in order_file:
            orders.append(dict(row))
        file.close() 


#FUNCTIONS: Save data to csv
def save_product_list():
    with open("products.csv", mode="w", newline = '') as file:
        w = csv.DictWriter(file, fieldnames = ['Product', 'Price'])
        w.writeheader()
        w.writerows(products) 
        file.close() 

def save_order_list():
    with open("orders.csv", "w", newline = '') as file:
        w = csv.DictWriter(file, fieldnames = ['customer_name', 'customer_address', 'customer_phone', 'courier_index', 'order_status', 'product_index'])
        w.writeheader()
        w.writerows(orders)
        file.close()   

def save_courier_list():
    with open("couriers.csv", "w", newline = '') as file:
        w = csv.DictWriter(file, fieldnames = ['Name', 'Phone'])
        w.writeheader()
        w.writerows(couriers)
        file.close()  





#PRODUCT-RELATED FUNCTIONS#

#FUNCTION: View products with pandas
def view_products_csv():
    print('Product information:')
    df = pd.read_csv('products.csv')
    print(df.to_string()) 
    print()

#FUNCTION: create a new product to csv
def create_product_csv():
    newprod = input('Please enter your product name: ').title()
    newprice = input('Please enter the price: ')
    new_prod_dict = {'Product': newprod, 'Price': newprice}
    products.append(new_prod_dict)
    save_product_list()
    view_products_csv()
    
#FUNCTION: update a product to csv
def update_product_csv():
    
    try:
        view_products_csv()
        user_index = int(input('Index value of the product you wish to update: '))
        product_to_change = products[user_index]
        for key, value in product_to_change.items():
            print(key, ':', value)

        product_new = input('What is the new product name?: ').title()  
        price_new = input('What is the new price?: ')

        if product_new == '': 
            print('Product name will not be updated')
        else:
            product_to_change['Product'] = product_new

        if price_new == '': 
            print('Price will not be updated')
        else:
            product_to_change['Price'] = price_new    
        
        save_product_list()
        view_products_csv()
        
    
    except (IndexError, ValueError):
        print('You have selected an invalid index number.') 

    else:
        print('You have successfully updated this product!')    
 
#FUNCTION: delete a product to csv #check
def delete_product_csv():
         
    try:
        view_products_csv()
        user_index = int(input('Index value of the product you wish to delete: '))    
        del products[user_index]
        save_product_list()
        view_products_csv()
           

    except (IndexError, ValueError):
        print('You have selected an invalid index number.')        

    else:
        print('You have successfully deleted this product!')    
        
    
                     

#COURIER-RELATED FUNCTIONS#

#FUNCTION: View couriers with pandas
def view_couriers_csv():
    print('Courier information:')
    df = pd.read_csv('couriers.csv')
    print(df.to_string())
    print() 

#FUNCTION: create a new courier to csv
def new_courier_csv():
    new_courier = input('What is the name of the new courier?: ').title()
    new_phone = input('Please enter their phone number: ')
    new_courier_dict = {'Name': new_courier, 'Phone': new_phone}
    couriers.append(new_courier_dict)
    print('The current courier list:')
    save_courier_list()
    view_couriers_csv()
       
#FUNCTION: update a courier to csv
def update_courier_csv():

    try:
        view_couriers_csv()
        user_index = int(input('Index value of the product you wish to update: ')) 
        courier_to_change = couriers[user_index]
        for key, value in courier_to_change.items():
            print(key, ':', value)

        courier_new = input('What is the new courier name?: ').title()  
        phone_new = input('What is the new phone number?: ')

        if courier_new == '': 
            print('Name will not be updated')
        else:
            courier_to_change['Name'] = courier_new

        if phone_new == '': 
            print('Phone number will not be updated')
        else:
            courier_to_change['Phone'] = phone_new    

        save_courier_list()
        view_couriers_csv()
        

    except (IndexError, ValueError):
        print('You have selected an invalid index number.')

    else: 
        print('You have successfully updated this courier!')     
      
#FUNCTION: delete a courier to csv
def del_courier_csv():  

    try:
        view_couriers_csv()
        user_index = int(input('Index value of the courier you wish to delete: '))    
        del couriers[user_index]
        save_courier_list()
        view_couriers_csv()
               
    
    except (IndexError, ValueError):
        print('You have selected an invalid index number.') 

    else:
        print('You have successfully deleted this courier!')    
  



#ORDER-RELATED FUCNTIONS#

#FUNCTION: View orders with pandas
def view_orders_csv():
    print('Order information:')
    df = pd.read_csv('orders.csv')
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