# Color schemes
# http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter

import tkinter as tk
from tkinter import ttk
from plotter import Plotter
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

class Ourcoolapp():
    def __init__(self, window):
        self.window = window
        #frame = tk.Frame(self.window, bg='pale turquoise')
        # Variables for the output, currently just a string
        self.out = tk.StringVar()
        self.out.set('')
        # Header in the window
        header = tk.Label(self.window,
                          text='*******    We need a cool name for this!    ********',
                          font=('Helvetica',16, 'bold'), bg='light blue', fg='blue4',
                          width = 40, height=2)
        # Text in the window
        description = tk.Label(self.window,
                               text='Load data and choose a plot-type!',
                               font=('Helvetica', 16), bg='light blue', fg='black')

        # Call preview images
        preview_img_1 = tk.PhotoImage(file='pictures/one.png')
        preview_img_2 = tk.PhotoImage(file='pictures/two.png')
        preview_img_3 = tk.PhotoImage(file='pictures/three.png')

        # Show output, this is now a string, need to look how we can have an image
        result = tk.Label(self.window, textvariable=self.out, font=('Helvetica',16, 'bold'), bg='light blue', fg='blue4', width = 40, height=2)

        # Buttons to choose which plot you want
        plotbutton1 = tk.Button(self.window, image=preview_img_1, text='Enter', bg='red', fg='orange', command=lambda: self.pressbutton('1'))
        plotbutton2 = tk.Button(self.window, image=preview_img_2, text='Enter', bg='red', fg='orange', command=lambda: self.pressbutton('2'))
        plotbutton3 = tk.Button(self.window, image=preview_img_3, text='Enter', bg='red', fg='orange', command=lambda: self.pressbutton('3'))

        # Open file button
        #open_button = ttk.Button(frame, text='Open a File', command=self.select_file())

        # position everything on the window
        # row,column
        #  __ __ __
        # |00 01 02|
        # |10 11 12|
        # |20 21 22|

        header.grid(row=0, column=0, columnspan=3, rowspan=2)
        description.grid(row=2,column=0, columnspan=3, rowspan=1)
        #open_button.grid(row=0, column=0)
        plotbutton1.grid(row=3, column=0)
        plotbutton2.grid(row=3,column=1)
        plotbutton3.grid(row=3, column=2)
        result.grid(row=5, column=0, columnspan=3)

    def pressbutton(self, choice):
        '''This function is called when one
        clicks on one of the image buttons'''
        # call function
        plot = Plotter(choice)
        self.out.set(plot.plottype())
        self.window.update_idletasks()

    def select_file(self):
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
win = tk.Tk(bg='pale turquoise')

# Name of the "App"
win.title('Our cool App')

app=Ourcoolapp(win)
# "Run" window
win.mainloop()