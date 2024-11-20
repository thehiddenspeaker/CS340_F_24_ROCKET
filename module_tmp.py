#Version: v0.1
#Date Last Updated: 12-20-2023

#%% STANDARDS   -DO NOT include this block in a new module
'''
Unless otherwise required, use the following guidelines
* Style:
    - Write the code in aesthetically-pleasing style
    - Names should be self-explanatory
        - "the main variable designator_variable group name": "child_parent"
            - pm_single, not singlepm, dataDf_grpL_1 , not dataDf_grpL1; "_1" is safer for bugs.
    - Comment adequately.
        - Add a comment for each code block, such as a loop-block, that describe the functionality
    - Use relative path
    - Use generic coding instead of manually-entered constant values
    - Legends should be good enough in color, linestyle, shape etc. to distinguish data series.
    - Always test your code with an artificial data whose return value is known.
    - Add the symbol # at the end of EACH block.
    - Sort imports aphabetically
 
* Performance and Safety:
    - Avoid use of global variables. If needed, use cautiously. Add suffix 
        - "_gl" to global variables
        - "_ui" to the user interface variables    
    - Code must be efficient (data-structure, functionality).
    - Avoid if-block in a loop-block unless it is required.
    - Do not calculate a common/constant value inside a loop.
    - Avoid declarations in a loop-block unless it is required.
    - Avoid initializing variables inside a loop unless it is required.
    - Initialize an array if size is known.
    - Save data in categorized folders.
    - import only the components from a package/module to be used instead of entire one.

    - Avoid using global scope
    - Prefer to use immutable types
    - Use deep-copy
    - Use [None for i in Sequence] instead of [None]*len(Sequence)
    - Initialize objects with None (null) (NOT zero) if their size is known instead of using append-like methods.
    - Operations with dataframe
        - Sort by the same column  name, and then reset index. As an example,
            grid_EntrpAll = x_trans.value_counts(subset=featureLst,normalize=True)
            reset_index().sort_values(featureLst).reset_index()
    - Utilize process logging


'''

#%% MODULE BEGINS
module_name = 'main'

'''
Version: 2

Description:
    <***>

Authors:
    Brennan Kimbrell
    Trent Law 
    Morgan Montet

Date Created     :  11/19/2024
Date Last Updated:  11/19/2024

Doc:
    <***>

Notes:
    <***>
'''

#%% IMPORTS                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
   import os
   import pandas as pd
   import ast
   #os.chdir("./../..")
#

#custom imports
from csv_parent import P1
from csv_child import C1

#other imports
from   copy       import deepcopy as dpcpy
import pandas as pd
import numpy  as np
'''
from   matplotlib import pyplot as plt
import mne

import os

import seaborn as sns
'''
#%% USER INTERFACE              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#%% CONSTANTS                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#%% CONFIGURATION               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


#%% INITIALIZATIONS             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#%% DECLARATIONS                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Global declarations Start Here



#Class definitions Start Here



#Function definitions Start Here
def main():

    csv_child = C1()
    csv_parent = P1()
    headers = csv_child.todict()
    df = csv_child.toDF("dict.csv", headers)

    print(headers)
    print(df)
    #csv_child = C1()

    '''
    #searh test with child class
    user_input = input('Enter a column name to search in:')
    input_search = input('Enter an integer or string to search for:')
    input_operator = input('Enter an operator to search with(<, =, >, ect):')

    print(input_operator)
    print(csv_child.search_dataframe(df, input_search, input_operator, user_input))

    #search test with parent class
    user_input = input('Enter a string/number to search: ')
    search_test = csv_parent.search(user_input)

    #print the list vertical if the list is returned with data in it
    if search_test:
        for row in search_test:
            print(row)
        #
    #
    '''
    #scatter plot test
    csv_child.scatter_plot(df, 'attack_display', 'attack_raw')


    pass
#end of main

#%% MAIN CODE                  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Main code start here



#%% SELF-RUN                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Main Self-run block
if __name__ == "__main__":

    print(f"\"{module_name}\" module begins.")
    
    #TEST Code
    main()