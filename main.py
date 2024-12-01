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
    position = 0
    with open('Input/user_input', 'r') as file:
        file_input = file.read().splitlines()
    #end of file open statement


    # defining child and parent
    csv_child = C1()
    csv_parent = P1()
    pkl_child = pkl_use()
    pkl_parent = pkl_input()
    # retriving headers through parent for config
    headers = csv_child.todict()
    # create data frame
    df = csv_child.toDF(file_input[position], headers)
    position +=1
    # print data
    print(df)


    #searh test with child class
    user_input = file_input[position]#Column
    position += 1
    input_search = file_input[position]#integer searched for
    position += 1
    input_operator = file_input[position]# operator
    position += 1


    #print(input_operator)
    print(csv_child.search_dataframe(df, int(input_search), input_operator, user_input))

    #search test with parent class
    user_input = file_input[position]
    position += 1

    search_test = csv_parent.search(user_input)
    #print the list vertical if the list is returned with data in it
    if search_test:
        for row in search_test:
            print(row)
        #
    #

    #scatter plot test
    print("Scatter Plot")
    user_input_column1 = file_input[position]#column 1
    position +=1
    user_input_column2 = file_input[position]#column 2
    position += 1
    user_input_title = file_input[position]#title
    position +=1

    csv_child.scatter_plot(df, user_input_column1, user_input_column2, user_input_title)



    #violen plot test
    print("Violin plot:")
    user_input_column1 = file_input[position]  # column 1
    position += 1
    user_input_column2 = file_input[position]  # column 2
    position += 1
    user_input_title = file_input[position]  # title
    position += 1

    csv_child.violin_plot(df, user_input_column1, user_input_column2, user_input_title)



    #whisker box plot test
    print("whisker box plot:")
    user_input = file_input[position]  # column names
    position += 1

    # turns users input into a list
    columns_list = [col.strip() for col in user_input.split(',')]

    user_input_title = file_input[position]#whisker title
    position += 1

    csv_child.whisker_box_plot(df, columns_list, user_input_title)



    #histogram plot test
    print("Histogram:")
    user_input_column1 = file_input[position]  # column names
    position += 1
    user_input_bin = file_input[position]  # bin count
    position += 1
    user_input_title = file_input[position]  # title
    position += 1

    csv_parent.histogram_plot(df, user_input_column1, user_input_bin, user_input_title)



    #line plot test
    print("Line Plot")
    user_input_column1 = file_input[position]  # column names
    position += 1
    user_input_title = file_input[position]  # title
    position += 1

    csv_parent.line_plot(df, user_input_column1, user_input_title)


    # pkl test

    pkl_child.mean(df)
    pkl_child.median(df)
    pkl_child.standard_deviation(df)
    pkl_child.joint_count(df, file_input[position])
    position += 1
    pkl_child.joint_probability(df, file_input[position])
    position+=1
    pkl_child.conditional_probability(df, file_input[position], file_input[position+1])
    position+=2


    # Define a vector Q (for projection calculations, you can replace it with your desired vector)
    Q = np.array([int(file_input[position]), int(file_input[position+1])])# Example vector Q = (0, 10)
    position+=2


    # Lists to store the calculated values
    position_vectors = []
    magnitudes = []
    unit_vectors = []
    projections = []
    dot_products = []
    angles = []
    orthogonality = []

    #columns to read from
    row1 =file_input[position]
    position+=1
    row2=file_input[position]
    position+=1
    # Iterate over each row and calculate the vectors and dot product
    for index, row in df.iterrows():
        # Extract weapon attack (A_w) and elemental attack (A_e) from the DataFrame row
        A_w = row[row1]  # Weapon attack (x-component)
        A_e = row[row2]  # Elemental attack (y-component)

        # Define the position vector P
        P = np.array([A_w, A_e])

        # Calculate the magnitude of the position vector P
        magnitude_P = pkl_child.magnitude(P)

        # Calculate the unit vector of P
        P_hat = pkl_child.unit_vector(P)

        # Calculate the projection of P onto Q
        proj_P_on_Q = pkl_child.projection(P, Q)

        # Calculate the dot product of P and Q
        dot_PQ = pkl_child.dot_product(P, Q)

        orthogonal = pkl_child.is_orthogonal(P, Q)
        # Calculate the angle between P and Q
        angle_PQ = pkl_child.angle_between(P, Q)
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
    print(df_results)
    df_results.to_csv(file_input[position])
    position+=1
    pkl_child.create_plot(df_results, file_input[position], file_input[position+1], int(file_input[position+2]), int(file_input[position+3]))
    position+=4
    pkl_child.create_plot(df_results, file_input[position], file_input[position+1], int(file_input[position+2]), int(file_input[position+3]))
    position+=4
    pkl_child.create_plot(df_results, file_input[position], file_input[position+1], int(file_input[position+2]), int(file_input[position+3]))




    log.info("main finished")
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