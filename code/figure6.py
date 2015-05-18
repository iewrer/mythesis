import plotly.plotly as py
from plotly.graph_objs import *

axe = ['v_2 = 4.4','v_2 = 4.4.2','v_2 = 4.3','v_2 = 4.3.1','v_2 = 4.2','v_2 = 4.2.1','v_2 = 4.2.2']

trace2 = Scatter(
    x = axe,
    y=[2,3,3,3,4,3,4],
    name = '预处理后影响域重叠数'
)

trace1 = Bar(
    x=axe,
    y=[2,3,3,3,4,3,4],
    name='冲突文件数'
)
trace3 = Scatter(
    x = axe,
    y=[59,64,69,66,64,63,65],
    name = '预处理前影响域重叠数'
)
data = Data([trace1, trace2, trace3])
plot_url = py.plot(data, filename='bar-line')
py.image.save_as({'data': data}, '../figures/conflict1.png')