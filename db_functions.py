#DATABASE specifc functions referenced in current_project.py, cafe project

#import libraries
import pymysql
import os
from time import sleep
from dotenv import load_dotenv


#### SET UP DB CONNECTION ####

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
    print('The current product information:')
    cursor.execute('SELECT * FROM products')
    rows = cursor.fetchall()
    for row in rows:
        print(f'Name: {(row[1])}, Price: {row[2]}')
    print()    

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
    
    view_products()

#FUNCTION: update a product
def update_product():
    
    available_ids = []
    
    #view current products
    cursor.execute('SELECT id, name, price FROM products') 
    rows = cursor.fetchall()
    for row in rows:
        available_ids.append(str(row[0]))
        print(f'Product ID: {row[0]}, Name: {row[1]}, Price: {row[2]}')
    
    while True:
        prod_id = input('ID of the product you wish to update: ') 
        
        if prod_id in available_ids:

            #log updated product - get old name/price
            sql = 'SELECT name, price FROM products WHERE id = %s'
            val = (prod_id)
            cursor.execute(sql, val)
            row = cursor.fetchone()
            old_prod = row[0]
            old_price = row[1]

            #update product in main products table
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

            #log updated product - insert into table
            sql = "INSERT INTO updated_products (Name, Price, New_Name, New_Price) VALUES (%s, %s, %s, %s)"
            val = (old_prod, old_price, prod_name, prod_price)
            cursor.execute(sql, val)
            connection.commit()

            view_products()
            break
        elif prod_id not in available_ids:
            print('You have selected an invalid product ID, please try again!')    
            continue

#FUNCTION: delete a product
def delete_product():
    
    available_ids = []

    #view current products 
    cursor.execute('SELECT id, name, price FROM products') 
    rows = cursor.fetchall()
    for row in rows:
        available_ids.append(str(row[0]))
        print(f'Product ID: {row[0]}, Name: {row[1]}, Price: {row[2]}')
    
    while True:
        prod_id = input('ID of the product you wish to delete: ')

        if prod_id in available_ids:
            
            #log deleted product
            sql = 'SELECT name, price FROM products WHERE id = %s'
            val = (prod_id)
            cursor.execute(sql, val)
            row = cursor.fetchone()
            del_prod_name = row[0]
            del_prod_price = row[1]

            sql = "INSERT INTO deleted_products (Name, Price) VALUES (%s, %s)"
            val = (del_prod_name, del_prod_price)
            cursor.execute(sql, val)
            connection.commit()
            
            #delete from ordered_products table (child table)
            sql = "DELETE FROM ordered_products WHERE product=%s"
            val = (prod_id)
            cursor.execute(sql, val)
            connection.commit() 

            #delete from products table
            sql = "DELETE FROM products WHERE id=%s"
            val = (prod_id)
            cursor.execute(sql, val)
            connection.commit() 
            
            view_products()
            break
        
        elif prod_id not in available_ids:
            print('You have selected an invalid product ID, please try again!')
            continue

#FUNCTION: track product inventory
def track_prod_inventory():
    #view current product list
    print("The current product list is as follows: ")
    cursor.execute('SELECT id, name, price FROM products') 
    rows = cursor.fetchall()
    for row in rows:
        print(f'Product ID: {row[0]}, Name: {row[1]}, Price: {row[2]}')

    print('''
            [1] Created products 
            [2] Updated products 
            [3] Products added to orders 
            [4] Deleted products ''')
    
    menu_range = ['1', '2', '3', '4']
  
    while True:
        user_input = input('What would you like to see?: ')
        
        if user_input == '1':
            cursor.execute('SELECT * FROM created_products') 
            rows = cursor.fetchall()
            for row in rows:
                print(f'Name: {row[1]}, Price: {row[2]}')
            break
        
        elif user_input == '2': 
            cursor.execute('SELECT * FROM updated_products') 
            rows = cursor.fetchall()
            for row in rows:
                print(f'Name: {row[1]}, Price: {row[2]}, New Name: {row[3]}, New Price: {row[4]} ')
            break
        
        elif user_input == '3': 
            cursor.execute('SELECT * FROM ordered_products') 
            rows = cursor.fetchall()
            for row in rows:
                print(f'Order ID: {row[1]}, Product:{row[2]}, Quantity:{row[3]} ')
            break
        
        elif user_input == '4': 
            cursor.execute('SELECT * FROM deleted_products') 
            rows = cursor.fetchall()
            for row in rows:
                print(f'Name: {row[1]}, Price: {row[2]}')
            break
        
        elif user_input not in menu_range:
            print('You have not entered a valid menu number, please try again!')
            continue        
    



#COURIER-RELATED FUNCTIONS

#FUNCTION: view all couriers
def view_couriers():
    print('The current courier information:')
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
    view_couriers()

#FUNCTION: update a courier
def update_courier():
    
    available_ids = []

    #view current courier list
    cursor.execute('SELECT id, name, phone FROM couriers') 
    rows = cursor.fetchall()
    for row in rows:
        available_ids.append(str(row[0]))
        print(f'Courier ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}')
    
    while True:
        courier_id = input('ID value of the courier you wish to update: ')  
        
        if courier_id in available_ids:

            courier_name = input('What is the new courier name?: ') 
            courier_phone = input('What is the new phone number?: ')

            if courier_name == '': 
                print('Courier name will not be updated')
            else:
                sql = "UPDATE couriers SET name = %s WHERE id = %s"
                val = (courier_name, courier_id)
                cursor.execute(sql, val)
                connection.commit()

            if courier_phone == '': 
                print('Courier phone number will not be updated')
            else:
                sql = "UPDATE couriers SET phone = %s WHERE id = %s"
                val = (courier_phone, courier_id)
                cursor.execute(sql, val)
                connection.commit()  
            
            view_couriers()
            break

        elif courier_id not in available_ids:
            print('You have selected an invalid courier ID, please try again!')
            continue
 
#FUNCTION: delete a courier #fix, works without try
def del_courier(): 

    available_ids = [] 
    
    cursor.execute('SELECT id, name, phone FROM couriers') 
    rows = cursor.fetchall()
    for row in rows:
        available_ids.append(str(row[0]))
        print(f'Courier ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}')
    
    while True:  
        courier_id = input('ID value of the courier you wish to delete: ')
        
        if courier_id in available_ids:
            #update orders table: remove the courier from the orders table - cell is NULL
            sql = "UPDATE orders SET courier = NULL WHERE courier=%s"
            val = (courier_id)
            cursor.execute(sql, val) 
            connection.commit()

            #delete from couriers
            sql = "DELETE FROM couriers WHERE id=%s"
            val = (courier_id)
            cursor.execute(sql, val) 
            connection.commit()
            
            view_couriers()
            break
        
        elif courier_id not in available_ids:
            print('You have selected an invalid courier ID, please try again!')
            continue




#ORDER-RELATED FUCNTIONS

#FUNCTION: sort and view orders
def view_orders():
    print('The current order information:')
    cursor.execute('''SELECT orders.name, orders.address, orders.phone, orders.courier, ordered_products.product, ordered_products.quantity, order_status.order_status
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
      
def sort_orders():
    
    list_orders= ['Customer', 'Status', 'Courier']
    list_options = ['0','1','2']
    
    for index, value in enumerate(list_orders):
        print(index, value)
    
    while True:
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
            break
        elif user_input == '1':
            val = ('order_status.order_status')
            
            cursor.execute(
                            '''SELECT orders.name, orders.address, orders.phone, orders.courier, ordered_products.product, ordered_products.quantity, order_status.order_status
                            FROM orders
                            JOIN ordered_products
                            ON orders.id = ordered_products.id_order
                            JOIN order_status
                            ON orders.order_status = order_status.ID
                            ORDER BY order_status.order_status
                            ''')
                
            rows = cursor.fetchall()
            for row in rows:
                print(f'Name: {(row[0])}, Address: {row[1]}, Phone Number: {row[2]}, Courier: {row[3]}, Product:{row[4]}, Quantity: {row[5]}, Order Status: {row[6]} ')                
            break
        elif user_input == '2':
            val = ('orders.courier')
            
            cursor.execute(
                            '''SELECT orders.name, orders.address, orders.phone, orders.courier, ordered_products.product, ordered_products.quantity, order_status.order_status
                            FROM orders
                            JOIN ordered_products
                            ON orders.id = ordered_products.id_order
                            JOIN order_status
                            ON orders.order_status = order_status.ID
                            ORDER BY orders.courier
                            ''')
                
            rows = cursor.fetchall()
            for row in rows:
                print(f'Name: {(row[0])}, Address: {row[1]}, Phone Number: {row[2]}, Courier: {row[3]}, Product:{row[4]}, Quantity: {row[5]}, Order Status: {row[6]} ')                        
            break
        
        elif user_input not in list_options:
            print('You have selected an invalid option ID, please try again!')
            continue   

#FUNCTION: create a new order
def new_order():
    courier_ids = []
    customer_name = input('Please type the customer name: ')
    customer_address = input('Please type the customer address: ')
    customer_phone = input('Please type the customer phone number: ')

    
    #add courier to the order 
    cursor.execute('SELECT id, name, phone FROM couriers') 
    rows = cursor.fetchall()
    for row in rows:
        courier_ids.append(str(row[0]))
        print(f'Courier ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}')
    
    
    # Set order-status to preparing(1)
    order_status = 1

    while True:
        courier_add = input('ID of the courier you would like to attach to this order: ')

        if courier_add in courier_ids:
            #add new order
            sql = "INSERT INTO orders (name, address, phone, courier, order_status) VALUES (%s, %s, %s, %s, %s)"
            val = (customer_name, customer_address, customer_phone, courier_add, order_status)
            cursor.execute(sql, val)
            connection.commit()
            break
        
        elif courier_add not in courier_ids:
            print('You have selected an invalid courier ID, please try again!')
            continue    


    #print products list with index values and get user input for what products they want, add to ordered products table
    product_ids = []
    cursor.execute('SELECT id, name, price FROM products') 
    rows = cursor.fetchall()
    for row in rows:
        product_ids.append(str(row[0]))
        print(f'Product ID: {row[0]}, Name: {row[1]}, Price: {row[2]}')
    
    while True:
        add_prod_input = input('What products would you like to add to this order? Type done to exit: ')
        if add_prod_input == 'done':
            break
        elif add_prod_input in product_ids:
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
            
        elif add_prod_input not in product_ids:
            print('You have selected an invalid product ID, please try again!')
            continue 
    view_orders()       
            
#FUNCTION: update the order status of a product
def update_order_status():
    
    #print order list with ids
    print ("Order list index-values are : ")
    order_ids = []
    cursor.execute("SELECT * FROM orders ORDER BY orders.name")      
    rows = cursor.fetchall()
    for row in rows:
        order_ids.append(str(row[0]))
        print(f'Order ID:{(row[0])}, Name: {(row[1])}, Address: {row[2]}, Phone Number: {row[3]}, Courier: {row[4]}, Order Status: {row[5]} ')
    
    while True:
        #get user input for order id
        user_order_index = input('ID value of the order you wish to update: ')

        if user_order_index in order_ids:
            break
        elif user_order_index not in order_ids:
            print('You have not selected a valid order id, please try again!')
            continue

    #print possible order statuses
    order_status_ids = []
    cursor.execute("SELECT * FROM order_status")
    rows = cursor.fetchall()
    for row in rows:
        order_status_ids.append(str(row[0]))
        print(f'ID: {(row[0])}, Status: {(row[1])} ')
    
    while True:
        #get user input for new order status
        new_status = input('What is the new order status?: ') 

        if new_status in order_status_ids:
            #update status for this order
            sql = "UPDATE orders SET  order_status = %s WHERE id = %s"
            val = (new_status, user_order_index)
            cursor.execute(sql, val)
            connection.commit()
            break

        elif new_status not in order_status_ids:
            print('You have not selected a valid status id, please try again!')
            continue
    view_orders()   

#FUNCTION: update entire order
def update_full_order():
    
    #print order list with ids
    order_ids = []
    print ("Order list index-values are : ")
    cursor.execute("SELECT * FROM orders ORDER BY orders.name")      
    rows = cursor.fetchall()
    for row in rows:
        order_ids.append(str(row[0]))
        print(f'Order ID:{(row[0])}, Name: {(row[1])}, Address: {row[2]}, Phone Number: {row[3]}, Courier: {row[4]}, Order Status: {row[5]} ')
    
    #get user input for order id
    while True:
        user_order_index = input('ID value of the order you wish to update: ')
        if user_order_index in order_ids:
            break
        elif user_order_index not in order_ids:
            print('You have not selected a valid order id, please try again!')
            continue 

    print('Please enter your new values. Press Enter if you wish to skip.')        
    #user inputs for name, address, phone, courier and order status
    name = input('Please type the customer name: ')
    address = input('Please type the customer address: ')
    phone = input('Please type the customer phone number: ')

    #user input for courier id
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
            try:    
                if first == '':
                    continue
                elif item == column_name:
                    sql = (f"UPDATE orders SET {item} = %s WHERE id = %s")
                    val = (first, second)
                    cursor.execute(sql, val)
                    connection.commit()
            except:
                print('Oops!You have entered an id that is not in our database. Please try again!')        
    view_orders()

#FUNCTION: delete order
def del_order():
    del_ids = []
    cursor.execute('SELECT * FROM orders') 
    rows = cursor.fetchall()
    for row in rows:
        del_ids.append(str(row[0]))
        print(f'Order ID:{(row[0])}, Name: {(row[1])}, Address: {row[2]}, Phone Number: {row[3]}, Courier: {row[4]}, Order Status: {row[5]} ') 
    
    while True:
        order_id = input('ID of the order you wish to delete: ')
        if order_id in del_ids:

            #delete from ordered products table
            sql = "DELETE FROM ordered_products WHERE id_order=%s"
            val = (order_id)
            cursor.execute(sql, val)
            connection.commit()

            #delete from customers table
            sql = "DELETE FROM customers WHERE order_id=%s"
            val = (order_id)
            cursor.execute(sql, val)
            connection.commit()            

            #delete from orders table
            sql = "DELETE FROM orders WHERE id=%s"
            val = (order_id)
            cursor.execute(sql, val)
            connection.commit()
            
            view_orders()
            break

        elif order_id not in del_ids:
            print('You have selected an invalid order id, please try again!')
            continue




#CUSTOMER_RELATED FUNCTIONS (CRUD customer list)

def view_customer_list():
    print('The current customer information:')
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
   
    rows = cursor.fetchall()
    for row in rows:
        print(f'Order ID: {row[0]}, Name: {row[1]}')    
    while True:
        user_input = input('Would you like to add these customers to the customer list?(y/n): ')
        if user_input == 'y':
            for row in rows:
                name = row[1]
                order_id = row[0]
                sql = 'INSERT INTO customers (name, order_id) VALUES (%s, %s)'
                val = (name, order_id)
                cursor.execute(sql, val)
                connection.commit()   
            break
        
        elif user_input == 'n':
            print('Customer list has not been updated')
            break

        elif user_input != 'y' or user_input != 'n':
            print('You have selected an invalid option, please try again!')           
            continue
    view_customer_list()    

def delete_customer_list():
    del_ids = []
    cursor.execute('SELECT ID, name, order_id FROM customers') 
    rows = cursor.fetchall()
    for row in rows:
        del_ids.append(str(row[0]))
        print(f'Customer ID: {row[0]}, Name: {row[1]}, Order ID: {row[2]}')
    while True:
        customer_id = input('ID of the customer you wish to delete: ')

        if customer_id in del_ids:
            sql = "DELETE FROM customers WHERE id=%s"
            val = (customer_id)
            cursor.execute(sql, val)
            connection.commit() 
            view_customer_list()
            break 
        if customer_id not in del_ids:   
            print('You have selected an invalid customer ID, please try again!')
            continue 




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
    
