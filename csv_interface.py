#%% MODULE BEGINS

module_name = 'csv_interface'

'''
Version: 3

Description:
    The child class that read and interpret data from a csv file

Authors:
    Brennan Kimbrell
    Trent Law 
    morgan montet 

Date Created     :  11/19/2024
Date Last Updated:  11/26/2024

Doc:
    <***>

Notes:
    <***>
'''

#%% IMPORTS                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from csv_input import P1
#custom imports

from config import C_headers
from config import log

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
        log.info("search value start")
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
        log.info("search value finished")
        return False


    # Function to search and display the DataFrame
    def search_dataframe(self, df, search_term, comparison_operator=None, column=None):
        log.info("search dataframe start")
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
        log.info("search dataframe finished")
        return filtered_rows

    #end of search method

#end of class

    def scatter_plot(self, dataframe, column1, column2, user_title, output ='Output/scatter_plot.pdf', **kwargs):
        log.info("scatter plot start")
        try:
            dataframe.plot.scatter(column1, column2, title= user_title, **kwargs)
            plt.savefig(output)
        #
        except:
            print('error, make sure the column you gave only have number values.')
            log.error("scatter plot code crashed")
        #
    log.info("scatter plot finished")
    # end of scatter plot method

    def violin_plot(self, dataframe, column1, column2, user_title, output ='Output/violin_plot.pdf', **kwargs):
        log.info("violin plot start")
        try:
            sns.violinplot(data=dataframe, x=column1, y=column2, **kwargs)
            plt.title(user_title)
            plt.savefig(output)
        #
        except:
            print('error, make sure you gave one string column and one with numbers.')
            log.error("violin plot code crashed")
        #
    log.info("violin plot finished")
    #end of violin plot method

    def whisker_box_plot(self, dataframe, column1, user_title, output='Output/whisker_box_plot.pdf', **kwargs):
        log.info("whisker box plot start")
        try:
            dataframe.boxplot(column1, **kwargs)
            plt.title(user_title)
            plt.savefig(output)
        #
        except:
            print('error, make sure the columns you specified can be made into a box plot.')
            log.error("whisker box plot code crashed")
        #
    log.info("whisker box plot finished")
    #end of whisker box plot method