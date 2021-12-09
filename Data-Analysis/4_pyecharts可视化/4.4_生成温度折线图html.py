import csv
from pyecharts import options as opts
from pyecharts.charts import Line
import pandas as pd


def opencsv():

    csv_data = pd.read_csv("site_tem_1.csv")
    print(csv_data)
    yymmdd = csv_data['日期'].values.tolist()
    high_tem = csv_data['最高气温'].values.tolist()
    low_tem = csv_data['最低气温'].values.tolist()

    return yymmdd,high_tem,low_tem

def linechart(list):

    yymmdd = list[0]
    high_tem = list[1]
    low_tem = list[2]


    (
    Line(init_opts=opts.InitOpts(width="3200px", height="1600px"))
    .add_xaxis(xaxis_data=yymmdd)
    .add_yaxis(
        series_name="最高气温",
        y_axis=high_tem,
        markpoint_opts=opts.MarkPointOpts(
            data=[
                opts.MarkPointItem(type_="max", name="最大值"),
                opts.MarkPointItem(type_="min", name="最小值"),
            ]
        ),
        markline_opts=opts.MarkLineOpts(
            data=[opts.MarkLineItem(type_="average", name="平均值")]
        ),
    )
    .add_yaxis(
        series_name="最低气温",
        y_axis=low_tem,
        markpoint_opts=opts.MarkPointOpts(
            data=[opts.MarkPointItem(value=-2, name="周最低", x=1, y=-1.5)]
        ),
        markline_opts=opts.MarkLineOpts(
            data=[
                opts.MarkLineItem(type_="average", name="平均值"),
                opts.MarkLineItem(symbol="none", x="90%", y="max"),
                opts.MarkLineItem(symbol="circle", type_="max", name="最高点"),
            ]
        ),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="最近10年气温变化", subtitle="汉中市"),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        toolbox_opts=opts.ToolboxOpts(is_show=True),
        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
    )
    .render("temperature_change_line_chart.html")
)

if __name__ == '__main__':

    list = opencsv()
    # print(list)

    linechart(list)


