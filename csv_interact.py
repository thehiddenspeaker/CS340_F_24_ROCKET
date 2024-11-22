#%% MODULE BEGINS

module_name = 'csv_interact'

'''
Version: 2

Description:
    The child class that read and interpret data from a csv file

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
from csv_inherit import P1
#custom imports

from config import C_headers

#other imports
import csv
import requests
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

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

    def scatter_plot(self, dataframe, column1, column2, user_title):
        try:
            dataframe.plot.scatter(column1, column2, title= user_title)
            plt.show()
        #
        except:
            print('error, make sure the column you gave only have number values.')
        #
    # end of scatter plot method

    def violin_plot(self, dataframe, column1, column2, user_title):
        try:
            sns.violinplot(dataframe, x=column1, y=column2)
            plt.title(user_title)
            plt.show()
        #
        except:
            print('error, make sure you gave one string column and one with numbers.')
        #

    #end of violin plot method

    def whisker_box_plot(self, dataframe, column1, user_title):

        try:
            dataframe.boxplot(column1)
            plt.title(user_title)
            plt.show()
        #
        except:
            print('error, make sure the columns you specified can be made into a box plot.')
        #

    #end of whisker box plot method