products = ['Coke', 'Sprite', 'Fanta', 'Water', 'Lemonade'] 
orders = []




def mainmenu():
    while True:
        print ('''Main menu
        0. Exit
        1. Products
        2. Orders''')
        user_input = int(input("Please enter menu number: "))
        if user_input == 0:
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
                    print(products)
                elif x == 2:
                    newprod = str(input('Please type your new product name: '))
                    products.append(newprod)
                    print(products)
                elif x == 3:
                    print ("List index-value are : ")
                    for index, value in enumerate(products):
                        print(index, value)
                    try:
                        user_index = int(input('Index value of the product you wish to update: ')) 
                        new_name = input('New product name: ')
                        products[user_index] = new_name 
                        print(products)
                    except IndexError:
                        print('You have selected an unavailable index, please try again')
                    except ValueError as v:
                        print('You have not entered a valid index, please try again!')    
                        #call function that starts with product menu 

                elif x == 4:
                    for index, value in enumerate(products):
                        print(index, value)
                    try:
                        user_index = int(input('Please type the index value of the product you wish to delete: '))    
                        del products[user_index]
                        print(products) 
                    except IndexError as e:
                        print('You have selected an unavailable index, please try again')
                        #call function that starts with product menu     
                    except ValueError as v:
                        print('You have not entered a valid index, please try again!')                   
                else:
                    print('You have entered an invalid index number')    
        elif user_input == 2:
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
                    print(orders)
                elif x == 2:
                    new_orders = {}
                    customer_name = str(input('Please type the customer name: '))
                    new_orders['customer_name'] = customer_name
                    customer_address = str(input('Please type the customer address: '))
                    new_orders['customer_address'] = customer_address
                    customer_phone = str(input('Please type the customer phone number: '))
                    new_orders['customer_phone'] = customer_phone
                    new_orders['Order status'] = 'Preparing'
                    orders.append(new_orders)
                    print('The current order list:')
                    print(orders)
                elif x == 3:                    
                    print ("Order list index-values are : ")
                    for index, value in enumerate(orders):
                        print(index, value)
                    try:
                        user_index = int(input('Index value of the order you wish to update: '))
                        order_to_change = orders[user_index] 
                        for key, value in order_to_change.items():
                            print(key, ':', value)
                        print('Order status options:')
                    except IndexError as e:
                        print('You have selected an unavailable index, please try again')
                        #call order list index vlalues again- currently it starts printing order list, put main menu for now
                        mainmenu()
                    except ValueError as v:
                        print('You have not entered a valid index, please try again!')
                        mainmenu()    
                    order_status_list = ['Preparing', 'Ready for dispatch', 'Delivered', 'Arrived']
                    for index, value in enumerate(order_status_list):
                        print(index, value)
                    try:
                        new_status = int(input('What is the new order status?(Type 0-3): '))
                        updated_status = order_status_list[new_status]
                        order_to_change.update({'Order status': updated_status})
                        print('The current order list:') 
                        print(orders)  
                    except IndexError as e:
                        print('You have selected an unavailable index, please try again')
                    except ValueError as v:
                        print('You have not entered a valid index, please try again!')    
                        #call function that starts with product menu- after the error it returns to the main menu which is ok fr now
                elif x == 4:
                    for index, value in enumerate(orders):
                            print(index, value)
                    try:
                        user_index = int(input('Please type the index value of the order you wish to change: '))    
                        order_to_change = orders[user_index]
                        print('The order you wish to change is as follows')
                    except IndexError as e:
                        print('You have selected an unavailable index, please try again')
                        mainmenu()
                    except ValueError as v:
                        print('You have not entered a valid index, please try again!') 
                        mainmenu()
                    for key, value in order_to_change.items():
                        print(key, ':', value)
                    dict_keys = list(order_to_change.keys()) 
                    for index, value in enumerate(dict_keys):
                        print(index, value)
                    try:
                        key_to_change = int(input('What index would you like to change?(Enter nothing if you wish to return to main menu): '))
                        key_changed = dict_keys[key_to_change]  
                        if key_to_change == '':
                            print('Property will not be updated')
                            mainmenu()
                        else: 
                            new_value = input('What is the new value?: ')
                            order_to_change.update({key_changed: new_value}) 
                            print(orders)
                    except IndexError as e:
                        print('You have selected an unavailable index, please try again')
                    except ValueError as v:
                        print('You have not entered a valid index, please try again!')         
                elif x==5:
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
                    #this works perfectly    
                              
        else:
                print('You have not entered a valid menu number, please try again') 

mainmenu()