#PRODUCT-RELATED FUNCTIONS#

from csv_functions.csv_load import save_product_list
import pandas as pd


#FUNCTION: View products with pandas
def view_products_csv():
    print('Product information:')
    df = pd.read_csv('example_data\products.csv')
    print(df.to_string()) 
    print()

#FUNCTION: create a new product to csv
def create_product_csv():
    newprod = input('Please enter your product name: ').title()
    newprice = input('Please enter the price: ')
    new_prod_dict = {'Product': newprod, 'Price': newprice}
    products.append(new_prod_dict)
    save_product_list()
    view_products_csv()
    
#FUNCTION: update a product to csv
def update_product_csv():
    
    try:
        view_products_csv()
        user_index = int(input('Index value of the product you wish to update: '))
        product_to_change = products[user_index]
        for key, value in product_to_change.items():
            print(key, ':', value)

        product_new = input('What is the new product name?: ').title()  
        price_new = input('What is the new price?: ')

        if product_new == '': 
            print('Product name will not be updated')
        else:
            product_to_change['Product'] = product_new

        if price_new == '': 
            print('Price will not be updated')
        else:
            product_to_change['Price'] = price_new    
        
        save_product_list()
        view_products_csv()
        
    
    except (IndexError, ValueError):
        print('You have selected an invalid index number.') 

    else:
        print('You have successfully updated this product!')    
 
#FUNCTION: delete a product to csv #check
def delete_product_csv():
         
    try:
        view_products_csv()
        user_index = int(input('Index value of the product you wish to delete: '))    
        del products[user_index]
        save_product_list()
        view_products_csv()
           

    except (IndexError, ValueError):
        print('You have selected an invalid index number.')        

    else:
        print('You have successfully deleted this product!')    
        