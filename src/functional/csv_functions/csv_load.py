#### LOADING/SAVING CSV FILE ####

import csv


#FUNCTION: Loading data through csv
def load_product_data():
    # LOAD products from products.csv
    with open("example_data\products.csv", "r", newline = '') as file:
        product_file = csv.DictReader(file)
        for row in product_file:
            products.append(dict(row))
        file.close()    
                 
def load_courier_data():    
    # LOAD couriers from couriers.csv
    with open("example_data\couriers.csv", "r", newline = '') as file:
        courier_file = csv.DictReader(file)
        for row in courier_file:
            couriers.append(dict(row))       
        file.close() 

def load_order_data():            
    # LOAD orders from orders.csv
    with open("example_data\orders.csv", "r", newline = '') as file:
        order_file = csv.DictReader(file)
        for row in order_file:
            orders.append(dict(row))
        file.close() 


#FUNCTIONS: Save data to csv
def save_product_list():
    with open("example_data\products.csv", mode="w", newline = '') as file:
        w = csv.DictWriter(file, fieldnames = ['Product', 'Price'])
        w.writeheader()
        w.writerows(products) 
        file.close() 

def save_order_list():
    with open("example_data\orders.csv", "w", newline = '') as file:
        w = csv.DictWriter(file, fieldnames = ['customer_name', 'customer_address', 'customer_phone', 'courier_index', 'order_status', 'product_index'])
        w.writeheader()
        w.writerows(orders)
        file.close()   

def save_courier_list():
    with open("example_data\couriers.csv", "w", newline = '') as file:
        w = csv.DictWriter(file, fieldnames = ['Name', 'Phone'])
        w.writeheader()
        w.writerows(couriers)
        file.close()  

