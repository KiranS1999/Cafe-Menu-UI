#COURIER-RELATED FUNCTIONS#

from csv_functions.csv_load import save_courier_list
import pandas as pd 

#FUNCTION: View couriers with pandas
def view_couriers_csv():
    print('Courier information:')
    df = pd.read_csv('example_data\couriers.csv')
    print(df.to_string())
    print() 

#FUNCTION: create a new courier to csv
def new_courier_csv():
    new_courier = input('What is the name of the new courier?: ').title()
    new_phone = input('Please enter their phone number: ')
    new_courier_dict = {'Name': new_courier, 'Phone': new_phone}
    couriers.append(new_courier_dict)
    print('The current courier list:')
    save_courier_list()
    view_couriers_csv()
       
#FUNCTION: update a courier to csv
def update_courier_csv():

    try:
        view_couriers_csv()
        user_index = int(input('Index value of the product you wish to update: ')) 
        courier_to_change = couriers[user_index]
        for key, value in courier_to_change.items():
            print(key, ':', value)

        courier_new = input('What is the new courier name?: ').title()  
        phone_new = input('What is the new phone number?: ')

        if courier_new == '': 
            print('Name will not be updated')
        else:
            courier_to_change['Name'] = courier_new

        if phone_new == '': 
            print('Phone number will not be updated')
        else:
            courier_to_change['Phone'] = phone_new    

        save_courier_list()
        view_couriers_csv()
        

    except (IndexError, ValueError):
        print('You have selected an invalid index number.')

    else: 
        print('You have successfully updated this courier!')     
      
#FUNCTION: delete a courier to csv
def del_courier_csv():  

    try:
        view_couriers_csv()
        user_index = int(input('Index value of the courier you wish to delete: '))    
        del couriers[user_index]
        save_courier_list()
        view_couriers_csv()
               
    
    except (IndexError, ValueError):
        print('You have selected an invalid index number.') 

    else:
        print('You have successfully deleted this courier!')    
  