import plotly.plotly as py
from plotly.graph_objs import *

axe = ['v_2 = 4.4','v_2 = 4.4.2','v_2 = 4.3','v_2 = 4.3.1','v_2 = 4.2','v_2 = 4.2.1','v_2 = 4.2.2']

trace1 = Bar(
    x=axe,
    y=[91,94,110,110,99,99,99],
    name='预处理数'
)
trace2 = Bar(
    x=axe,
    y=[1088,1097,1126,1126,1115,1115,1115],
    name='diff(v_2,v_1)文件数'
)
trace3 = Bar(
	x = axe,
	y = [1172,1178,1124,1123,1117,1116,1116],
	name = 'diff(v_2,v_4)文件数'
)
data = Data([trace1, trace2, trace3])
layout = Layout(
    barmode='group'
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='grouped-bar')
py.image.save_as(fig, '../figures/differ1.png')