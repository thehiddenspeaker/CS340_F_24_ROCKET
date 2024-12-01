#%% MODULE BEGINS
module_name = 'pkl_use'

'''
Version: 3

Description:
    use the pkl file for various functions, child of pkl_input

Authors:
    Brennan Kimbrell 
    morgan montet 
    Trent Law

Date Created     :  11/26/2024
Date Last Updated:  11/26/2024

Doc:
    <***>

Notes:
    <***>
'''

#%% IMPORTS                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import pandas as pd
import numpy as np
from itertools import combinations, permutations
import itertools

#custom imports
from pkl_input import pkl_input
from config import log

#other imports
from   copy       import deepcopy as dpcpy

'''
from   matplotlib import pyplot as plt
import mne
import numpy  as np 
import os
import seaborn as sns
'''
#%% USER INTERFACE              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#%% CONSTANTS                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#%% CONFIGURATION               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#%% INITIALIZATIONS             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#%% DECLARATIONS                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Global declarations Start Here



#Class definitions Start Here
class pkl_use(pkl_input):
    pass

    def __init__(self):
        super().__init__()

    #Function definitions Start Here
    def mean(self, data_frame, user_axis = 0, file_name = 'mean'):
        log.info('mean started')

        # Check if the DataFrame is empty
        if data_frame.empty:
            log.error('The provided DataFrame is empty')
            return

        # Validate user_axis value
        if user_axis not in [0, 1]:
            log.error(f'Invalid user_axis value: {user_axis}')
            return

        try:
            # Select only numeric columns from the DataFrame
            numeric_columns = data_frame.select_dtypes(include=['number']).columns

            # If there are no numeric columns, log an error
            if numeric_columns.empty:
                log.error('No numeric columns available for mean calculation')
                return

            # Calculate the mean for only the numeric columns
            mean_result = data_frame[numeric_columns].mean(user_axis, skipna=True)


            # If mean_result is a pandas Series, convert it to a list for CSV writing
            if isinstance(mean_result, pd.Series):
                mean_result = mean_result.tolist()

            # Print the mean result to CSV
            super().csv_print(file_name, mean_result)

        except:
            log.error('mean method crashed')

        log.info('mean ended')
    # end of mean method

    def median(self, data_frame, user_axis = 0, file_name= 'median'):
        log.info('median started')
        try:
            # Filter out non-numeric columns
            numeric_data = data_frame.select_dtypes(include=['number'])

            # Calculate the median on the filtered numeric data
            median_result = numeric_data.median(axis=user_axis)

            # Print the result
            super().csv_print(file_name, median_result)
        except:
            log.error('median method crashed')
        log.info('median ended')
    #end of median method

    def standard_deviation(self, data_frame, user_axis = 0, file_name = 'std'):
        log.info('std started')
        try:
            # Filter out non-numeric columns
            numeric_data = data_frame.select_dtypes(include=['number'])

            # Calculate the standard deviation on the filtered numeric data
            standard_deviation_result = numeric_data.std(axis=user_axis)

            # Print the result
            super().csv_print(file_name, standard_deviation_result)
        except:
            log.error('std method crashed')
        log.info('std ended')
    # method end

    def joint_count(self, data_frame, columns, write = True, file_name = 'joint_count'):
        log.info('joint count start')
        try:
            joint_count_result = data_frame.groupby(columns).size()
            if write:
                super().csv_print(file_name, joint_count_result)
            #
        except:
            log.error('joint count crashed')
        log.info('joint count finished')
        return joint_count_result
    # joint count method end

    def joint_probability(self, data_frame, columns, write = True, file_name = 'joint_probability'):
        log.info('joint probability start')
        try:
            joint_count_result = self.joint_count(data_frame, columns, write=False)
            total_rows = len(data_frame)

            joint_probabilities = joint_count_result / total_rows

            if write:
                super().csv_print(file_name, joint_probabilities)
            #
        except:
            log.error('joint probability crashed')
        log.info('joint probability ended')
        return joint_probabilities
    #joint probability

    def conditional_probability(self, df, columns_a, columns_b, file_name ='conditional_probabilities'):
        log.info('conditional probability start')
        try:
            #getting the joint prob of the 2 colums
            joint_prob = pd.crosstab(df[columns_a], df[columns_b], normalize='all')

            # Calculate the marginal probability P(B) (probability of event B)
            marginal_prob_b = self.joint_probability(df, columns_b, write=False)

            conditional_probabilities = joint_prob / marginal_prob_b
            super().csv_print(file_name, conditional_probabilities)
        except:
            log.error('conditional probability code crashed')

        log.info('conditional probability ended')
    # conditional probability

    def unique(self, data_frame, columns, file_name = 'unique'):
        log.info('unique start')
        try:
            res = list(set(data_frame[columns].unique()))
            super().csv_print(file_name, res)
        except:
            log.error('unique method crashed')
        log.info('unique ended')

    def permute(self, data_frame, columns, output='permutations', r=2 ):
        log.info('permutations start')
        try:
            # Get the unique values from the specified column
            unique_values = data_frame[columns].unique()

            # Generate permutations of length r and convert to a list
            perm = list(itertools.permutations(unique_values, r))

            # Convert numpy.int64 to plain int for all elements in the permutation tuple
            perm = [tuple(int(x) for x in p) for p in perm]  # Convert each element in the tuple to int

            # Print all permutations at once (or process them as needed)
            super().csv_print(output, perm)  # Pass the entire list at once
        except:
            log.error('permutations crashed')
        log.info('permutations ended')
    #permutations

    def combine(self, data_frame, columns, output='combinations', r=2):
        log.info('combinations start')
        try:
            # Get the unique values from the specified column and convert them to plain Python types (e.g., int)
            unique_values = data_frame[columns].unique()
            unique_values = [int(value) for value in unique_values]  # Convert numpy.int64 to int

            # Generate combinations of length r
            comb = list(itertools.combinations(unique_values, r))

            # Print all combinations at once (or process them as needed)
            super().csv_print(output, comb)  # Pass the entire list at once
        except:
            log.error('combinations crashed')
        log.info('combinations ended')
    #combinations

#end of class pkl_use