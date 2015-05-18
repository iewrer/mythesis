import plotly.plotly as py
from plotly.graph_objs import *

axe = ['v_2 = 4.4','v_2 = 4.4.2','v_2 = 4.3','v_2 = 4.3.1','v_2 = 4.2','v_2 = 4.2.1','v_2 = 4.2.2']

trace1 = Bar(
    x=axe,
    y=[1272,1272,1200,1200,1196,1196,1196],
    name='v_2文件数'
)
trace2 = Bar(
    x=axe,
    y=[1088,1097,1126,1126,1115,1115,1115],
    name='diff(v_2,v_1)文件数'
)
trace3 = Bar(
	x = axe,
	y = [1200,1200,1200,1200,1200,1200,1200],
	name = 'v_1文件数'
)
data = Data([trace1, trace2, trace3])
layout = Layout(
    barmode='group'
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='stacked-bar')
py.image.save_as(fig, '../figures/differ2.png')