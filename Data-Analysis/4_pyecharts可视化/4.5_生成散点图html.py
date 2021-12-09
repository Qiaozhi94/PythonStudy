#!/usr/bin/env python3
# _*_coding:utf-8_*_
"""
@ File    :4.5_生成散点图html.py
@ Time    :2020/6/22 9:02 下午
@ Author  :GerorgeL.
@ Email   :George.q.li@outlook.com
@ IDE     :PyCharm
"""

from pyecharts import options as opts
from pyecharts.charts import Scatter
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot
import numpy as np
import pandas as pd
pd.set_option('display.max_columns',1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth',1000)

file_path = "/Users/georgel./Files/Study-Notes/Python/数据分析/3_Pandas/IMDB-Movie-Data.csv"

data = pd.read_csv(file_path)
print(data.info())

data_list = []

for i in range(1,len(data["Rating"])):
    data_list.append([i,data["Rating"][i]])


data_list.sort(key=lambda x: x[0])
x_data = [d[0] for d in data_list]
y_data = [d[1] for d in data_list]


def scatter():
    scatter = (
        Scatter(init_opts=opts.InitOpts(width="800px", height="500px"))
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(
            series_name="",
            y_axis=y_data,
            symbol_size=5,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_series_opts()
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(
                type_="value", splitline_opts=opts.SplitLineOpts(is_show=True)
            ),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
            tooltip_opts=opts.TooltipOpts(is_show=False),
        )
        .render("IMDB-Movie-Data.html")
    )
    return scatter


make_snapshot(snapshot, scatter(), "电影评分散点图.png")






