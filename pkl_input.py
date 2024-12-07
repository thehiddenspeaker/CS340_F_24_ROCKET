#%% MODULE BEGINS
import pandas as pd

module_name = 'pkl_input'

'''
Version: 3

Description:
    place pkl file into data frame

Authors:
    <***>

Date Created     :  11/26/2024
Date Last Updated:  12/6/2024

Doc:
    <***>

Notes:
    <***>
'''

#%% IMPORTS                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
   import os
   #os.chdir("./../..")
#

#custom imports
from config import log

#other imports
import csv
from   copy       import deepcopy as dpcpy

'''
from   matplotlib import pyplot as plt
import mne
import numpy  as np 
import os
import pandas as pd
import seaborn as sns
'''
#%% USER INTERFACE              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#%% CONSTANTS                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#%% CONFIGURATION               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#%% INITIALIZATIONS             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#%% DECLARATIONS                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Global declarations Start Here



#Class definitions Start Here
class pkl_input:

    def __init__(self):
        pass

    def pickle_to_df(self, file_path= 'Input/data.pkl'):
        df = pd.read_pickle(file_path)
        return df
    # pickle_to_df

    def csv_print(self, name, data, path = 'Output/'):
        log.info('print start')
        try:
            file_name = f'{path}{name}.csv'

            # Open the file in write mode
            with open(file_name, mode='w', newline='') as file:
                writer = csv.writer(file)

                # Write each item (assuming it's iterable) into the CSV file
                for item in data:
                    writer.writerow([item])
        except:
            log.error("somthing went wrong int pkl_input print method")
        #
        log.info('print end')
    # print method end
    pass

    def string_eval(self, user_input):
        log.info("string_eval started")

        x = 10  # Outer variable to demonstrate 'nonlocal'

        def nested_function():
            nonlocal x
            x = eval(user_input)
            return x

        try:
            answer = nested_function()

            self.csv_print('Eval()', [answer])

        except Exception as e :
            log.error(f"Eval failed: {e}")

        log.info("string_eval ended")
    #end of string_eval
#end of class pkl_input