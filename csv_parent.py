#%% MODULE BEGINS
module_name = 'csv_parent'

'''
Version: 2

Description:
    The parent class that read and interpret data from a csv file

Authors:
    Brennan Kimbrell
    Trent Law 
    morgan montet 

Date Created     :  11/19/2024
Date Last Updated:  11/19/2024

Doc:
    <***>

Notes:
    <***>
'''

#%% IMPORTS                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#custom imports
from config import C_headers

#other imports

import csv
import sys
import requests
import pandas as pd

#%% CONSTANTS                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#%% CONFIGURATION               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
header = C_headers



#%% INITIALIZATIONS             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#%% DECLARATIONS                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#Global declarations Start Here



#Class definitions Start Here
class P1:


#Function definitions Start Here
    def __init__(self):
        print("initialized p1")
    #


    def todict(self):
      empty_Dictionary = {header: None for header in header}
      return empty_Dictionary
    #

    def search(self, user_input):
        matching_rows = []  # List to store rows that match the user input

        with open('dict.csv', 'r') as file:
            csv_file = csv.reader(file, delimiter=",")

            # Iterate through the rows in the CSV file
            for row in csv_file:
                # Iterate over each column in the row
                for cell in row:
                    # Compare user_input with each cell (convert to string for comparison)
                    if str(user_input) == str(cell):
                        matching_rows.append(row)  # Add the matching row to the list
                        break  # No need to check further cells in this row
                    #if ends
                #for cell in row ends
            #for row in csv_file ends

        # Return the list of matching rows (empty if none found)
        return matching_rows
#end of class


