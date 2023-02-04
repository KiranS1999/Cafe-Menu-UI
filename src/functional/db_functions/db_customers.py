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

