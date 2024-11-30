# %% MODULE BEGINS
module_name = 'main'

'''
Version: 3

Description:
    <***>

Authors:
    Brennan Kimbrell
    Trent Law 
    Morgan Montet

Date Created     :  11/19/2024
Date Last Updated:  11/20/2024

Doc:
    <***>

Notes:
    <***>
'''

# %% IMPORTS                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
    from config import log
    import os
    import pandas as pd
    import ast
    from matplotlib.pyplot import violinplot
    # os.chdir("./../..")
#

# custom imports
from csv_input import P1
from csv_interface import C1
from pkl_use import pkl_use
from pkl_input import pkl_input

# other imports
from copy import deepcopy as dpcpy
import pandas as pd
import numpy as np

'''
from   matplotlib import pyplot as plt
import mne

import os

import seaborn as sns
'''
# %% USER INTERFACE              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# %% CONSTANTS                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# %% CONFIGURATION               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


# %% INITIALIZATIONS             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# %% DECLARATIONS                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Global declarations Start Here


# Class definitions Start Here


# Function definitions Start Here
def main():
    log.info("Main started")
    # defining child and parent
    csv_child = C1()
    csv_parent = P1()
    pkl_child = pkl_use()
    pkl_parent = pkl_input()
    # retriving headers through parent for config
    headers = csv_child.todict()
    # create data frame
    df = csv_child.toDF("Input/dict.csv", headers)
    # print data
    print(headers)
    print(df)

    '''
    #searh test with child class
    user_input = input('Enter a column name to search in:')
    input_search = input('Enter an integer or string to search for:')
    input_operator = input('Enter an operator to search with(<, =, >, ect):')

    print(input_operator)
    print(csv_child.search_dataframe(df, input_search, input_operator, user_input))

    #search test with parent class
    user_input = input('Enter a string/number to search: ')
   # file_path = input('Enter the path of the csv file: ')
    search_test = csv_parent.search(user_input)
    #print the list vertical if the list is returned with data in it
    if search_test:
        for row in search_test:
            print(row)
        #
    #

    #scatter plot test
    print("Scatter Plot")
    user_input_column1 = input('please input the column you want x to be: ')
    user_input_column2 = input('please input the column you want y to be: ')
    user_input_title = input('please input the title of your graph: ')

    csv_child.scatter_plot(df, user_input_column1, user_input_column2, user_input_title)



    #violen plot test
    print("Violin plot:")
    user_input_column1 = input('please input the column you want x to be: ')
    user_input_column2 = input('please input the column you want y to be: ')
    user_input_title = input('please input the title of your graph: ')

    csv_child.violin_plot(df, user_input_column1, user_input_column2, user_input_title)



    #whisker box plot test
    print("whisker box plot:")
    user_input = input('Enter the column names (comma-separated): ')

    # turns users input into a list
    columns_list = [col.strip() for col in user_input.split(',')]

    user_input_title = input('please input the title of your graph: ')

    csv_child.whisker_box_plot(df, columns_list, user_input_title)



    #histogram plot test
    print("Histogram:")
    user_input_column1 = input('please input the column you want x to be: ')
    user_input_bin = input('please input the amount of bins that graph should have: ')
    user_input_title = input('please input the title of your graph: ')

    csv_parent.histogram_plot(df, user_input_column1, user_input_bin, user_input_title)



    #line plot test
    print("Line Plot")
    user_input_column1 = input('please input the column you want x to be: ')
    user_input_title = input('please input the title of your graph: ')

    csv_parent.line_plot(df, user_input_column1, user_input_title)
    log.info("main finished")
    '''
    # pkl test

    pkl_child.mean(df)
    pkl_child.median(df)
    pkl_child.standard_deviation(df)
    pkl_child.joint_count(df, 'rarity')
    pkl_child.joint_probability(df, 'element_type')
    pkl_child.conditional_probability(df, 'rarity', 'attack_display')
    pkl_child.unique(df, 'id')

    pass


# end of main

# %% MAIN CODE                  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main code start here


# %% SELF-RUN                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main Self-run block
if __name__ == "__main__":
    print(f"\"{module_name}\" module begins.")

    # TEST Code
    main()