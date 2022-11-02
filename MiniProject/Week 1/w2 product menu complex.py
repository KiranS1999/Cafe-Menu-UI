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
                    newprod = input('Please type your new product name: ')
                    products.append(newprod)
                    print(products)
                elif x == 3:
                    print ("List index-value are : ")
                    for index, value in enumerate(products):
                        print(index, value)
                    user_index = int(input('Index value of the product you wish to update: '))
                    new_name = input('New product name: ')
                    products[user_index] = new_name 
                    print(products)
                elif x == 4:
                    for index, value in enumerate(products):
                        print(index, value)
                    user_index = int(input('Please type the index value of the product you wish to delete: '))    
                    del products[user_index]
                    print(products)
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
                    customer_name = input('Please type the customer name: ')
                    new_orders['customer_name'] = customer_name
                    customer_address = input('Please type the customer address: ')
                    new_orders['customer_address'] = customer_address
                    customer_phone = input('Please type the customer phone number: ')
                    new_orders['customer_phone'] = customer_phone
                    new_orders['Order status'] = 'Preparing'
                    orders.append(new_orders)
                    print(orders)
                elif x == 3:
                    print ("Order list index-values are : ")
                    for index, value in enumerate(orders):
                        print(index, value)
                    user_index = int(input('Index value of the order you wish to update: '))
                    order_to_change = orders[user_index] 
                    for key, value in order_to_change.items():
                        print(key, ':', value)
                    print('Order status options:')
                    order_status_list = ['Preparing', 'Ready for dispatch', 'Delivered', 'Arrived']
                    for index, value in enumerate(order_status_list):
                        print(index, value)
                    new_status = int(input('What is the new order status?(Type 0-3): '))
                    updated_status = order_status_list[new_status]
                    order_to_change.update({'Order status': updated_status}) 
                    print(orders)  
                elif x == 4:
                    for index, value in enumerate(orders):
                            print(index, value)
                    user_index = int(input('Please type the index value of the order you wish to change: '))    
                    order_to_change = orders[user_index]
                    print(order_to_change)
                    print('The order you wish to change is as follows')
                    for key, value in order_to_change.items():
                        print(key, ':', value)
                    dict_keys = list(order_to_change.keys()) #list of strings
                    print(type(dict_keys))#test gives string in a list
                    print(dict_keys)#test
                    for index, value in enumerate(dict_keys):
                        print(index, value)
                    key_to_change = int(input('What index would you like to change?: '))
                    key_changed = dict_keys[key_to_change]
                    print(key_changed) #test
                      #fix this section
                    if key_to_change == '':
                        print('Property will not be updated')
                        mainmenu()
                    else: 
                        new_value = input('What is the new value?: ')
                        order_to_change.update({key_changed: new_value}) #this in particular
                        print(orders)
                elif x==5:
                    for index, value in enumerate(orders):
                        print(index, value)
                    user_index = int(input('Please type the index vlaue of the product you wish to delete: '))    
                    del orders[user_index]
                    print(orders) 
        else:
                print('You have not entered a valid menu number, please try again') 

mainmenu()