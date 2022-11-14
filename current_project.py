#Program: A menu system that allows user to view and amend the products and orders for a cafe



#Libraries
import csv
import operator
import pymysql
import os
from dotenv import load_dotenv


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






#FUNCTION: Loading data through csv
def load_order_data():            
    # LOAD orders from orders.csv
    with open('orders.csv', 'r') as fhand:
        order_file = csv.DictReader(fhand)
        for row in order_file:
            orders.append(dict(row))


#FUNCTIONS: Save data to csv

def save_order_list():
    file = open('./orders.csv', 'w')
    w = csv.writer(file)
    w.writerow(['customer_name', 'customer_address', 'customer_phone', 'courier_index', 'order_status', 'product_index'])
    for dictionary in orders:
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




#FUNCTION: delete a product
def delete_product():
    cursor.execute('SELECT id, name, price FROM products') 
    rows = cursor.fetchall()
    for row in rows:
        print(f'Product ID: {row[0]}, Name: {row[1]}, Price: {row[2]}')
    prod_id = input('Index value of the product you wish to delete: ')
    sql = "DELETE FROM products WHERE id=%s"
    val = (prod_id)
    cursor.execute(sql, val)
    connection.commit()  







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
        
        load_order_data()

        print ('''Main menu
        0. Save order list and exit database
        1. Products
        2. Couriers
        3. Orders''')

        user_input = int(input("Please enter menu number: "))
        
        if user_input == 0:

            save_order_list() 
            cursor.close()
            connection.close()
            print('Exiting application')
            exit()   

        elif user_input == 1:
            
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
