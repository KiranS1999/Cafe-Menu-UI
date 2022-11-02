products = ['Coke', 'Sprite', 'Fanta', 'Water', 'Lemonade'] 
def mainmenu():
    while True:
        print ('''Main menu
        0. Exit
        1. Products''')
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
                    user_index = int(input('Please type the index vlaue of the product you wish to delete: '))    
                    del products[user_index]
                    print(products)
        else:
                print('You have not entered a valid menu number, please try again') 

mainmenu()