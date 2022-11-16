#Program: A menu system that allows user to view and amend the products and orders for a cafe


#Libraries
import csv
import operator
import pymysql
import os
from dotenv import load_dotenv


######CSV-RELATED FUNCTIONS######

#FUNCTION: Loading data through csv
def load_product_data():
    # LOAD products from products.csv
    with open('products.csv', 'r') as f:
        product_file = csv.DictReader(f)
        for row in product_file:
            products.append(dict(row))

def load_courier_data():    
    # LOAD couriers from couriers.csv
    with open('couriers.csv', 'r') as file:
        courier_file = csv.DictReader(file)
        for row in courier_file:
            couriers.append(dict(row))

def load_order_data():            
    # LOAD orders from orders.csv
    with open('orders.csv', 'r') as fhand:
        order_file = csv.DictReader(fhand)
        for row in order_file:
            orders.append(dict(row))


#FUNCTIONS: Save data to csv
def save_product_list():
    file = open('products.csv', 'w')
    w = csv.DictWriter(file, fieldnames = ['Product', 'Price'])
    w.writeheader()
    w.writerows(products)
    file.close()

def save_order_list():
    file = open('./orders.csv', 'w')
    w = csv.writer(file)
    w.writerow(['customer_name', 'customer_address', 'customer_phone', 'courier_index', 'order_status', 'product_index'])
    for dictionary in orders:
        w.writerow(dictionary.values())
    file.close()   

def save_courier_list():
    file = open('./couriers.csv', 'w')
    w = csv.writer(file)
    w.writerow(['Name', 'Phone'])
    for dictionary in couriers:
        w.writerow(dictionary.values())
    file.close()   









#PRODUCT-RELATED FUNCTIONS

#FUNCTION: create a new product to csv
def create_product_csv():
    newprod = input('Please enter your new product name: ')
    newprice = input('Please enter the price: ')
    new_prod_dict = {'Product': newprod, 'Price': newprice}
    products.append(new_prod_dict)
    return products

#FUNCTION: update a product to csv
def update_product_csv():
    print ("List index-value are : ")
            
    for index, value in enumerate(products):
        print(index, value)

    try:
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

    except IndexError:
        print('You have selected an unavailable index, please try again')
        update_product_csv()
    except ValueError as v:
        print('You have not entered a valid index, please try again!') 
        update_product_csv()

#FUNCTION: delete a product to csv
def delete_product_csv():
    for index, value in enumerate(products):
                print(index, value)
            
    try:
        user_index = int(input('Please type the index value of the product you wish to delete: '))    
        del products[user_index]
        print(products) 
    except IndexError as e:
        print('You have selected an unavailable index, please try again')
        delete_product_csv()  
    except ValueError as v:
        print('You have not entered a valid index, please try again!')
        delete_product_csv()                 

    else:
        print('You have entered an invalid index number')









#COURIER-RELATED FUNCTIONS

#Function: create a new courier to csv
def new_courier_csv():
    new_courier = input('What is the name of the new courier?: ')
    new_phone = input('Please enter their phone number: ')
    new_courier_dict = {'Name': new_courier, 'Phone': new_phone}
    couriers.append(new_courier_dict)
    print(couriers)

#Function: update a courier to csv
def update_courier_csv():
    print ("List index-value are : ")
        
    for index, value in enumerate(couriers):
        print(index, value)
    
    try:
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

    except IndexError:
        print('You have selected an unavailable index, please try again')
        update_courier_csv()
    except ValueError as v:
        print('You have not entered a valid index, please try again!') 
        update_courier_csv()

#FUNCTION: delete a courier to csv
def del_courier_csv():   
    for index, value in enumerate(couriers):
        print(index, value)
    
    try:
        user_index = int(input('Please type the index value of the courier you wish to delete: '))    
        del couriers[user_index]
        print(couriers) 
    except IndexError as e:
        print('You have selected an unavailable index, please try again')
            
    except ValueError as v:
        print('You have not entered a valid index, please try again!')
    
    else: #check 
        print('You have selected an invalid index, try again')










#ORDER-RELATED FUCNTIONS

#FUNCTION: sort and view orders by csv
def sort_orders_csv():
    import operator
    list_orders= ['Status', 'Courier', 'Original']
    for index, value in enumerate(list_orders):
        print(index, value)
    user_input = input('What key would you like to sort by?: ')
    if user_input == '0':
        orders.sort(key=operator.itemgetter('order_status'))
        print(orders)
    elif user_input == '1':
        orders.sort(key=operator.itemgetter('courier_index'))
        print(orders)
    elif user_input == '2':
        print(orders)


#FUNCTION: create a new order to csv
def new_order_csv():
    new_orders = {}
    customer_name = input('Please type the customer name: ')
    new_orders['customer_name'] = customer_name
    customer_address = input('Please type the customer address: ')
    new_orders['customer_address'] = customer_address
    customer_phone = input('Please type the customer phone number: ')
    new_orders['customer_phone'] = customer_phone
    

    #add courier to the order 
    print ("Courier list index-value are : ")
    for index, value in enumerate(couriers):
        print(index, value)   

    courier_add = input('Please type the index of the courier you would like to attach to this order: ')
    new_orders['courier_index']= courier_add 

    #order status to preparing
    new_orders['Order status'] = 'preparing'  

    #print products list with index values and get user input for what products they want
    print ("Product list index-value are : ")
    for index, value in enumerate(products):
        print(index, value)
    product_index = []
    while True:
        user_input = input('What products would you like to add to this order? Type done to exit: ')
        if user_input == 'done':
            break
        else:
            product_index.append(user_input)
    prod_index_str = ','.join(str(item) for item in product_index)
    new_orders['product_index']=prod_index_str     


    orders.append(new_orders)

    print('The current order list:')
    print(orders)


#FUNCTION: update the order status of a product to csv
def update_order_status_csv():
    print ("Order list index-values are : ")
    for index, value in enumerate(orders):
        print(index, value)
    
    try:
        user_index = int(input('Index value of the order you wish to update: '))
        order_to_change = orders[user_index] 
        for key, value in order_to_change.items():
            print(key, ':', value)
        
    except IndexError:
        print('You have selected an unavailable index, please try again')
        mainmenu()
    except ValueError:
        print('You have not entered a valid index, please try again!')
        mainmenu()    
    
    order_status_list = ['Preparing', 'Ready for dispatch', 'Delivered', 'Arrived']
    print('Order status options:')
    for index, value in enumerate(order_status_list):
        print(index, value)
    
    try:
        new_status = int(input('What is the new order status?(Type 0-3): '))
        updated_status = order_status_list[new_status]
        order_to_change.update({'order_status': updated_status})
        print('The current order list:') 
        print(orders)  
    except IndexError as e:
        print('You have selected an unavailable index, please try again')
        update_order_status_csv()
    except ValueError as v:
        print('You have not entered a valid index, please try again!')
        update_order_status_csv()


#FUNCTION: update entire order to csv
def update_full_order_csv():
    for index, value in enumerate(orders):
        print(index, value)
    
    try:
        user_index = int(input('Please type the index value of the order you wish to change: '))    
        order_to_change = orders[user_index]
        print('The order you wish to change is as follows')
        print(order_to_change)
    except IndexError:
        print('You have selected an unavailable index, please try again')
        mainmenu()
    except ValueError:
        print('You have not entered a valid index, please try again!')
        mainmenu() 
        
    
    for key, value in order_to_change.items():
        print(key, ':', value)
        user_input = input('What would you like to change the value to?: ')
        if user_input == '': 
            print('Property will not be updated')
        else:
            order_to_change[key] = user_input
    print(orders)        

#FUNCTION: delete order to csv
def del_order_csv():
    for index, value in enumerate(orders):
                    print(index, value)
    try:
        user_index = int(input('Please type the index vlaue of the product you wish to delete: '))    
        del orders[user_index]
        print(orders)
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





#create a list of products from an incoming csv file
orders = []
products = [] 
couriers = []



#FUNCTION: Loading data through csv

def load_product_data():
    # LOAD products from products.csv
    with open('products.csv', 'r') as f:
        product_file = csv.DictReader(f)
        for row in product_file:
            products.append(dict(row))

def load_courier_data():    
    # LOAD couriers from couriers.csv
    with open('couriers.csv', 'r') as file:
        courier_file = csv.DictReader(file)
        for row in courier_file:
            couriers.append(dict(row))

def load_order_data():            
    # LOAD orders from orders.csv
    with open('orders.csv', 'r') as fhand:
        order_file = csv.DictReader(fhand)
        for row in order_file:
            orders.append(dict(row))


#FUNCTIONS: Save data to csv

def save_product_list():
    file = open('products.csv', 'w')
    w = csv.DictWriter(file, fieldnames = ['Product', 'Price'])
    w.writeheader()
    w.writerows(products)
    file.close()

def save_order_list():
    file = open('./orders.csv', 'w')
    w = csv.writer(file)
    w.writerow(['customer_name', 'customer_address', 'customer_phone', 'courier_index', 'order_status', 'product_index'])
    for dictionary in orders:
        w.writerow(dictionary.values())
    file.close()   

def save_courier_list():
    file = open('./couriers.csv', 'w')
    w = csv.writer(file)
    w.writerow(['Name', 'Phone'])
    for dictionary in couriers:
        w.writerow(dictionary.values())
    file.close()   











#PRODUCT-RELATED FUNCTIONS

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

#Function: create a new courier
def new_courier():
    new_courier= input('What is the name of the new courier?: ')
    new_phone = input('Please enter their phone number: ')
    sql = "INSERT INTO couriers (name, phone) VALUES (%s, %s)"
    val = (new_courier, new_phone)
    cursor.execute(sql, val)
    connection.commit()
    

#Function: update a courier
def update_courier():
    cursor.execute('SELECT id, name, phone FROM couriers') 
    rows = cursor.fetchall()
    for row in rows:
        print(f'Courier ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}')
    courier_id = input('Index value of the product you wish to update: ')
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
    courier_id = input('Index value of the product you wish to delete: ')
    sql = "DELETE FROM couriers WHERE id=%s"
    val = (courier_id)
    cursor.execute(sql, val)
    connection.commit()  










#ORDER-RELATED FUCNTIONS

#FUNCTION: sort and view orders
def sort_orders():
    import operator
    list_orders= ['Status', 'Courier', 'Original']
    for index, value in enumerate(list_orders):
        print(index, value)
    user_input = input('What key would you like to sort by?: ')
    if user_input == '0':
        orders.sort(key=operator.itemgetter('order_status'))
        print(orders)
    elif user_input == '1':
        orders.sort(key=operator.itemgetter('courier_index'))
        print(orders)
    elif user_input == '2':
        print(orders)


#FUNCTION: create a new order
def new_order():
    new_orders = {}
    customer_name = input('Please type the customer name: ')
    new_orders['customer_name'] = customer_name
    customer_address = input('Please type the customer address: ')
    new_orders['customer_address'] = customer_address
    customer_phone = input('Please type the customer phone number: ')
    new_orders['customer_phone'] = customer_phone
    

    #add courier to the order 
    cursor.execute('SELECT id, name, phone FROM couriers') 
    rows = cursor.fetchall()
    for row in rows:
        print(f'Courier ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}')
    
    courier_add = input('Please type the index of the courier you would like to attach to this order: ')
    new_orders['courier_index']= courier_add 



    #order status to preparing
    new_orders['Order status'] = 'preparing'  

    #print products list with index values and get user input for what products they want
    cursor.execute('SELECT id, name, price FROM products') 
    rows = cursor.fetchall()
    for row in rows:
        print(f'Product ID: {row[0]}, Name: {row[1]}, Price: {row[2]}')
    product_index = []    
    
    while True:
        user_input = input('What products would you like to add to this order? Type done to exit: ')
        if user_input == 'done':
            break
        else:
            product_index.append(user_input)

    prod_index_str = ','.join(str(item) for item in product_index)
    new_orders['product_index']=prod_index_str 
    print(new_orders)    
    orders.append(new_orders)

    #track products appended to an order
    sql = "INSERT INTO ordered_products (products) VALUES (%s)"
    val = (prod_index_str)
    cursor.execute(sql, val)
    connection.commit()




#FUNCTION: update the order status of a product
def update_order_status():
    print ("Order list index-values are : ")
    for index, value in enumerate(orders):
        print(index, value)
    
    try:
        user_index = int(input('Index value of the order you wish to update: '))
        order_to_change = orders[user_index] 
        for key, value in order_to_change.items():
            print(key, ':', value)
        
    except IndexError:
        print('You have selected an unavailable index, please try again')
        mainmenu()
    except ValueError:
        print('You have not entered a valid index, please try again!')
        mainmenu()    
    
    order_status_list = ['Preparing', 'Ready for dispatch', 'Delivered', 'Arrived']
    print('Order status options:')
    for index, value in enumerate(order_status_list):
        print(index, value)
    
    try:
        new_status = int(input('What is the new order status?(Type 0-3): '))
        updated_status = order_status_list[new_status]
        order_to_change.update({'order_status': updated_status})
        print('The current order list:') 
        print(orders)  
    except IndexError as e:
        print('You have selected an unavailable index, please try again')
        update_order_status()()
    except ValueError as v:
        print('You have not entered a valid index, please try again!')
        update_order_status()()


#FUNCTION: update entire order
def update_full_order():
    for index, value in enumerate(orders):
        print(index, value)
    
    try:
        user_index = int(input('Please type the index value of the order you wish to change: '))    
        order_to_change = orders[user_index]
        print('The order you wish to change is as follows')
        print(order_to_change)
    except IndexError:
        print('You have selected an unavailable index, please try again')
        mainmenu()
    except ValueError:
        print('You have not entered a valid index, please try again!')
        mainmenu() 
        
    
    for key, value in order_to_change.items():
        print(key, ':', value)
        user_input = input('What would you like to change the value to?: ')
        if user_input == '': 
            print('Property will not be updated')
        else:
            order_to_change[key] = user_input
    print(orders)        

#FUNCTION: delete order
def del_order():
    for index, value in enumerate(orders):
                    print(index, value)
    try:
        user_index = int(input('Please type the index vlaue of the product you wish to delete: '))    
        del orders[user_index]
        print(orders)
    except IndexError as e:
        print('You have selected an unavailable index, please try again')
    except ValueError as v:
        print('You have not entered a number, please try again!')
   








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
            load_product_data()
            load_courier_data()
            load_order_data()

            print ('''Main menu
            0. Save product, order and courier list
            1. Products
            2. Couriers
            3. Orders''')

            user_input = int(input("Please enter menu number: "))
            
            if user_input == 0:
                save_product_list()
                save_courier_list()
                save_order_list() 
                print('Exiting application')
                exit()   

            elif user_input == 1:
                print('Product list:')
                print(products)
                print('''Product Menu:
                0. Return to main menu
                1. View products
                2. Create a new product
                3. Update a product
                4. Delete a product''')
                
                x = int(input("Please enter menu number: "))
                
                if x == 0:
                    mainmenu()
                
                elif x == 1: 
                #view products    
                    print(products)
                
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
                    1. Print courier list
                    2. Create a new courier
                    3. Update existing courier
                    4. Delete courier
                ''')

                x = int(input("Please enter menu number: "))

                if x == 0:
                    mainmenu()

                elif x == 1:
                    print(couriers)

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
                    1. View orders
                    2. Create a new order
                    3. Update order status
                    4. Update existing order
                    5. Delete an order''')

                x = int(input("Please enter menu number: "))

                if x == 0:
                    mainmenu()

                elif x == 1:
                    #view and sort orders
                    sort_orders_csv()  
                    
                elif x == 2:
                    #create a new order
                    new_order_csv()

                elif x == 3:
                    #update order status                    
                    update_order_status_csv()

                elif x == 4:
                    #update an existing order
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
            3. Orders''')

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
                    mainmenu()
                
                elif x == 1: 
                #view products    
                    cursor.execute('SELECT * FROM products')
                    rows = cursor.fetchall()
                    for row in rows:
                        print(f'Name: {str(row[1])}, Price: {row[2]}')
                
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
                    mainmenu()

                elif x == 1:
                    #View couriers
                    cursor.execute('SELECT * FROM couriers')
                    rows = cursor.fetchall()
                    for row in rows:
                        print(f'Name: {str(row[1])}, Phone Number: {row[2]}')

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
                    1. View orders
                    2. Create a new order
                    3. Update order status
                    4. Update existing order
                    5. Delete an order''')

                x = int(input("Please enter menu number: "))

                if x == 0:
                    mainmenu()

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
            else:
                    print('You have not entered a valid menu number, please try again') 

if __name__ == "__main__":
    mainmenu()
