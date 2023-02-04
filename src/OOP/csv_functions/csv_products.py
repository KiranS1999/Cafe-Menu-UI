#PRODUCT-RELATED FUNCTIONS#

from csv_load import SaveLoad
import pandas as pd
from datetime import date



class ProductLog:
    def __init__(self):
        '''Initialise the product.
        '''
        self.name = input('Please enter your name: ')
        self.date = self.current_date()
        self.action = '*No Action*'

    def update_product_log(self, new_product: str, new_price: float):
        '''Update product name and price.
        Arg:
            name: new product name
            price: new product price'''  
        self.action = f"Updated an item: name:{new_product}, price: {new_price}"

    def create_product_log(self, product: str, price: float):
        '''Log new product creation'''
        self.action = f"Created {product}:{price}"

    def delete_product_log(self, product: str):
        '''Log product deletion'''
        self.action = f"Deleted {product}"
   
    def current_date(self):
        today = str(date.today())
        return today   

    def useraccess(self):
        return f"\n {self.name} {self.action} at {self.date}"

    def writelog(self):
        with open("log.txt", "a") as file:
            log = self.useraccess()
            file.write(log)
            print('Successfully logged action!')
        


        

class ProductMenu(ProductLog, SaveLoad):
    '''Class ProductMenu implemets a product mennu with a fucntionality to CRUD products 
        and save them to a CSV'''
    def __init__(self, filename: str):
        ProductLog.__init__(self)
        SaveLoad.__init__(self, filename)
        self.product_list = []
        self.load_data()

    def load_data(self):
        return super().load_data(info_type = self.product_list)

    def save_data(self):
        return super().save_data(fieldnames =['Product', 'Price'], info_type = self.product_list )    

    def view_products(self):
        '''Display products that have been loaded
        Returns:
            dataframe of current products'''
        
        print('Product information:')
        try:
            df = pd.read_csv(self.filename)
            print(df.to_string())
        except Exception as e:
            print(f"Error: {e}")
            raise Exception

    def create_product(self):
        '''User input to create a new product
        Returns: 
        Boolean value indicating if product has been successfully added or not'''
        
        new_prod = input('Please enter your product name: ').title()
        new_price = input('Please enter the price: ')
        try:
            x = float(new_price)
            if x == 0:
                return False
        except ValueError:
            print('You have not entered an accepted price format (X.XX where X is a number)')        
            return False
        new_prod_dict = {'Product': new_prod, 'Price': new_price}
        self.product_list.append(new_prod_dict)
        super().create_product_log(new_prod, new_price)
        return True    
        

    def update_product(self):
        '''Updates existing product
        
        Returns:
        
        Boolean value indicating if product has been successfully added or not 
        '''
        
        try:
            user_index = int(input('Index value of the product you wish to update: '))
            product_to_change = self.product_list[user_index]
            for key, value in product_to_change.items():
                print(key, ':', value)

            product_new = input('What is the new product name?: ').title()  
            price_new = input('What is the new price?: ')

            if product_new == '': 
                product_new = 'Product Unchanged'
                print('Product name will not be updated')
            else:
                product_to_change['Product'] = product_new

            if price_new == '': 
                price_new = 'Price Unchanged'
                print('Price will not be updated')
            else:
                product_to_change['Price'] = price_new    

        except (IndexError, ValueError):
            print('You have selected an invalid index number.') 
            return False
        super().update_product_log(product_new, price_new)
        print('You have successfully updated this product!')      
        return True

    def delete_product(self):
            
        try:
            user_index = int(input('Index value of the product you wish to delete: '))    
            del self.product_list[user_index]
        
        except (IndexError, ValueError):
            print('You have selected an invalid index number.')        
        
        else:
            print('You have successfully deleted this product!')    
        super().delete_product_log(self.product_list[user_index])


x = ProductMenu('products.csv')
print(x.useraccess())
x.view_products()
x.create_product()
print(x.useraccess())
x.writelog()
x.save_data()
x.load_data()
x.view_products()


