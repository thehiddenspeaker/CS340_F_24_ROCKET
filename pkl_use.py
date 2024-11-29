#%% MODULE BEGINS
import logging

module_name = 'pkl_use'

'''
Version: 2

Description:
    use the pkl file for various functions

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


#custom imports
from pkl_input import pkl_input, csv_print
from config import log

#other imports
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
class pkl_use(pkl_input):
    pass


    #Function definitions Start Here
    def mean(self, data_frame, user_axis = 0):
        log.info('mean started')
        try:
            mean_result = data_frame.mean(user_axis, skipna = True)
            csv_print('mean', mean_result)
        except:
            log.error('mean method crashed')
        #
        log.info('mean ended')
    # end of mean method

    def median(self, data_frame, user_axis = 0):
        log.info('median started')
        try:
            median_result = data_frame.median(axis = user_axis)
            csv_print('median', median_result)
        except:
            log.error('median method crashed')
        log.info('median ended')
    #end of median method

    def standard_deviation(self, data_frame, user_axis = 0):
        log.info('std started')
        try:
            standard_deviation_result = data_frame.std(axis=user_axis)
            csv_print('std', standard_deviation_result )
        except:
            log.error('std method crashed')
        log.info('std ended')
    # method end

    def joint_count(self, data_frame, columns, write = True):
        log.info('joint count start')
        try:
            joint_count_result = data_frame.groupby(columns).size()
            if write:
                csv_print('joint_count', joint_count_result)
            #
        except:
            log.error('joint count crashed')
        log.info('joint count finished')
        return joint_count_result
    # joint count method end

    def joint_probability(self, data_frame, columns, write = True):
        log.info('joint probability start')
        try:
            joint_count_result = self.joint_count(data_frame, columns, write=False)
            total_rows = len(data_frame)

            joint_probabilities = joint_count_result / total_rows

            if write:
                csv_print('joint_probability', joint_probabilities)
            #
        except:
            log.error('joint probability crashed')
        log.info('joint probability ended')
        return joint_probabilities
    #joint probability

    def conditional_probability(self, df, columns_a, columns_b):
        log.info('conditional probability start')
        try:
            joint_prob_a_and_b = self.joint_probability(df, columns_a + columns_b, write= False)

            # Calculate the marginal probability P(B) (probability of event B)
            marginal_prob_b = self.joint_probability(df, columns_b, write= False)

            # Conditional Probability P(A | B) = P(A ∩ B) / P(B)
            conditional_probabilities = joint_prob_a_and_b / marginal_prob_b
            csv_print('conditional_probabilities', conditional_probabilities)
        except:
            log.error('conditional probability code crashed')

        log.info('conditional probability ended')
    # conditional probability
#end of class pkl_use