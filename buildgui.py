# Color schemes
# http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter

import tkinter as tk
from tkinter import ttk
from plotter import Plotter
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

def pressbutton(choice):
    '''This function is called when one
    clicks on one of the image buttons'''
    global out1
    # call function
    plot = Plotter(choice)
    out.set(plot.plottype())
    window.update_idletasks()

def select_file():
    '''This function is called by the open_button'''
    # We should think about which kind of files we accept
    filetypes = (
        ('CSV files', '*.csv'),
        ('HDF5 files', '*.hdf5'),
        ('Fits files', '*.fits'),
        ('All files', '*.*'))

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename)

# Create tkinter window
window = tk.Tk()
window.config(bg='pale turquoise')

# Name of the "App"
window.title('Name')

# Variables for the output, currently just a string
out = tk.StringVar()
out.set('')

# Header in the window
header = tk.Label(window,
                  text='*******    We need a cool name for this!    ********',
                  font=('Helvetica',16, 'bold'), bg='light blue', fg='blue4',
                  width = 40, height=2)
# Text in the window
description = tk.Label(window,
                       text='Load data and choose a plot-type!',
                       font=('Helvetica', 16), bg='light blue', fg='black')

# Call preview images
preview_img_1 = tk.PhotoImage(file='pictures/one.png')
preview_img_2 = tk.PhotoImage(file='pictures/two.png')
preview_img_3 = tk.PhotoImage(file='pictures/three.png')

# Show output, this is now a string, need to look how we can have an image
result = tk.Label(window, textvariable=out, font=('Helvetica',16, 'bold'), bg='light blue', fg='blue4', width = 40, height=2)

# Buttons to choose which plot you want
plotbutton1 = tk.Button(window, image=preview_img_1, text='Enter', bg='red', fg='orange', command=lambda: pressbutton('1'))
plotbutton2 = tk.Button(window, image=preview_img_2, text='Enter', bg='red', fg='orange', command=lambda: pressbutton('2'))
plotbutton3 = tk.Button(window, image=preview_img_3, text='Enter', bg='red', fg='orange', command=lambda: pressbutton('3'))

# Open file button
open_button = ttk.Button(window, text='Open a File', command=select_file)

# position everything on the window
# row,column
#  __ __ __
# |00 01 02|
# |10 11 12|
# |20 21 22|

header.grid(row=0, column=0, columnspan=3, rowspan=2)
description.grid(row=2,column=0, columnspan=3, rowspan=1)
open_button.grid(row=0, column=0)
plotbutton1.grid(row=3, column=0)
plotbutton2.grid(row=3,column=1)
plotbutton3.grid(row=3, column=2)
result.grid(row=5, column=0, columnspan=3)

# create window
window.mainloop()