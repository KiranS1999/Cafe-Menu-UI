#COURIER-RELATED FUNCTIONS

from db_connect import ConnectDB
#FUNCTION: view all couriers
class CourierDB(ConnectDB):    
    def view_couriers(self):
        cursor, connection = super().connect()
        print('The current courier information:')
        cursor.execute('SELECT * FROM couriers')
        rows = cursor.fetchall()
        for row in rows:
            print(f'Name: {str(row[1])}, Phone Number: {row[2]}')

    #FUNCTION: create a new courier
    def new_courier(self):
        cursor, connection = super().connect()
        new_courier= input('What is the name of the new courier?: ')
        new_phone = input('Please enter their phone number: ')
        sql = "INSERT INTO couriers (name, phone) VALUES (%s, %s)"
        val = (new_courier, new_phone)
        cursor.execute(sql, val)
        connection.commit()
    
    #FUNCTION: update a courier
    def update_courier(self):
        cursor, connection = super().connect()
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
                break

            elif courier_id not in available_ids:
                print('You have selected an invalid courier ID, please try again!')
                continue
    
    #FUNCTION: delete a courier #fix, works without try
    def del_courier(self): 
        cursor, connection = super().connect()
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
                break
            
            elif courier_id not in available_ids:
                print('You have selected an invalid courier ID, please try again!')
                continue

