# Color schemes
# http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from .plotter import Plotter

class Ourcoolapp():
    def __init__(self, window):
        self.window = window
        # background color
        self.window.config(bg='pale turquoise')
        # title
        self.window.title('Group-34: Our fabulous App')
        # Variables for the output, currently just a string
        self.out = tk.StringVar()
        self.out.set('')
        # Read in preview images
        self.preview_img_1 = tk.PhotoImage(file='pictures/one.png')
        self.preview_img_2 = tk.PhotoImage(file='pictures/two.png')
        self.preview_img_3 = tk.PhotoImage(file='pictures/three.png')
        self.buttonsandlabels()

    def pressbutton(self,choice):
        '''This function is called when one
        clicks on one of the image buttons'''
        # call plotter function
        plot = Plotter(choice)
        # set out variable accordingly
        self.out.set(plot.plottype())
        self.window.update_idletasks()

    def select_file(self):
        '''This function is called by the open_button'''
        # Which kind of files are accepted?
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

    def buttonsandlabels(self):

        # Header in the window
        self.header = tk.Label(self.window,
                          text='*******    We need a cool name for this!    ********',
                          font=('Helvetica',16, 'bold'), bg='light blue', fg='blue4',
                          width = 40, height=2)
        # Text in the window
        self.description = tk.Label(self.window,
                               text='Load data and choose a plot-type!',
                               font=('Helvetica', 16), bg='light blue', fg='black')

        # Show output, this is now a string, need to look how we can have an (interactive) image
        self.result = tk.Label(self.window,
                               textvariable = self.out,
                               font=('Helvetica',16, 'bold'), bg='light blue', fg='blue4',
                               width = 40, height=2)

        # Buttons to choose which plot you want
        self.plotbutton1 = tk.Button(self.window, image=self.preview_img_1,
                                     text='Enter', bg='red', fg='orange',
                                     command=lambda: self.pressbutton('1'))
        self.plotbutton2 = tk.Button(self.window, image=self.preview_img_2,
                                     text='Enter', bg='red', fg='orange',
                                     command=lambda: self.pressbutton('2'))
        self.plotbutton3 = tk.Button(self.window, image=self.preview_img_3,
                                     text='Enter', bg='red', fg='orange',
                                     command=lambda: self.pressbutton('3'))

        # Open file button
        self.open_button = ttk.Button(self.window, text='Open a File', command=self.select_file)

        # Call function to place everything on the window
        self.place()

    def place(self):
        '''
        # place everything on the window
        # row,column
        #  __ __ __
        # |00 01 02|
        # |10 11 12|
        # |20 21 22|
        '''
        self.header.grid(row=0, column=0, columnspan=3, rowspan=2)
        self.description.grid(row=2,column=0, columnspan=3, rowspan=1)
        self.open_button.grid(row=0, column=0)
        self.plotbutton1.grid(row=3, column=0)
        self.plotbutton2.grid(row=3,column=1)
        self.plotbutton3.grid(row=3, column=2)
        self.result.grid(row=5, column=0, columnspan=3)