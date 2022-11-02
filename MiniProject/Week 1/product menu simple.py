products = ['coke', 'sprite', 'fanta', 'water', 'lemonade'] #create a product list

main_menu = ['0.Exit, 1. Products']
print (main_menu)

user_input = int(input("Please type 0 to exit app, otherwise type 1 to see product menu: "))

if user_input == 0:
    print('Exiting')
    exit()
elif user_input == 1:
    print(products)
    x = int(input("Please type 0 to return to main menu, 1 to see product list, 2 to create a new product, 3 to update a product and 4 to delete a product: "))
    if x == 0:
        print(main_menu)
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
        user_index = int(input('Please type the index vlaue of the product you wish to change: '))
        new_name = input('Please write the new name of the product: ')
        products[user_index] = new_name 
        print(products)
    elif x == 4:
        print(products)
        for index, value in enumerate(products):
            print(index, value)
        user_index = int(input('Please type the index vlaue of the product you wish to delete: '))    
        del products[user_index]
        print(products)
else:
    print('You have not entered a valid number, please try again') 
