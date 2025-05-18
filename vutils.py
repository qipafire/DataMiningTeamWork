from pyecharts.charts import Pie,Line,Funnel
from pyecharts import options as opts
import joblib



def draw(k, sse, sc):
    """
    绘制聚类折线图
    :param k: 聚类的个数
    :param sse: 误差平方和
    :param sc: 轮廓系数
    """
    chart = (
        Line(init_opts=opts.InitOpts(
            theme='light',
            width='350px',
            height='350px'
        ))
        .add_xaxis(k)
        .add_yaxis('sse', sse, yaxis_index=0, label_opts=opts.LabelOpts(is_show=False))
        .add_yaxis('sc', sc, yaxis_index=1, label_opts=opts.LabelOpts(is_show=False))
        .extend_axis(yaxis=opts.AxisOpts())
        .set_global_opts(
            title_opts=opts.TitleOpts(title='聚类效果'),
            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=True),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
        )
    )
    return chart

def line_chart(t, data):
    chart = (
        Line(init_opts = opts.InitOpts(theme='light', width='500px', height='300px'))
        .add_xaxis([i[0] for i in data])
        .add_yaxis(
            '',
            [i[1] for i in data],
            is_symbol_show=False,
            areastyle_opts=opts.AreaStyleOpts(opacity=1, color="cyan")
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title=t),
            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=True),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
        )
    )
    return chart
def pie_chart(t, data_pair):
    # 新建一个饼图
    chart = (
        Pie(init_opts=opts.InitOpts(theme='light', width='350px', height='300px'))
        .add('', data_pair ,radius=["30%", "45%"], # 半径范围，内径和外径
            label_opts=opts.LabelOpts(formatter="{b}: {d}%") # 标签设置，{d}表示显示百分比
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title=t
             ),
            legend_opts=opts.LegendOpts(pos_left="0%",pos_top="55",orient='vertical')
        )
    )
    return chart
def fl_chart(t, data):
    chart = (
        Funnel(init_opts=opts.InitOpts(theme='light', width='150px', height='200px'))
        .add('', data, min_=4000, max_=60000, 
             label_opts=opts.LabelOpts(formatter='{d}%', position='right'))
        .set_global_opts(
            title_opts=opts.TitleOpts(title=t),
        legend_opts=opts.LegendOpts(pos_left="0%",pos_top="55",orient='vertical')
        )
    )
    return chart



# if __name__ == '__main__':
#     # 示例：生成并保存用户聚类图表
#     user_score = joblib.load(f'data/用户聚类指标.score')
#     user_chart = draw([str(x) for x in range(2,10)], user_score['sse'], user_score['sc'])
#     save_chart_to_file(user_chart, "output/user_cluster.html")
    
#     # 示例：生成并保存作者聚类图表
#     author_score = joblib.load(f'data/作者聚类指标.score')
#     author_chart = draw([str(x) for x in range(2,10)], author_score['sse'], author_score['sc'])
#     save_chart_to_file(author_chart, "output/author_cluster.html")
