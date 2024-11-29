#%% MODULE BEGINS
module_name = 'pkl_input'

'''
Version: <***>

Description:
    place pkl file into data frame

Authors:
    <***>

Date Created     :  11/26/2024
Date Last Updated:  11/26/2024

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
def csv_print(name, data):
    log.info('print start')
    try:
        file_name = f'{name}.csv'

        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file)

        for row in data:
            writer.writerow(row)
    except:
        log.error("somthing went wrong int pkl_input print method")
    #
    log.info('print end')


class pkl_input:

    def csv_print(self, name, data):
        log.info('print start')
        try:
            file_name = f'{name}.csv'

            with open(file_name, mode='w', newline='') as file:
                writer = csv.writer(file)

            for row in data:
                writer.writerow(row)
        except:
            log.error("somthing went wrong int pkl_input print method")
        #
        log.info('print end')
    # print method end
    pass


#Function definitions Start Here

#end of class pkl_input