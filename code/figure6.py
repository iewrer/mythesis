import plotly.plotly as py
from plotly.graph_objs import *

axe = ['v2 = 4.4','v2 = 4.4.2','v2 = 4.3','v2 = 4.3.1','v2 = 4.2','v2 = 4.2.1','v2 = 4.2.2']

# trace2 = Scatter(
#     x = axe,
#     y=[2,3,3,3,4,3,4],
#     name = '影响域重叠数'
# )

trace1 = Scatter(
    x=axe,
    y=[2,3,3,3,4,3,4],
    name='冲突文件数'
)
# trace2 = Scatter(
#     x = axe,
#     y=[59,64,69,66,64,63,65],
#     name = '影响域重叠数'
# )
data = Data([trace1])
layout = Layout(
    xaxis=XAxis(
        title = 'Eclipse JDT Core版本'
    ),
    yaxis=YAxis(
        title = '文件数量'
    ),
    showlegend=True
    # barnorm='percent'
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='grouped-bar')
py.image.save_as({'data': data}, '../figures/conflict1.png')