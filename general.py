print('Welcome, I\'m importing a couple of modules.')

from slotpy import Ourcoolapp
import tkinter as tk

# Create tkinter window
window = tk.Tk()
# Call Ourcoolapp
Ourcoolapp(window)
# Let the window loop
window.mainloop()

'''
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
'''

