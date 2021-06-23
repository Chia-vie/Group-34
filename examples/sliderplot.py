import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import plotly.graph_objs as go


# read in the data
file = "example_data/run_GGM_1M_CRlER_norm_st.csv"
df = pd.read_csv(file, index_col="Unnamed: 0", float_precision='round_trip')
columns = df.columns
snaptimes = np.array([c.lstrip('R_') for c in columns if 'R_' in c])
print(snaptimes)


# set up the plot
ylim = (0.5, np.max(df['radius'].values))
figure_height, figure_width = 700, 950
title = 'Time evo planet population'

layout = go.Layout(height=figure_height,
                    width=figure_width,
                    title=title,
                    xaxis=go.layout.XAxis(range=[np.min(df['period'].values), np.max(df['period'].values)]),
                    yaxis=go.layout.YAxis(range=[ylim[0], ylim[1]])
                    ) #title=str(y_axis.expression)
                    


# Create figure
fig = go.Figure(layout=layout)

# Add traces, one for each slider step
for step in snaptimes: #np.arange(1, 10, 1):
    fig.add_trace(go.Scatter( 
            #visible=False,
            #name="𝜈 = " + str(step),
            x=df['period'].values,
            y=df['R_'+step].values,
            marker=dict(
                size=15,
                cmax=np.max(np.log10(df['M_'+step].values)),
                cmin=np.min(np.log10(df['M_'+step].values)),
                color=np.log10(df['M_'+step].values),
                colorbar=dict(
                    title="Colorbar"
                ),
                colorscale="Turbo"
            ),
            mode="markers",
        ))

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
            #    color="rgba(152, 0, 0, .8)",##00CED1
                size=5,
                line=dict(
                    color='Black',
                    width=0.5
                )
            ),
)


fig.show()
