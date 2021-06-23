# Reads data
print('importing dataframe')
import vaex
import os

class DataFrame():
    '''basic things like reding in data'''
    def __init__(self,path):
        # check if path is valid
        if os.path.isfile(path):
            self.path = path
        else:
            self.path = 'None'
            self.msg = 'Please enter valid path'

    def read_data(self):
        '''reads data, this currently works only it the file has the correct format.
        We can add some functionality here'''
        self.df = vaex.open(self.path)

    def do_something_with_data(self):
        # maybe we want to pre-process the data somehow?
        pass




