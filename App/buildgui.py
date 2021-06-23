# Color schemes
# http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from .plotter import Plotter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from .dataframe import dummydata

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
        self.logmsg = tk.StringVar()
        self.logmsg.set('Please select a dataframe and click on the type of plot you would you like to make')
        # Read in preview images
        self.preview_img_1 = tk.PhotoImage(file='App/pictures/one.png')
        self.preview_img_2 = tk.PhotoImage(file='App/pictures/two.png')
        self.preview_img_3 = tk.PhotoImage(file='App/pictures/three.png')
        self.buttonsandlabels()

    def pressbutton(self,choice):
        '''This function is called when one
        clicks on one of the image buttons'''
        # check if dataframe was read in
        if hasattr(self, 'df'):
            # call plotter function
            plot = Plotter(choice, self.df)
            # set out variable accordingly
            self.logmsg.set(plot.plottype())
        else:
            self.logmsg.set('Please select a dataframe before plotting')
        # display the updated out string in window
        self.window.update_idletasks()

    def decrease(self):
        x, y = self.line.get_data()
        self.line.set_ydata(y - 0.2 * x)
        self.canvas.draw()

    def increase(self):
        x, y = self.line.get_data()
        self.line.set_ydata(y + 0.2 * x)
        self.canvas.draw()

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

    # just for testing
    def select_dummy_file(self):
        self.df = dummydata()
        self.logmsg.set('You chose to load the dummy data')

    def makefig(self):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        self.line, = self.ax.plot(range(10))

    def buttonsandlabels(self):

        # Header in the window
        self.header = tk.Label(self.window,
                          text='*******    We need a cool name for this!    ********',
                          font=('Helvetica',16, 'bold'), bg='light blue', fg='blue4',
                          width = 40, height=2)

        # Show log messages
        self.description = tk.Label(self.window,
                               textvariable=self.logmsg,
                               font=('Helvetica', 16), bg='light blue', fg='black')

        # Buttons to choose which plot you want
        self.plotbutton1 = tk.Button(self.window, image=self.preview_img_1,
                                     text='Enter', bg='red', fg='orange',
                                     command=lambda: self.pressbutton('1'),
                                     width = 300, height=400)
        self.plotbutton2 = tk.Button(self.window, image=self.preview_img_2,
                                     text='Enter', bg='red', fg='orange',
                                     command=lambda: self.pressbutton('2'),
                                     width = 300, height=400)
        self.plotbutton3 = tk.Button(self.window, image=self.preview_img_3,
                                     text='Enter', bg='red', fg='orange',
                                     command=lambda: self.pressbutton('3'),
                                     width = 300, height=400)

        self.open_button = ttk.Button(self.window, text='Open a file', command=self.select_file)
        self.dummy_button = ttk.Button(self.window, text='Open dummy data', command=self.select_dummy_file)

        self.makefig()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.window)
        self.canvas.draw()
        self.widgets = self.canvas.get_tk_widget()
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
        self.dummy_button.grid(row=1,column=0)
        self.plotbutton1.grid(row=3, column=0)
        self.plotbutton2.grid(row=3,column=1)
        self.plotbutton3.grid(row=3, column=2)
        self.widgets.grid(row=7,column=1, columnspan=1)