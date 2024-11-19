#%% MODULE BEGINS
module_name = 'csv_parent_child'

'''
Version: 1

Description:
    The parent and child class that read and interpret data from a csv file

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


    def todict(self):
      empty_Dictionary = {header: None for header in header}
      return empty_Dictionary


