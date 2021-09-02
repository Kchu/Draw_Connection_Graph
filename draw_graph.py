import pyecharts.options as opts
from pyecharts.charts import Graph
import json
 
with open(r".\connection_data.json", encoding='utf-8') as f: #设置以utf-8解码模式读取文件，encoding参数必须设置，否则默认以gbk模式读取文件，当文件中包含中文时，会报错
  data = json.load(f)
#print(data)
 
nodes = [
  {
    "x": node["x"],
    "y": node["y"],
    "id": node["id"],
    "name": node["label"],
    "symbolSize": node["size"],
    "itemStyle": {"normal": {"color": node["color"]}},
  }
  for node in data["nodes"]
]
 
edges = [{"source": edge["sourceID"], "target": edge["targetID"]} for edge in data["edges"]]

(
  Graph(init_opts=opts.InitOpts(width="1600px", height="800px"))
  .add(
    series_name="",
    nodes=nodes,
    links=edges,
    layout="none",
    is_roam=True,
    is_focusnode=True,
    label_opts=opts.LabelOpts(is_show=True, font_size=20),
    # linestyle_opts=opts.LineStyleOpts(width=0.5, curve=0.3, opacity=0.7),
    linestyle_opts=opts.LineStyleOpts(width=2, curve=0.3, opacity=0.7),
  )
  .set_global_opts(title_opts=opts.TitleOpts())
  .render("Connection-Graph.html")
)