#### DATABASE CONNECTION CLASS ####


# Import Libraries
import pymysql
import os
from dotenv import load_dotenv


class ConnectDB:
    
    def __init__(self):
        '''
        Initialise environment variables from .env file
        '''

        load_dotenv()
        self.host = os.environ.get("mysql_host")
        self.user = os.environ.get("mysql_user")
        self.password = os.environ.get("mysql_pass")
        self.database = os.environ.get("mysql_db")

    def connect(self):
        '''
        Establish a database connection
        Return: cursor, connection
        '''
        
        connection = pymysql.connect(
            self.host,
            self.user,
            self.password,
            self.database
        )

        cursor = connection.cursor()  
        return cursor, connection