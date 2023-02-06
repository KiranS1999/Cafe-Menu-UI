#### CUSTOMER_RELATED CLASS ####


# Import DB Connection Class
from db_connect import ConnectDB

class CustomerDB(ConnectDB):

    def view_customer_list(self):
        '''
        View current courier information in the database
        '''

        cursor, connection = super().connect()
        print('The current customer information:')
        cursor.execute('SELECT * FROM customers')
        rows = cursor.fetchall()
        for row in rows:
            print(f'Name: {(row[1])}, Order ID: {row[2]}')

    def update_customer_list(self):
        '''
        View discrepancy in customer data in orders list customer list
        Customers that are in orders but not in customer list yet are added 
        '''

        cursor, connection = super().connect()
    
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
  
    def delete_customer_list(self):
        '''
        Delete a specific customer
        '''

        cursor, connection = super().connect()
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
                break 
            if customer_id not in del_ids:   
                print('You have selected an invalid customer ID, please try again!')
                continue 

