#%% MODULE BEGINS
module_name = 'csv_child'

'''
Version: 2

Description:
    The child class that read and interpret data from a csv file

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
from csv_parent import P1
#custom imports

from config import C_headers

#other imports
import csv
import requests
import pandas as pd

#%% CONSTANTS                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#%% CONFIGURATION               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




#%% INITIALIZATIONS             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#%% DECLARATIONS                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#Global declarations Start Here



#Class definitions Start Here
class C1(P1):


#Function definitions Start Here
    def __init__(self):

        print("initialized p1")
    #

    def toDF(self, filename,head):
        self.df = pd.read_csv(filename, header=None, names=head, skiprows= 1)
        return self.df
    #

    def search(self, user_input):

     return 0


    def search_value(self, val, search_term, comparison_operator=None):

        try:
            search_term = float(search_term)
            print(search_term)
        #
        except ValueError:
            search_term = str(search_term)
            print(search_term)
        #

        if isinstance(val, str):
            return search_term.lower() in val.lower()


        # If the value is numeric (int or float), perform >, < or exact comparisons
        if isinstance(val, (int, float)):
            if comparison_operator == '>':
                return val > search_term
            elif comparison_operator == '<':
                return val < search_term
            else:
                return val == search_term  # Default is exact match
        return False


    # Function to search and display the DataFrame
    def search_dataframe(self, df, search_term, comparison_operator=None, column=None):
        if column:
            # Filter the DataFrame to the selected column (which will be a Series)
            filtered_column = df[column]

            # Create the boolean mask using apply
            boolean_mask = filtered_column.apply(lambda x: self.search_value(x, search_term, comparison_operator))

            # Apply boolean indexing to filter rows where the column matches the condition
            filtered_rows = df[boolean_mask]  # Boolean indexing to filter rows
        else:
            # Create the boolean mask using applymap for the entire DataFrame
            boolean_mask = df.applymap(lambda x: self.search_value(x, search_term, comparison_operator))

            # Apply boolean indexing using .any(axis=1) to filter rows where any column matches the condition
            filtered_rows = df[boolean_mask.any(axis=1)]  # Boolean indexing for any match in a row
        print(":", boolean_mask)
        return filtered_rows

    #end of search method

#end of class