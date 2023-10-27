# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 13:36:45 2023

@author: ila
"""

import pandas as pd


class DataLoader():
    
    def __init__(self):
        pass
    
    def take_a_subset(df, chunk_size=140000, read_as_csv=False):
        """ returns a subset of the input df with the 'chunk_size' number of rows """
        
        df_sub = df.iloc[:chunk_size, :]
        if read_as_csv:
            df_sub.to_csv('Trips_subset.csv', index=False)
        return df_sub
    
    def read_data(file_path):
        return pd.read_csv(file_path)