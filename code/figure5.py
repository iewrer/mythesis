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
    y=[881,892,930,925,916,924,928],
    name='impact(diff(v2,v4),v2)成功分析数'
)
trace3 = Bar(
    x = axe,
    y = [1278,1274,1202,1202,1198,1198,1198],
    name = 'v4文件数'
)
trace4 = Bar(
    x = axe,
    y = [1172,1178,1124,1123,1117,1116,1116],
    name = 'diff(v2,v4)文件数'
)
data = Data([trace1, trace2, trace3, trace4])
plot_url = py.plot(data, filename='bar-line')
py.image.save_as({'data': data}, '../figures/impact2.png')