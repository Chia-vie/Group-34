import matplotlib.pyplot as plt

class Plotter():

    def __init__(self, choice):
        self.choice = choice

    def plottype(self):
        if self.choice == '1':
            msg = 'You chose plot type 1'
        elif self.choice == '2':
            msg = 'You chose plot type 2'
        elif self.choice == '3':
            msg = 'You chose plot type 3'
        return msg
