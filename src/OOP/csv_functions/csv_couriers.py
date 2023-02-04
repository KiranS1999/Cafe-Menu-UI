#COURIER-RELATED FUNCTIONS#

import pandas as pd 
from datetime import date
from dataclasses import dataclass, field
import csv
    
@dataclass
class UserLog:    
    '''Class for keeping track of user information'''
    name: str = field(default_factory=('No User'))
    action: str = field(default_factory=('No Action'))
    date: str = field(default_factory=('No Date'))


class SaveLoad:
    def __init__(self, filename: str):
        self.filename = filename
    
    def load_data (self, info_type):
        try:
            with open(self.filename, "r", newline = '') as file:
                file = csv.DictReader(file)
                for row in file:
                    info_type.append(dict(row))  
        except Exception as e:
            print(f"Error: {e}")
            raise Exception    

    def save_data (self, info_type, fieldnames=[]):
        try:
            with open(self.filename, "w", newline = '') as file:
                w = csv.DictWriter(file, fieldnames)
                w.writeheader()
                w.writerows(info_type)
    
        except Exception as e:
            print(f"Error: {e}")
            raise Exception

class CourierLog:
    def __init__(self, name: str):
        '''Initialise the product.
        Args:
            name: User Name
        '''
        self.name = name
        self.date = self.current_date()
        self.action = '*No Action*'

    def update_courier_log(self, new_courier_name: str, new_courier_phone: float):
        '''Log update courier name and price.
        Arg:
            name: new courier name
            price: new courier phone'''  
        self.action = f"Updated a courier: name:{new_courier_name}, phone: {new_courier_phone}"

    def create_courier_log(self, new_courier_name: str, new_courier_phone: float):
        '''Log courier creation'''
        self.action = f"Created a new courier, {new_courier_name}:{new_courier_phone}"

    def delete_courier_log(self, courier_name: str):
        '''Log courier deletion'''
        self.action = f"Deleted {courier_name}"
   
    def current_date(self):
        today = str(date.today())
        return today   

    def useraccess(self):
        return f"\n{self.name} {self.action} at {self.date}"

    def writelog(self):
        with open("log.txt", "a") as file:
            log = self.useraccess()
            file.write(log)
            print('Successfully logged action!')
        
class CourierMenu(CourierLog, SaveLoad):
    '''Class CourierMenu implemets a courier menu with a fucntionality to CRUD couriers
        and save changes to a CSV'''
    def __init__(self, filename: str, name: str):
        CourierLog.__init__(self, name)
        SaveLoad.__init__(self, filename)
        self.courier_list = []
        self.load_data()

    def load_data(self):
        return super().load_data(info_type = self.courier_list)

    def save_data(self):
        return super().save_data(fieldnames =['Name', 'Phone'], info_type = self.courier_list )    

    def view_courier(self):
        '''Display couriers that have been loaded
        Returns:
            dataframe of current couriers'''
        
        print('Courier information:')
        try:
            df = pd.read_csv(self.filename)
            print(df.to_string())
        except Exception as e:
            print(f"Error: {e}")
            raise Exception

    def create_couriers(self):
        '''User input to create a new courier
        Returns: 
        Boolean value indicating if courier has been successfully added or not'''
        
        new_courier = input('What is the name of the new courier?: ').title()
        new_phone = input('Please enter their phone number: ')
        new_courier_dict = {'Name': new_courier, 'Phone': new_phone}
        self.courier_list.append(new_courier_dict)
        super().create_courier_log(new_courier, new_phone)
        return True       

    def update_couriers(self):
        '''Updates existing courier
        
        Returns:
        
        Boolean value indicating if courier has been successfully updated
        '''
        try:
            user_index = int(input('Index value of the product you wish to update: ')) 
            courier_to_change = self.courier_list[user_index]
            for key, value in courier_to_change.items():
                print(key, ':', value)

            courier_new = input('What is the new courier name?: ').title()  
            phone_new = input('What is the new phone number?: ')

            if courier_new == '':
                courier_new = 'Name Unchanged' 
                print('Name will not be updated')
            else:
                courier_to_change['Name'] = courier_new

            if phone_new == '':
                phone_new = 'Phone Number Unchanged' 
                print('Phone number will not be updated')
            else:
                courier_to_change['Phone'] = phone_new    

        except (IndexError, ValueError):
            print('You have selected an invalid index number.')
            return False
        else: 
            print('You have successfully updated this courier!')    

        super().update_courier_log(courier_new, phone_new)
        print('You have successfully updated this product!')      
        return True

    def delete_couriers(self):
        try:
            user_index = int(input('Index value of the courier you wish to delete: '))    
            del self.courier_list[user_index]
  
        except (IndexError, ValueError):
            print('You have selected an invalid index number.') 

        else:
            print('You have successfully deleted this courier!')    
  
        super().delete_product_log(self.product_list[user_index])

x = CourierMenu('couriers.csv','Matt')
print(x.useraccess())
x.view_courier()
x.create_couriers()
print(x.useraccess())
x.writelog()
x.save_data()
x.load_data()
x.view_courier()
