#%% MODULE BEGINS
module_name = 'csv_child'

'''
Version: 1

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
        self.df = pd.read_csv(filename, header=None, names=head)
        return self.df
    #

    def search(self, user_input):
     return 0
    #end of search method

#end of class