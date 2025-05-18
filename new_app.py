from dash import Dash, html, dcc, Input, Output, State, callback
import dash
import json
from pages import welcome_layout, main_layout
from vutils import pie_chart, line_chart, fl_chart, draw
from dataAdapter import data_prepare

# 加载数据
data = data_prepare()

# 从graph.txt中读取图表配置
chart_configs = [
    {'label': '不同浏览量用户占比', 'chart_func': pie_chart, 'data': data['user_data']['view_user'], 'category': 'user'},
    {'label': '用户累计浏览量占比', 'chart_func': line_chart, 'data': data['user_data']['cumulate_view'], 'category': 'user'},
    {'label': '不同点赞量用户占比', 'chart_func': pie_chart, 'data': data['user_data']['like_user'], 'category': 'user'},
    {'label': '用户累计点赞量分布', 'chart_func': line_chart, 'data': data['user_data']['like'], 'category': 'user'},
    {'label': '完整观看情况', 'chart_func': pie_chart, 'data': data['user_data']['full_view'], 'category': 'user'},
    {'label': '观看平均时长', 'chart_func': fl_chart, 'data': data['user_data']['avgtime_user'], 'category': 'user'},
    {'label': '去过不同数量城市的用户占比', 'chart_func': pie_chart, 'data': data['user_data']['cities'], 'category': 'user'},
    
    {'label': '不同浏览量作者占比', 'chart_func': pie_chart, 'data': data['author_data']['view_author'], 'category': 'author'},
    {'label': '作者累计浏览量占比', 'chart_func': line_chart, 'data': data['author_data']['cumulate_view'], 'category': 'author'},
    {'label': '不同点赞量作者占比', 'chart_func': pie_chart, 'data': data['author_data']['like_author'], 'category': 'author'},
    {'label': '作者累计点赞量分布', 'chart_func': line_chart, 'data': data['author_data']['like'], 'category': 'author'},
    {'label': '作者去过不同城市数量分布', 'chart_func': pie_chart, 'data': data['author_data']['cities'], 'category': 'author'},
    
    {'label': '单日作品发布量', 'chart_func': line_chart, 'data': data['artwork_data']['single_day'], 'category': 'artwork'},
    {'label': '作品浏览量占比', 'chart_func': pie_chart, 'data': data['artwork_data']['view_work'], 'category': 'artwork'},
    {'label': '作品点赞数分布', 'chart_func': pie_chart, 'data': data['artwork_data']['like_work'], 'category': 'artwork'},
    
    {'label': '用户聚类效果', 'chart_func': draw, 'data': data['clst_data']['user'], 'category': 'clst'},
    {'label': '作者聚类效果', 'chart_func': draw, 'data': data['clst_data']['author'], 'category': 'clst'}
]

# 初始化Dash应用
app = Dash(__name__, suppress_callback_exceptions=True)
server = app.server

# 应用布局
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# 页面路由
@callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/main':
        return main_layout
    return welcome_layout

# 导航到主页面
@callback(
    Output('url', 'pathname', allow_duplicate=True),
    Input('start-button', 'n_clicks'),
    prevent_initial_call=True
)
def navigate_to_main(n_clicks):
    if n_clicks:
        return '/main'
    return dash.no_update

# 导航回首页
@callback(
    Output('url', 'pathname', allow_duplicate=True),
    Input('btn-home', 'n_clicks'),
    prevent_initial_call=True
)
def navigate_to_home(n_clicks):
    if n_clicks:
        return '/'
    return dash.no_update

# 更新可视化选项下拉框
@callback(
    Output('visualization-dropdown', 'options'),
    Input('category-dropdown', 'value')
)
def update_visualization_options(selected_category):
    if not selected_category:
        return []
    
    options = []
    for config in chart_configs:
        if config['category'] == selected_category:
            options.append({
                'label': config['label'],
                'value': chart_configs.index(config)
            })
    
    return options

# 更新当前选中项目显示
@callback(
    Output('current-selection', 'children'),
    Input('category-dropdown', 'value'),
    Input('visualization-dropdown', 'value'),
    prevent_initial_call=True
)
def update_current_selection(selected_category, selected_chart_idx):
    if not selected_chart_idx:
        return "请选择分析项目"
    
    selected_config = chart_configs[selected_chart_idx]
    return html.Div([
        html.H4("当前选中分析项目", style={'marginBottom': '10px'}),
        html.P(f"类别: {selected_category}"),
        html.P(f"图表: {selected_config['label']}")
    ])

# 初始化默认选择   
@callback(
    Output('visualization-dropdown', 'value'),
    Input('category-dropdown', 'value')
)
def set_default_visualization(selected_category):
    if not selected_category:
        return None
    
    # 找到该类别下的第一个图表配置
    for config in chart_configs:
        if config['category'] == selected_category:
            return chart_configs.index(config)
    return None

# 更新图表
@callback(
    Output('visualization', 'option'),
    Output('graph-title', 'children'),
    Input('confirm-btn', 'n_clicks'),
    State('current-selection', 'children'),
    prevent_initial_call=False
)
def update_chart(n_clicks, current_selection):
    if not current_selection or isinstance(current_selection, str):
        # 初始状态，显示默认图表
        default_category = 'user'
        for config in chart_configs:
            if config['category'] == default_category:
                selected_config = config
                break
    else:
        # 从显示框内容中解析出当前选中的图表label
        chart_label = current_selection['props']['children'][2]['props']['children'].split(': ')[1]
        for config in chart_configs:
            if config['label'] == chart_label:
                selected_config = config
                break
        else:
            return {}, ""
    
    chart_func = selected_config['chart_func']
    chart_data = selected_config['data']
    
    # 根据图表类型调用不同的绘图函数
    if selected_config['chart_func'] == draw:
        # 聚类图表特殊处理
        k = [str(x) for x in range(2, 10)]
        sse = chart_data['sse']
        sc = chart_data['sc']
        chart = chart_func(k, sse, sc)
    else:
        # 其他图表
        chart = chart_func(selected_config['label'], chart_data)
    
    # 获取图表配置
    chart_option = json.loads(chart.dump_options())
    
    # 更新标题
    title = html.H2(selected_config['label'])
    
    return chart_option, title
if __name__ == '__main__':
    app.run(debug=True) 