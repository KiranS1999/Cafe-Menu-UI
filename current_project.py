#PROGRAM: A menu system that allows user to view, create, amend and delete 
#the products, couriers and orders for a cafe 
#using either CSV files or a database


#Libraries
import csv
import pandas as pd
import pymysql
import os
from dotenv import load_dotenv



######CSV-RELATED FUNCTIONS######

#empty list of orders,products and couriers to be written to a csv file
orders = []
products = [] 
couriers = []


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
    df = pd.read_csv('products.csv')
    print(df.to_string()) 

#FUNCTION: create a new product to csv
def create_product_csv():
    newprod = input('Please enter your new product name: ')
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

        product_new = input('What is the new product name?: ')  
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
    
    except IndexError:
        print('You have selected an unavailable index, please try again')
    except ValueError:
        print('You have not entered a valid index, please try again!') 
 
#FUNCTION: delete a product to csv
def delete_product_csv():
         
    try:
        view_products_csv()
        user_index = int(input('Please type the index value of the product you wish to delete: '))    
        del products[user_index]
        save_product_list()
        view_products_csv()   

    except IndexError:
        print('You have selected an unavailable index, please try again')
        
    except ValueError:
        print('You have not entered a valid index, please try again!')
        
    
                     


#COURIER-RELATED FUNCTIONS#

#FUNCTION: View couriers with pandas
def view_couriers_csv():
    df = pd.read_csv('couriers.csv')
    print(df.to_string()) 

#FUNCTION: create a new courier to csv
def new_courier_csv():
    new_courier = input('What is the name of the new courier?: ')
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

        courier_new = input('What is the new courier name?: ')  
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

    except IndexError:
        print('You have selected an unavailable index, please try again')    
    except ValueError:
        print('You have not entered a valid index, please try again!') 
        
#FUNCTION: delete a courier to csv
def del_courier_csv():  

    try:
        view_couriers_csv()
        user_index = int(input('Please type the index value of the courier you wish to delete: '))    
        del couriers[user_index]
        save_courier_list()
        view_couriers_csv()         
    
    except IndexError as e:
        print('You have selected an unavailable index, please try again')      
    except ValueError as v:
        print('You have not entered a valid index, please try again!')
    
  





#ORDER-RELATED FUCNTIONS#

#FUNCTION: View orders with pandas
def view_orders_csv():
    df = pd.read_csv('orders.csv')
    print(df.to_string()) 

#FUNCTION: sort and view orders by csv
def sort_orders_csv():
    
    try: 
        list_orders= ['Status', 'Courier', 'Original']

        for index, value in enumerate(list_orders):
            print(index, value)

        user_input = input('What key would you like to sort by?: ')

        if user_input == '0':
            df = pd.read_csv('orders.csv')
            df = df.sort_values(by=['order_status'])
            print(df.to_string())  

        elif user_input == '1':
            df = pd.read_csv('orders.csv')
            df = df.sort_values(by=['courier_index'])
            print(df.to_string()) 

        elif user_input == '2':
            view_orders_csv()

    except IndexError as e:
        print('You have selected an unavailable index, please try again')      
    except ValueError as v:
        print('You have not entered a valid index, please try again!')     

#FUNCTION: create a new order to csv
def new_order_csv():

    try:
        new_orders = {}
        customer_name = input('Please type the customer name: ')
        new_orders['customer_name'] = customer_name
        customer_address = input('Please type the customer address: ')
        new_orders['customer_address'] = customer_address
        customer_phone = input('Please type the customer phone number: ')
        new_orders['customer_phone'] = customer_phone
        

        #add courier to the order 
        print ("Courier list index-value are : ")  
        view_couriers_csv()
        courier_add = input('Please type the index of the courier you would like to attach to this order: ')
        new_orders['courier_index']= courier_add 

        #order status to preparing
        new_orders['order_status'] = 'preparing'  

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

    except IndexError as e:
        print('You have selected an unavailable index, please try again')      
    except ValueError as v:
        print('You have not entered a valid index, please try again!')

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

    except IndexError:
        print('You have selected an unavailable index, please try again')
    except ValueError:
        print('You have not entered a valid index, please try again!')
        
#FUNCTION: update entire order to csv
def update_full_order_csv():
    
    try:
        view_orders_csv()
        user_index = int(input('Please type the index value of the order you wish to change: '))    
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
       
    except IndexError:
        print('You have selected an unavailable index, please try again')        
    except ValueError:
        print('You have not entered a valid index, please try again!')
       
#FUNCTION: delete order to csv
def del_order_csv():
    
    try:
        view_orders_csv()
        user_index = int(input('Please type the index vlaue of the product you wish to delete: '))    
        del orders[user_index]
        save_order_list()
        view_orders_csv() 

    except IndexError as e:
        print('You have selected an unavailable index, please try again')
    except ValueError as v:
        print('You have not entered a number, please try again!')







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




#PRODUCT-RELATED FUNCTIONS

#FUNCTION: view all products
def view_products():
    cursor.execute('SELECT * FROM products')
    rows = cursor.fetchall()
    for row in rows:
        print(f'Name: {str(row[1])}, Price: {row[2]}')

#FUNCTION: create a new product
def create_product ():
    newprod = input('Please enter your new product name: ')
    newprice = input('Please enter the price: ')
    sql = "INSERT INTO products (name, price) VALUES (%s, %s)"
    val = (newprod, newprice)
    cursor.execute(sql, val)
    connection.commit()
    
    #log new product
    sql = "INSERT INTO created_products (Name, Price) VALUES (%s, %s)"
    val = (newprod, newprice)
    cursor.execute(sql, val)
    connection.commit()
    
#FUNCTION: update a product
def update_product():
    cursor.execute('SELECT id, name, price FROM products') 
    rows = cursor.fetchall()
    for row in rows:
        print(f'Product ID: {row[0]}, Name: {row[1]}, Price: {row[2]}')
    prod_id = input('Index value of the product you wish to update: ')
    prod_name = input('What is the new product name?: ') 
    prod_price = input('What is the new price?: ')
    

    if prod_name == '': 
        print('Product name will not be updated')
    else:
        sql = "UPDATE products SET name = %s WHERE id = %s"
        val = (prod_name, prod_id)
        cursor.execute(sql, val)
        connection.commit()

    if prod_price == '': 
        print('Product price will not be updated')
    else:
        sql = "UPDATE products SET price = %s WHERE id = %s"
        val = (prod_price, prod_id)
        cursor.execute(sql, val)
        connection.commit() 

    #log updated product
    sql = 'SELECT name, price FROM products WHERE id = %s'
    val = (prod_id)
    cursor.execute(sql, val)
    myresult = cursor.fetchone()
    for result in myresult:
        old_prod = row[1]
        old_price = row[2]
    sql = "INSERT INTO updated_products (Name, Price, New_Name, New_Price) VALUES (%s, %s, %s, %s)"
    val = (old_prod, old_price, prod_name, prod_price)
    cursor.execute(sql, val)
    connection.commit()    
    
#FUNCTION: delete a product
def delete_product():
    cursor.execute('SELECT id, name, price FROM products') 
    rows = cursor.fetchall()
    for row in rows:
        del_prod_name = row[1]
        del_prod_price = row[2]
        print(f'Product ID: {row[0]}, Name: {row[1]}, Price: {row[2]}')
    prod_id = input('Index value of the product you wish to delete: ')
    sql = "DELETE FROM products WHERE id=%s"
    val = (prod_id)
    cursor.execute(sql, val)
    connection.commit() 
    
    #log deleted product
    sql = "INSERT INTO deleted_products (Name, Price) VALUES (%s, %s)"
    val = (del_prod_name, del_prod_price)
    cursor.execute(sql, val)
    connection.commit()
     
#FUNCTION: track product inventory
def track_prod_inventory():
    print("The current product list is as follows: ")
    cursor.execute('SELECT id, name, price FROM products') 
    rows = cursor.fetchall()
    for row in rows:
        print(f'Product ID: {row[0]}, Name: {row[1]}, Price: {row[2]}')

    print('''
             Created products [1]
             Updated products [2]
             Products added to orders [3]
             Deleted products [4]''')
    user_input = int(input('What would you like to see?: '))    
    
    if user_input == 1:
        cursor.execute('SELECT * FROM created_products') 
        rows = cursor.fetchall()
        for row in rows:
            print(f'Name: {row[1]}, Price: {row[2]}')
    elif user_input == 2: 
        cursor.execute('SELECT * FROM updated_products') 
        rows = cursor.fetchall()
        for row in rows:
            print(f'Name: {row[1]}, Price: {row[2]}, New Name: {row[3]}, New Price: {row[4]} ')
    elif user_input == 3: 
        cursor.execute('SELECT * FROM ordered_products') 
        rows = cursor.fetchall()
        for row in rows:
            print(f'Products: {row[1]}')
    elif user_input == 4: 
        cursor.execute('SELECT * FROM deleted_products') 
        rows = cursor.fetchall()
        for row in rows:
            print(f'Name: {row[1]}, Price: {row[2]}')




#COURIER-RELATED FUNCTIONS

#FUNCTION: view all couriers
def view_couriers():
    cursor.execute('SELECT * FROM couriers')
    rows = cursor.fetchall()
    for row in rows:
        print(f'Name: {str(row[1])}, Phone Number: {row[2]}')

#FUNCTION: create a new courier
def new_courier():
    new_courier= input('What is the name of the new courier?: ')
    new_phone = input('Please enter their phone number: ')
    sql = "INSERT INTO couriers (name, phone) VALUES (%s, %s)"
    val = (new_courier, new_phone)
    cursor.execute(sql, val)
    connection.commit()
    
#FUNCTION: update a courier
def update_courier():
    cursor.execute('SELECT id, name, phone FROM couriers') 
    rows = cursor.fetchall()
    for row in rows:
        print(f'Courier ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}')
    courier_id = input('ID value of the courier you wish to update: ')
    courier_name = input('What is the new courier name?: ') 
    courier_phone = input('What is the new phone number?: ')

    if courier_name == '': 
        print('Courier name will not be updated')
    else:
        sql = "UPDATE couriers SET name = %s WHERE id = %s"
        val = (courier_name, courier_id)
        cursor.execute(sql, val)
        connection.commit()

    if courier_name == '': 
        print('Courier phone number will not be updated')
    else:
        sql = "UPDATE couriers SET phone = %s WHERE id = %s"
        val = (courier_phone, courier_id)
        cursor.execute(sql, val)
        connection.commit()  
    
#FUNCTION: delete a courier 
def del_courier():   
    cursor.execute('SELECT id, name, phone FROM couriers') 
    rows = cursor.fetchall()
    for row in rows:
        print(f'Courier ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}')
    courier_id = input('ID value of the courier you wish to delete: ')
    sql = "DELETE FROM couriers WHERE id=%s"
    val = (courier_id)
    cursor.execute(sql, val)
    connection.commit()  




#ORDER-RELATED FUCNTIONS

#FUNCTION: sort and view orders
def sort_orders():
    
    list_orders= ['Customer', 'Status', 'Courier']
    for index, value in enumerate(list_orders):
        print(index, value)
    user_input = input('What would you like to sort by?: ')
    
    if user_input == '0':    
        cursor.execute(
                        '''SELECT orders.name, orders.address, orders.phone, orders.courier, ordered_products.product, ordered_products.quantity, order_status.order_status
                        FROM orders
                        JOIN ordered_products
                        ON orders.id = ordered_products.id_order
                        JOIN order_status
                        ON orders.order_status = order_status.ID
                        ORDER BY orders.name
                        ''')
            
        rows = cursor.fetchall()
        for row in rows:
            print(f'Name: {(row[0])}, Address: {row[1]}, Phone Number: {row[2]}, Courier: {row[3]}, Product:{row[4]}, Quantity: {row[5]}, Order Status: {row[6]} ')
    
    if user_input == '1':
        cursor.execute(
                        '''SELECT orders.name, orders.address, orders.phone, orders.courier, ordered_products.product, ordered_products.quantity, order_status.order_status
                        FROM orders
                        JOIN ordered_products
                        ON orders.id = ordered_products.order
                        JOIN order_status
                        ON orders.order_status = order_status.ID
                        ORDER BY order_status.order_status
                        ''')
            
        rows = cursor.fetchall()
        for row in rows:
            print(f'Name: {(row[0])}, Address: {row[1]}, Phone Number: {row[2]}, Courier: {row[3]}, Product:{row[4]}, Quantity: {row[5]}, Order Status: {row[6]} ')                
    
    if user_input == '2':
        cursor.execute(
                        '''SELECT orders.name, orders.address, orders.phone, orders.courier, ordered_products.product, ordered_products.quantity, order_status.order_status
                        FROM orders
                        JOIN ordered_products
                        ON orders.id = ordered_products.order
                        JOIN order_status
                        ON orders.order_status = order_status.ID
                        ORDER BY orders.courier
                        ''')
            
        rows = cursor.fetchall()
        for row in rows:
            print(f'Name: {(row[0])}, Address: {row[1]}, Phone Number: {row[2]}, Courier: {row[3]}, Product:{row[4]}, Quantity: {row[5]}, Order Status: {row[6]} ')                        

#FUNCTION: create a new order
def new_order():
    
    customer_name = input('Please type the customer name: ')
    customer_address = input('Please type the customer address: ')
    customer_phone = input('Please type the customer phone number: ')

    
    #add courier to the order 
    cursor.execute('SELECT id, name, phone FROM couriers') 
    rows = cursor.fetchall()
    for row in rows:
        print(f'Courier ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}')
    
    courier_add = input('ID of the courier you would like to attach to this order: ')

    # Set order-status to preparing(1)
    order_status = 1

    #add new order
    sql = "INSERT INTO orders (name, address, phone, courier, order_status) VALUES (%s, %s, %s, %s, %s)"
    val = (customer_name, customer_address, customer_phone, courier_add, order_status)
    cursor.execute(sql, val)
    connection.commit()


    #print products list with index values and get user input for what products they want, add to ordered products table
    cursor.execute('SELECT id, name, price FROM products') 
    rows = cursor.fetchall()
    for row in rows:
        print(f'Product ID: {row[0]}, Name: {row[1]}, Price: {row[2]}')
    
    while True:
        add_prod_input = input('What products would you like to add to this order? Type done to exit: ')
        if add_prod_input == 'done':
            break
        else:
            #find the id of the order we just added
            sql = 'SELECT id FROM orders WHERE name=%s'
            val = (customer_name)
            cursor.execute(sql, val)
            row = cursor.fetchone()
            order_id = row[0]
            #ask quantity
            quantity_input = input('Product quantity: ')
            #insert into ordered products (order, product, quantity)
            sql = "INSERT INTO ordered_products (id_order, product, quantity) VALUES (%s, %s, %s)"
            val = (order_id, add_prod_input, quantity_input)
            cursor.execute(sql, val)
            connection.commit()

#FUNCTION: update the order status of a product
def update_order_status():
    
    #print order list with ids
    print ("Order list index-values are : ")
    cursor.execute("SELECT * FROM orders ORDER BY orders.name")      
    rows = cursor.fetchall()
    for row in rows:
            print(f'Order ID:{(row[0])}, Name: {(row[1])}, Address: {row[2]}, Phone Number: {row[3]}, Courier: {row[4]}, Order Status: {row[5]} ')
    
    #get user input for order id
    user_order_index = input('ID value of the order you wish to update: ')

    #print possible order statuses
    cursor.execute("SELECT * FROM order_status")
    rows = cursor.fetchall()
    for row in rows:
            print(f'ID: {(row[0])}, Status: {(row[1])} ')
    
    #get user input for new order status
    new_status = input('What is the new order status?: ') 

    #update status for this order
    sql = "UPDATE orders SET  order_status = %s WHERE id = %s"
    val = (new_status, user_order_index)
    cursor.execute(sql, val)
    connection.commit()

#FUNCTION: update entire order
def update_full_order():
    
    #print order list with ids
    print ("Order list index-values are : ")
    cursor.execute("SELECT * FROM orders ORDER BY orders.name")      
    rows = cursor.fetchall()
    for row in rows:
            print(f'Order ID:{(row[0])}, Name: {(row[1])}, Address: {row[2]}, Phone Number: {row[3]}, Courier: {row[4]}, Order Status: {row[5]} ')
    
    #get user input for order id
    user_order_index = input('ID value of the order you wish to update: ')

    #user inputs for name, address, phone, courier and order status
    name = input('Please type the customer name: ')
    address = input('Please type the customer address: ')
    phone = input('Please type the customer phone number: ')

    cursor.execute('SELECT id, name, phone FROM couriers') 
    rows = cursor.fetchall()
    for row in rows:
        print(f'Courier ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}')

    courier = input('ID of the courier you want to add: ') 

    cursor.execute("SELECT * FROM order_status")
    rows = cursor.fetchall()
    for row in rows:
            print(f'ID: {(row[0])}, Status: {(row[1])} ')
    
    order_status = input('What is the new order status?: ') 

    #update the database
    column_list = ['name', 'address', 'phone', 'courier', 'order_status']
    val_tup_list = [(name, user_order_index), (address, user_order_index), (phone, user_order_index), (courier, user_order_index), (order_status, user_order_index)]
 
    for item in column_list:
        for first, second in val_tup_list:
            column_name = [ i for i, j in locals().items() if j == first][0] #gets variable name of first and puts it into column_name
            if first == '':
                continue
            elif item == column_name:
                sql = (f"UPDATE orders SET {item} = %s WHERE id = %s")
                val = (first, second)
                cursor.execute(sql, val)
                connection.commit()  

#FUNCTION: delete order
def del_order():
    cursor.execute('SELECT * FROM orders') 
    rows = cursor.fetchall()
    for row in rows:
            print(f'Order ID:{(row[0])}, Name: {(row[1])}, Address: {row[2]}, Phone Number: {row[3]}, Courier: {row[4]}, Order Status: {row[5]} ') 
    order_id = input('ID of the order you wish to delete: ')
    sql = "DELETE FROM orders WHERE id=%s"
    val = (order_id)
    cursor.execute(sql, val)
    connection.commit()




#CUSTOMER_RELATED FUNCTIONS

def view_customer_list():
    cursor.execute('SELECT * FROM customers')
    rows = cursor.fetchall()
    for row in rows:
        print(f'Name: {(row[1])}, Order ID: {row[2]}')

def update_customer_list():
    #view discrepancy in customers in orders list and customers in customer list
    #shows customers that are in orders but not in customer list yet
    cursor.execute('''SELECT id, name FROM orders as od
                    WHERE (NOT EXISTS(SELECT name, order_ID
                        FROM customers 
                        WHERE (name = od.name AND order_ID = od.id)))''')

    user_input = input('Would you like to add these customers to the customer list?(y/n): ')
    
    if user_input == 'y':
        rows = cursor.fetchall()
        for row in rows:
            name = row[1]
            order_id = row[0]
            sql = 'INSERT INTO customers (name, order_id) VALUES (%s, %s)'
            val = (name, order_id)
            cursor.execute(sql, val)
            connection.commit()
    
    elif user_input == 'n':
        print('Customer list has not been updated')        
            
def delete_customer_list():
    cursor.execute('SELECT ID, name, order_id FROM customers') 
    rows = cursor.fetchall()
    for row in rows:
        print(f'Customer ID: {row[0]}, Name: {row[1]}, Order ID: {row[2]}')
    customer_id = input('ID of the customer you wish to delete: ')
    sql = "DELETE FROM customers WHERE id=%s"
    val = (customer_id)
    cursor.execute(sql, val)
    connection.commit()  




#MAIN MENU FUNCTION
  
def mainmenu():
    while True:

        print ('''Menu
        0. Exit 
        1. Main Menu (CSV)
        2. Main Menu (Database)''')

        data_store_option = int(input("Please enter menu number: "))
        
        if data_store_option == 0:
            print('Exiting application')
            exit() 

        elif data_store_option == 1:

            print ('''Main menu
            0. Return to Main Menu
            1. Products
            2. Couriers
            3. Orders''')

            user_input = int(input("Please enter menu number: "))
            
            if user_input == 0:
                continue

            elif user_input == 1:  
                print('''Product Menu:
                0. Return to main menu
                1. Load and View products
                2. Create a new product
                3. Update a product
                4. Delete a product''')
                
                x = int(input("Please enter menu number: "))
                
                if x == 0:
                    continue
                
                elif x == 1: 
                #view products    
                    load_product_data()
                    view_products_csv()
                    
                
                elif x == 2:
                #create a new product    
                    create_product_csv()
            
                
                elif x == 3:
                #update an existing product    
                    update_product_csv()
                    
                
                elif x == 4:
                #delete a product    
                    delete_product_csv()
                     
                else:
                    print('You have not entered a valid sub-menu number, please try again') 

            elif user_input == 2:
                print('''Courier Menu:
                    0. Return to main menu
                    1. Load and View courier list
                    2. Create a new courier
                    3. Update existing courier
                    4. Delete courier
                ''')

                x = int(input("Please enter menu number: "))

                if x == 0:
                    continue

                elif x == 1:
                    load_courier_data()
                    view_couriers_csv()

                elif x == 2:
                    #create a new courier
                    new_courier_csv()
                    
                
                elif x == 3:
                    #update exisitng courier
                    update_courier_csv()
                    
                    
                elif x == 4:
                    #delete a courier
                    del_courier_csv()
                    
                else:
                    print('You have not entered a valid sub-menu number, please try again')     
                
            elif user_input == 3:
                print('''Order Menu:
                    0. Return to main menu
                    1. Load, View and Sort orders
                    2. Create a new order
                    3. Update order status
                    4. Update existing order
                    5. Delete an order''')

                x = int(input("Please enter menu number: "))

                if x == 0:
                    continue

                elif x == 1:
                    #view and sort orders
                    load_order_data()
                    sort_orders_csv()  
                    
                elif x == 2:
                    #create a new order
                    load_courier_data()
                    load_product_data()
                    new_order_csv()
                    

                elif x == 3:
                    #update order status                    
                    update_order_status_csv()
                    

                elif x == 4:
                    #update an existing order
                    load_courier_data()
                    load_product_data()
                    update_full_order_csv()
                         

                elif x==5:
                    #delete an existing order
                    del_order_csv()
                    
                else:
                    print('You have not entered a valid sub-menu number, please try again') 
            else:
                print('You have not entered a valid menu number, please try again')             

        elif data_store_option == 2:
            print ('''Main menu
            0. Exit Database
            1. Products
            2. Couriers
            3. Orders
            4. Customers''')

            user_input = int(input("Please enter menu number: "))
            
            if user_input == 0:
                #exit database
                cursor.close()
                connection.close()
                print('You have successfully closed the connection to the database!')            

            elif user_input == 1:
                
                print('''Product Menu:
                0. Return to main menu
                1. View products
                2. Create a new product
                3. Update a product
                4. Delete a product
                5. Track product inventory''')
                
                x = int(input("Please enter menu number: "))
                
                if x == 0:
                    continue
                
                elif x == 1: 
                #view products    
                    view_products()
                
                elif x == 2:
                #create a new product    
                    create_product()
                
                elif x == 3:
                #update an existing product    
                    update_product()
                
                elif x == 4:
                #delete a product    
                    delete_product()

                elif x == 5:
                    track_prod_inventory()    
                
                else:
                    print('You have not entered a valid sub-menu number, please try again') 

            elif user_input == 2:
                print('''Courier Menu:
                    0. Return to main menu
                    1. Print courier list
                    2. Create a new courier
                    3. Update existing courier
                    4. Delete courier
                ''')

                x = int(input("Please enter menu number: "))

                if x == 0:
                    continue

                elif x == 1:
                    #View couriers
                    view_couriers()

                elif x == 2:
                    #create a new courier
                    new_courier()
                
                elif x == 3:
                    #update exisitng courier
                    update_courier()
                    
                elif x == 4:
                    #delete a courier
                    del_courier()

                else:
                    print('You have not entered a valid sub-menu number, please try again')     
                
            elif user_input == 3:
                print('''Order Menu:
                    0. Return to main menu
                    1. Sort and View orders
                    2. Create a new order
                    3. Update order status
                    4. Update existing order
                    5. Delete an order''')

                x = int(input("Please enter menu number: "))

                if x == 0:
                    continue

                elif x == 1:
                    #view and sort orders
                    sort_orders()  
                    
                elif x == 2:
                    #create a new order
                    new_order()

                elif x == 3:
                    #update order status                    
                    update_order_status()

                elif x == 4:
                    #update an existing order
                    update_full_order()      

                elif x==5:
                    #delete an existing order
                    del_order()

                else:
                    print('You have not entered a valid sub-menu number, please try again') 
            
            elif user_input == 4:
                print('''Customer Menu:
                    0. Return to main menu
                    1. View customers
                    2. Update customers
                    3. Delete customers
                    ''')
                x = int(input("Please enter menu number: "))

                if x == 0:
                    continue
                
                elif x == 1:
                    #view customers
                    view_customer_list()

                elif x == 2:
                    #update customers
                    update_customer_list()

                elif x == 3:
                    #delete customers
                    delete_customer_list()
                
                else:
                    print('You have not entered a valid sub-menu number, please try again')                    
    
            else:
                    print('You have not entered a valid menu number, please try again') 
        else:
            print('You have not entered a valid menu number, please try again')

if __name__ == "__main__":
    mainmenu()
