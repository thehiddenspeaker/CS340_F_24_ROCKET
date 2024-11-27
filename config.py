#%% MODULE BEGINS
module_name = 'config'

'''
Version: 2

Description:
    config for team rockets project 

Authors:
    Brennan Kimbrell
    Trent Law 
    morgan montet 

Date Created     :  11/19/2024
Date Last Updated:  11/20/2024

Doc:
    <***>

Notes:
    <***>
'''
import logging as log

log.basicConfig(filename="Output/log_file.log",
                    format='%(asctime)s %(message)s',
                    filemode='w', level=20)


C_headers = ( 'id','elderseal','rarity','damageType','name','attack_display','attack_raw','element_type','element_damage','element_hidden')
