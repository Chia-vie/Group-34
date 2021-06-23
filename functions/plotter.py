import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
        

class Plotter():
""" add documentation """
    def __init__(self, choice, df):
        self.choice = choice
        self.df = df

    def plottype(self):
        if self.choice == '1':
            msg = 'You chose plot type 1'
            self.plot_type1()
        elif self.choice == '2':
            msg = 'You chose plot type 2'
        elif self.choice == '3':
            msg = 'You chose plot type 3'
        return msg


    def plot_type1(self, ylim=None,
                         title = None):
        """ currently everyting is set up for my data set only. 
        and in a bad way. maybe pass column names instead. 
        dictionary with params
        """ 
        
        if ylim == None:
            ylim=(0.5, np.max(self.df['radius'].values))
        if title == None:
            title = 'title'


        # plot layout
        figure_height, figure_width = 700, 950
        layout = go.Layout(height=figure_height,
                            width=figure_width,
                            title=title,
                            xaxis=go.layout.XAxis(range=[np.min(self.df['period'].values), np.max(self.df['period'].values)]),
                            yaxis=go.layout.YAxis(range=[ylim[0], ylim[1]])
                            ) #title=str(y_axis.expression)
        
        df = pd.read_csv("./example_data/run_GGM_CRlER_norm_st.csv", index_col="Unnamed: 0", float_precision='round_trip')
        columns = df.columns
        snaptimes = np.array([c.lstrip('R_') for c in columns if 'R_' in c])

        # Create figure
        fig = go.Figure(layout=layout)

        # Add traces, one for each slider step
        for step in snaptimes: #np.arange(1, 10, 1):
            fig.add_trace(
                go.Scatter( 
                    visible=False,
                    name="𝜈 = " + str(step),
                    x=df['period'].values,
                    y=df['R_'+step].values),
                )

        # Make 10th trace visible
        fig.data[0].visible = True


        # Create and add slider
        steps = []
        for i in range(len(fig.data)):
            step = dict(
                method="update",
                args=[{"visible": [False] * len(fig.data)},
                    {"title": "Slider switched to step: " + snaptimes[i] + ' Myr'}],  # layout attribute
            )
            step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
            steps.append(step)

        sliders = [dict(
            active=0,
            currentvalue={"prefix": "Age [Myr]: "},
            pad={"t": 50},
            steps=steps
        )]

        fig.update_layout(
            sliders=sliders
        )

        fig.update_xaxes(title_text='Period [days]', type="log", range=[np.log10(np.min(df['period'].values)), np.log10(np.max(df['period'].values))])
        fig.update_yaxes(title_text='Radius [R_Earth]', type="log", range=[np.log10(ylim[0]), np.log10(ylim[1])])
        fig.update_traces(mode='markers', opacity=0.75, 
                    marker=dict(
                        color="rgba(152, 0, 0, .8)",##00CED1
                        size=5,
                        line=dict(
                            color='Black',
                            width=0.5
                        )
                    ),
        )

        fig.show()
