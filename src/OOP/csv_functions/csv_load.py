#### LOADING/SAVING CSV FILE ####

import csv
from dataclasses import dataclass, field

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