#%% MODULE BEGINS
module_name = 'csv_parent'

'''
Version: 3

Description:
    The parent class that read and interpret data from a csv file

Authors:
    Brennan Kimbrell
    Trent Law 
    morgan montet 

Date Created     :  11/19/2024
Date Last Updated:  11/20/2024

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
from matplotlib import pyplot as plt

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

        with open('Input/dict.csv', 'r') as file:
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

    def histogram_plot(self, dataframe, column1, bin_number, user_title):
        try:
            dataframe.hist(column1,bins=int(bin_number), edgecolor='black')
            plt.title(user_title)
            plt.xlabel(column1)
            plt.ylabel('Frequency')
            plt.tight_layout()
            plt.savefig('Output/histogram_plot.pdf')
        #
        except:
            print('error, make sure the columns you specified can be made into a histogram.')

    #end of histogram plot

    def line_plot(self, dataframe, column1, user_title):
        try:
            # Create a line plot for the specified column
            dataframe[column1].plot(kind='line', figsize=(10, 6))

            # Adding title and labels
            plt.title(user_title)
            plt.xlabel('Index')
            plt.ylabel(column1)  # Y-axis will be the values from the column

            # turns graph into pdf
            plt.savefig('Output/line_plot.pdf')
        except:
            print('error, make sure the columns you specified can be made into a line plot.')

    #end of line plot

#end of class




