import plotly.plotly as py
from plotly.graph_objs import *

axe = ['v2 = 4.4','v2 = 4.4.2','v2 = 4.3','v2 = 4.3.1','v2 = 4.2','v2 = 4.2.1','v2 = 4.2.2']

trace1 = Bar(
    x=axe,
    y=[1272,1272,1200,1200,1196,1196,1196],
    name='v2文件数'
)
trace2 = Scatter(
    x=axe,
    y=[881,892,930,930,918,923,924],
    name='impact(diff(v2,v1),v2)成功分析数'
)
trace3 = Bar(
	x = axe,
	y = [1200,1200,1200,1200,1200,1200,1200],
	name = 'v1文件数'
)
trace4 = Bar(
    x=axe,
    y=[1088,1097,1126,1126,1115,1115,1115],
    name='diff(v2,v1)文件数'
)
data = Data([trace1, trace2, trace3, trace4])
plot_url = py.plot(data, filename='bar-line')
py.image.save_as({'data': data}, '../figures/impact1.png')