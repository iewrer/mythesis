import plotly.plotly as py
from plotly.graph_objs import *

axe = ['v2 = 4.4','v2 = 4.4.2','v2 = 4.3','v2 = 4.3.1','v2 = 4.2','v2 = 4.2.1','v2 = 4.2.2']

trace1 = Bar(
    x=axe,
    y=[1272,1272,1200,1200,1196,1196,1196],
    name='v2文件数'
)
trace2 = Bar(
    x=axe,
    y=[1088,1097,1126,1126,1115,1115,1115],
    name='diff(v2,v1)文件数'
)
trace3 = Bar(
	x = axe,
	y = [1200,1200,1200,1200,1200,1200,1200],
	name = 'v1文件数'
)
data = Data([trace1, trace2, trace3])
layout = Layout(
    barmode='group'
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='grouped-bar')
py.image.save_as(fig, '../figures/differ2.png')