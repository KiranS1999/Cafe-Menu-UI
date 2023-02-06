#### ORDER-RELATED CLASS ####


# Import DB Connection Class
from db_connect import ConnectDB


class OrderDB(ConnectDB):

    def view_orders(self):
        '''
        View current order information in the database
        '''

        cursor, connection = super().connect()
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
        
    def sort_orders(self):
        '''
        Sort and view orders on customer name or status
        '''

        cursor, connection = super().connect()
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

    def new_order(self):
        '''
        Create a new order and insert into database
        '''

        cursor, connection = super().connect()
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
                        
    def update_order_status(self):
        '''
        Update the status of a particular order
        '''

        cursor, connection = super().connect()
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
    
    def update_full_order(self):
        '''
        Update each value of existing order
        '''

        cursor, connection = super().connect()
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

    def del_order(self):
        '''
        Delete an order and its references within all database tables
        '''

        cursor, connection = super().connect()
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
                break

            elif order_id not in del_ids:
                print('You have selected an invalid order id, please try again!')
                continue
