#PRODUCT-RELATED FUNCTIONS

from db_connect import ConnectDB

class ProductDB(ConnectDB):

    def view_products(self):
        '''
        View current product information in the database
        '''

        cursor, connection = super().connect()
        print('The current product information:')
        cursor.execute('SELECT * FROM products')
        rows = cursor.fetchall()
        for row in rows:
            print(f'Name: {(row[1])}, Price: {row[2]}')
        print()    

    def create_product(self):
        '''
        Create a new product then insert into table
        '''

        cursor, connection = super().connect()
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
        
    def update_product(self):
        '''
        Update a product that exists within the database
        '''

        cursor, connection = super().connect()
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
                break

            elif prod_id not in available_ids:
                print('You have selected an invalid product ID, please try again!')    
                continue

    def delete_product(self):
        '''
         Delete a product and its references within all tables
        '''

        cursor, connection = super().connect()
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
                
                break
            
            elif prod_id not in available_ids:
                print('You have selected an invalid product ID, please try again!')
                continue

    def track_prod_inventory(self):
        '''
        Track product inventory: New, Updated, Added to Orders, Deleted
        '''

        cursor, connection = super().connect()
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
        