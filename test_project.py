
from csv_functions import load_order_data, load_courier_data, load_product_data, create_product_csv

from unittest.mock import patch, mock_open

from pandas.util.testing import assert_frame_equal

import pandas as pd

#TEST- open correct file
@patch("builtins.open", new_callable=mock_open, read_data="data")
#test if fucntion is inputing orders data
def test_load_order_data(mock_open):
    load_order_data()
    mock_open.assert_called_with('orders.csv', 'r', newline ='')
    assert open("orders.csv").read() == "data"

@patch("builtins.open", new_callable=mock_open, read_data="data")
#test if fucntion is inputing products data
def test_load_product_data(mock_open):
    load_product_data()
    mock_open.assert_called_with('products.csv', 'r', newline ='')
    assert open("products.csv").read() == "data"

@patch("builtins.open", new_callable=mock_open, read_data="data")
#test if fucntion is inputing couriers data
def test_load_courier_data(mock_open):
    load_courier_data()
    mock_open.assert_called_with('couriers.csv', 'r', newline ='')
    assert open("couriers.csv").read() == "data"


#TESTING- PRODUCT-RELATED FUNCTIONS

# def create_product_csv():
#     newprod = input('Please enter your product name: ').title()
#     newprice = input('Please enter the price: ')
#     new_prod_dict = {'Product': newprod, 'Price': newprice}
#     products.append(new_prod_dict)
#     save_product_list()
#     view_products_csv()


# input_mock_newprod = Mock()
# input_mock_newprod.return_value = 'Juice' # mock for first input call

# input_mock_newprice = Mock()
# input_mock_newprice.return_value = '0.98' #mock for second input call

# #put both mocks into another mock so we can patch this into input
# input_mock = Mock() 
# input_mock.side_effect = [input_mock_newprod.return_value, input_mock_newprice.return_value ]

# @patch('csv_functions.save_product_list')
# @patch('csv_functions.view_products_csv')
#mock_save_product_list, mock_view_products_csv

def test_create_product():
    with patch('builtins.input') as mock_input:
        mock_input.side_effect = ['Juice', '0.98']
        
        # mock_save_product_list.return_value = 
        # mock_view_products_csv.return_value = 
        actual = create_product_csv()
        assert mock_input.call_count == 2

        #print(actual) gives none
        #assert actual == [{'Product': 'Juice', 'Price': '0.98'}]
        #dataframe = pd.DataFrame()
        #assert_frame_equal([{'Product': 'Juice', 'Price': '0.98'}], dataframe) == actual


    
    


