import os

print('Welcome, I\'m importing a couple of modules.')

from dataframe import DataFrame
from plotter import Plotter
from buildgui import Ourcoolapp

# eventually this has to be some sort of open file button
path = input('Please enter path to your file')

# check if path is valid and if so read data
while True:
    df = DataFrame(path)
    if df.path == path:
        df.read_data()
        break
    else:
        path = input(df.msg)

