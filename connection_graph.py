import json
import pandas as pd
import random
import copy
import numpy as np
import matplotlib.pyplot as plt

# 对每个圆设置随机颜色
def randomcolor_func():
  color_char = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
  color_code = ""
  for i in range(6):
    color_code += color_char[random.randint(0,14)] # randint包括前后节点0和14
  return "#"+color_code

## 生成每个圆心的坐标
# 根据圆的参数方程进行
r = 10
a, b = (0, 0)
theta = np.arange(0, 2*np.pi, 0.36)
X = a + r * np.cos(theta)
Y = b + r * np.sin(theta)

## 构造连接图（节点和边）
def create_json(data, weights):
  # 自定义节点
  address_dict = {"nodes":[], "edges":[]}
  node_dict = {
      "color": "",
      "label": "",
      "attributes": {},
      "y": None,
      "x": None,
      "id": "",
      "size": None
    }
  edge_dict = {
      "sourceID": "",
      "attributes": {},
      "targetID": "",
      "size": None
    }
    
  # 存储每个节点的数据
  for ii in range(len(data)):
    # for jj in range(len(data.iloc[ii])):
    jj = 0
    # node，"attributes"属性可自行设置
    node_dict[r"color"] = randomcolor_func()
    node_dict[r"label"] = data.iloc[ii, jj]
    x, y = X[ii], Y[ii]
    node_dict[r"y"] = y
    node_dict[r"x"] = x
    node_dict[r"id"] = data.iloc[ii, jj]
    node_dict[r"size"] = int(weights.loc[data.iloc[ii, jj]])
    
    tmp_node = copy.deepcopy(node_dict)
    address_dict[r"nodes"].append(tmp_node)

  # 存储每个边的数据
  for ii in range(len(data)):
    for jj in range(1, len(data.iloc[ii])):    
      # edge
      edge_dict[r"sourceID"] = data.iloc[ii, 0]
      edge_dict[r"targetID"] = data.iloc[ii, jj]
      edge_dict[r"size"] = 10
        
      tmp_edge = copy.deepcopy(edge_dict)
      address_dict["edges"].append(tmp_edge)
    
  return address_dict

if __name__ == '__main__': 
  # read data
    data = pd.read_excel(r'connection_data.xlsx', 0)

    # weights = pd.DataFrame({"比例":[30, 22, 12, 10, 8, 8, 4, 4, 4, 4, 4, 4, 2, 2, 2, 2, 2]}, 
    #           index = ['美国','中国','德国','希腊','西班牙','英国','意大利','丹麦','奥地利','韩国','新加坡','瑞典', '瑞士', '波兰', '澳大利亚', '爱尔兰', '法国']) #建立索引权值列表
    weights = pd.DataFrame({"比例":[90, 66, 36, 30, 24, 24, 12, 12, 12, 12, 12, 12, 6, 6, 6, 6, 6]}, 
              index = ['美国','中国','德国','希腊','西班牙','英国','意大利','丹麦','奥地利','韩国','新加坡','瑞典', '瑞士', '波兰', '澳大利亚', '爱尔兰', '法国']) #建立索引权值列表

    address_dict = create_json(data, weights)
   
    with open("connection_data.json", "w", encoding='utf-8') as f:
    # json.dump(dict_, f) # 写为一行
        json.dump(address_dict, f, indent=2, ensure_ascii=False) # 写为多行
