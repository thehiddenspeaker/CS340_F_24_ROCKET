#%% MODULE BEGINS
module_name = 'pkl_use'

'''
Version: 5

Description:
    use the pkl file for various functions, child of pkl_input

Authors:
    Brennan Kimbrell 
    morgan montet 
    Trent Law

Date Created     :  11/26/2024
Date Last Updated:  12/6/2024

Doc:
    <***>

Notes:
    <***>
'''

#%% IMPORTS                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import pandas as pd
import numpy as np
import itertools
#custom imports
from pkl_input import pkl_input
from config import log

#other imports
from   copy       import deepcopy as dpcpy
import numpy  as np
from   matplotlib import pyplot as plt
import itertools
'''

import mne
 
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

    def __init__(self):
        super().__init__()

    #Function definitions Start Here
    def mean(self, data_frame, user_axis = 0):
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
            super().csv_print('mean', mean_result)

        except:
            log.error('mean method crashed')

        log.info('mean ended')
    # end of mean method

    def median(self, data_frame, user_axis = 0):
        log.info('median started')
        try:
            # Filter out non-numeric columns
            numeric_data = data_frame.select_dtypes(include=['number'])

            # Calculate the median on the filtered numeric data
            median_result = numeric_data.median(axis=user_axis)

            # Print the result
            super().csv_print('median', median_result)
        except:
            log.error('median method crashed')
        log.info('median ended')
    #end of median method

    def standard_deviation(self, data_frame, user_axis = 0):
        log.info('std started')
        try:
            # Filter out non-numeric columns
            numeric_data = data_frame.select_dtypes(include=['number'])

            # Calculate the standard deviation on the filtered numeric data
            standard_deviation_result = numeric_data.std(axis=user_axis)

            # Print the result
            super().csv_print('std', standard_deviation_result)
        except:
            log.error('std method crashed')
        log.info('std ended')
    # method end

    def joint_count(self, data_frame, columns, write = True):
        log.info('joint count start')
        try:
            joint_count_result = data_frame.groupby(columns).size()
            if write:
                super().csv_print('joint_count', joint_count_result)
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
                super().csv_print('joint_probability', joint_probabilities)
            #
        except:
            log.error('joint probability crashed')
        log.info('joint probability ended')
        return joint_probabilities
    #joint probability

    def conditional_probability(self, df, columns_a, columns_b):
        log.info('conditional probability start')
        try:
            #getting the joint prob of the 2 colums
            joint_prob = pd.crosstab(df[columns_a], df[columns_b], normalize='all')

            # Calculate the marginal probability P(B) (probability of event B)
            marginal_prob_b = self.joint_probability(df, columns_b, write=False)

            conditional_probabilities = joint_prob / marginal_prob_b
            super().csv_print('conditional_probabilities', conditional_probabilities)
        except:
            log.error('conditional probability code crashed')

        log.info('conditional probability ended')
    # conditional probability

    # Function to calculate the magnitude of a vector
    def magnitude(self, vector):
        return np.linalg.norm(vector)

    # Function to calculate the unit vector
    def unit_vector(self, vector):
        return vector / self.magnitude(vector) if self.magnitude(vector) != 0 else np.zeros_like(vector)
    #end unit_vector
    # Function to calculate the projection of P onto Q
    def projection(self,P, Q):
        dot_product_PQ = np.dot(P, Q)
        magnitude_Q_squared = np.dot(Q, Q)
        return (dot_product_PQ / magnitude_Q_squared) * Q
    #end projection vector
    # Function to calculate the dot product of P and Q
    def dot_product(self, P, Q):
        return np.dot(P, Q)
    #end dot_product
    def create_plot(self, df, column, title, llimit, hlimit):
        plt.figure(figsize=(10,5))
        ax = plt.gca()
        for i in range(len(df)):
            # Get the vector components

            vector = df[column][i]

            # Plot the vector as an arrow
            ax.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color='b', width=0.005)

        # Adjusting the plot to display the vectors nicely
        plt.xlim(-1, llimit)
        plt.ylim(-1, hlimit)
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.grid(True)
        plt.gca().set_aspect('equal', adjustable='box')

        # Labels and title
        plt.xlabel('attack_raw')
        plt.ylabel('attack_display')
        plt.title(title)

        # Display the plot
        plt.savefig('Output/'+title)
    #end create_plot
    def angle_between(self, P, Q):
        cos_theta = np.dot(P, Q) / (self.magnitude(P) * self.magnitude(Q))
        theta_rad = np.arccos(np.clip(cos_theta, -1.0, 1.0))  # Clip value to avoid numerical errors
        return np.degrees(theta_rad)
    # end of angle between
    def is_orthogonal(self, P, Q):
        return np.isclose(self.dot_product(P, Q), 0)
    # end orthogonal
    
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
    def vectorDF(self,df, col1, col2, Q):
        position_vectors = []
        magnitudes = []
        unit_vectors = []
        projections = []
        dot_products = []
        angles = []
        orthogonality = []

        # columns to read from
        row1= col1

        row2 = col2

        # Iterate over each row and calculate the vectors and dot product
        for index, row in df.iterrows():
            # Extract weapon attack (A_w) and elemental attack (A_e) from the DataFrame row
            A_w = row[row1]  # Weapon attack (x-component)
            A_e = row[row2]  # Elemental attack (y-component)

            # Define the position vector P
            P = np.array([A_w, A_e])

            # Calculate the magnitude of the position vector P
            magnitude_P = self.magnitude(P)

            # Calculate the unit vector of P
            P_hat = self.unit_vector(P)

            # Calculate the projection of P onto Q
            proj_P_on_Q = self.projection(P, Q)

            # Calculate the dot product of P and Q
            dot_PQ = self.dot_product(P, Q)

            orthogonal = self.is_orthogonal(P, Q)
            # Calculate the angle between P and Q
            angle_PQ = self.angle_between(P, Q)
            # Append the results to the respective lists
            position_vectors.append(P)
            magnitudes.append(magnitude_P)
            unit_vectors.append(P_hat)
            projections.append(proj_P_on_Q)
            dot_products.append(dot_PQ)
            angles.append(angle_PQ)
            orthogonality.append(orthogonal)

        # Create a new DataFrame to store the results
        df_results = pd.DataFrame({
            'attack_raw': df['attack_raw'],
            'attack_display': df['attack_display'],
            'position_vector': position_vectors,
            'magnitude': magnitudes,
            'unit_vector': unit_vectors,
            'projection': projections,
            'dot_product': dot_products,
            'angle_with_Q': angles,
            'Orthogonality': orthogonality
        })
        return df_results
    #
#end of class pkl_use