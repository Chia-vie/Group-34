# Reads data
print('importing dataframe')
import vaex
import os
import pandas as pd
import numpy as np

def dummydata():
    df = vaex.example()
    return df

def dummydata2():
    """ for plot_type2 """
    cwd = os.getcwd().rstrip("App")
    file = os.path.join(cwd, "examples/example_data/run_GGM_1M_CRlER_norm_st.csv")
    df = pd.read_csv(file, index_col="Unnamed: 0", float_precision='round_trip')
    slider_cols = np.array([c for c in df.columns if 'R_' in c])
    return df, slider_cols

class DataFrame():
    '''basic things like reading in data'''
    def __init__(self,path):
        # check if path is valid
        if os.path.isfile(path):
            self.path = path
        else:
            self.path = 'None.'
            self.msg = 'Please enter a valid path!'

    def to_csv(self):
        # turn input into csv
        if self.path.endswith('.csv'):
            new_path = self.path
        else:
            os.system("tr -s '[:blank:]' ',' < " + self.path + " > " + self.path + ".csv")
            new_path = self.path + '.csv'

    def read_data(self, path_to_csv):
        '''
        We can add some functionality here
        '''
        self.df = vaex.open(path_to_csv)
        print('Success!\n')
        print('I read in the following file:\n')
        print(path_to_csv)