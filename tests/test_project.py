from src.csv_functions import csv_load

from unittest.mock import patch, mock_open
import unittest

from pandas.util.testing import assert_frame_equal

import pandas as pd

#TEST- open correct file
@patch("builtins.open", new_callable=mock_open, read_data="data")
#test if function is inputing orders data
def test_load_order_data(mock_open):
    load_order_data()
    mock_open.assert_called_with('orders.csv', 'r', newline ='')
    assert open("orders.csv").read() == "data"

@patch("builtins.open", new_callable=mock_open, read_data="data")
#test if function is inputing products data
def test_load_product_data(mock_open):
    load_product_data()
    mock_open.assert_called_with('products.csv', 'r', newline ='')
    assert open("products.csv").read() == "data"

@patch("builtins.open", new_callable=mock_open, read_data="data")
#test if function is inputing couriers data
def test_load_courier_data(mock_open):
    load_courier_data()
    mock_open.assert_called_with('couriers.csv', 'r', newline ='')
    assert open("couriers.csv").read() == "data"


#TESTING- PRODUCT-RELATED FUNCTIONS
# test dataframe
colnames = ['Product', 'Price']
class DFTests(unittest.TestCase):
    def setUp(self):
        test_file_name =  'products.csv'
        data = pd.read_csv(test_file_name,
            sep = ',',
            header = 0)
        self.fixture = data

    #Check column names
    def test_columns(self):
        self.assertListEqual(list(self.fixture.columns), colnames)

def test_create_product():
    with patch('builtins.input') as mock_input:
        mock_input.side_effect = ['Juice', '0.98']
        actual = create_product_csv()
        assert mock_input.call_count == 2

    


