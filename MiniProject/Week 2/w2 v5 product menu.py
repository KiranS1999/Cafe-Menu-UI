#Program: A menu system that allows user to view and amend the products and orders for a cafe

#create a list of products from an incoming txt file


products = ['Coke', 'Sprite', 'Fanta', 'Water', 'Lemonade'] 
orders = []



#full product menu as a function
def productmenu():
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
        newprod = input('Please type your new product name: ')
        products.append(newprod)
        print(products)
    
    elif x == 3:
    #update an existing product    
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
            productmenu()
        except ValueError as v:
            print('You have not entered a valid index, please try again!') 
            productmenu()   
    
    elif x == 4:
    #delete a product    
        for index, value in enumerate(products):
            print(index, value)
        
        try:
            user_index = int(input('Please type the index value of the product you wish to delete: '))    
            del products[user_index]
            print(products) 
        except IndexError as e:
            print('You have selected an unavailable index, please try again')
            productmenu()   
        except ValueError as v:
            print('You have not entered a valid index, please try again!')
            productmenu()                   
    
    else:
        print('You have entered an invalid index number')


#function to update the order status of a product
def order_status_update():
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
        order_to_change.update({'Order status': updated_status})
        print('The current order list:') 
        print(orders)  
    except IndexError as e:
        print('You have selected an unavailable index, please try again')
        order_status_update()
    except ValueError as v:
        print('You have not entered a valid index, please try again!')
        order_status_update()


#function to update an existing order; user can change the value of each key
def full_order_update():
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


#Main menu function, incl order and product menu with submenus    
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
            productmenu()        
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
                    #view orders
                    print(orders)
                elif x == 2:
                    #create a new order
                    new_orders = {}
                    customer_name = input('Please type the customer name: ')
                    new_orders['customer_name'] = customer_name
                    customer_address = input('Please type the customer address: ')
                    new_orders['customer_address'] = customer_address
                    customer_phone = input('Please type the customer phone number: ')
                    new_orders['customer_phone'] = customer_phone
                    new_orders['Order status'] = 'Preparing'
                    orders.append(new_orders)
                    print('The current order list:')
                    print(orders)
                elif x == 3:
                    #update order status                    
                    order_status_update()   
                elif x == 4:
                    #update an existing order
                    full_order_update()        
                elif x==5:
                    #delete an existing order
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
                      
                              
        else:
                print('You have not entered a valid menu number, please try again') 

mainmenu()
