from dash import html,dcc
from dash_echarts import DashECharts


from dash import html, dcc
from dash_echarts import DashECharts

welcome_layout = html.Div(
    children=[html.Div([
            html.H1("抖音用户行为分析", style={
                'fontSize': '48px',
                'marginBottom': '30px',
                'color': 'white'
            }),
            html.P("抖音用户作者浏览行为分析与聚类分析", style={
                'fontSize': '20px',
                'marginBottom': '40px',
                'color': 'white'
            }),
            html.Button('马上开始', 
                        id='start-button', 
                        n_clicks=0, 
                        className='start-button')
        ], className="welcome-header"),]
    , className='welcome-container')

main_layout = html.Div([
    html.Div([
        html.H1("抖音用户浏览数据挖掘", className='header'),
        html.Div([
            # 左侧导航栏
            html.Div([
                html.H3("分析选项", style={'marginBottom': '20px', 'color': '#333'}),
                
                # 类别选择下拉框
                dcc.Dropdown(
                    id='category-dropdown',
                    options=[
                        {'label': '用户数据分析', 'value': 'user'},
                        {'label': '作者数据分析', 'value': 'author'},
                        {'label': '作品数据分析', 'value': 'artwork'},
                        {'label': '聚类效果分析', 'value': 'clst'}
                    ],
                    value='user',
                    clearable=False,
                    style={'marginBottom': '10px'}
                ),
                
                # 可视化选项下拉框
                dcc.Dropdown(
                    id='visualization-dropdown',
                    options=[],
                    value=None,
                    clearable=False,
                    style={'marginBottom': '10px'}
                ),
                
                # 当前选中项目显示
                html.Div(id='current-selection', style={
                    'margin': '10px 0',
                    'padding': '10px',
                    'border': '1px solid #ddd',
                    'borderRadius': '5px',
                    'backgroundColor': '#f9f9f9'
                }),
                
                # 操作按钮
                html.Div([
                    html.Button('选定分析目标', 
                              id='confirm-btn', 
                              n_clicks=0, 
                              className='button',
                              style={'marginBottom': '10px'}),
                    html.Button('返回首页', 
                              id='btn-home', 
                              n_clicks=0, 
                              className='button')
                ], style={'marginTop': '10px'})
            ], className='sidebar'),
            
            # 右侧主显示区
            html.Div([
                html.Div(id='graph-title', className='graph-title'),
                DashECharts(
                    id='visualization',
                    style={'height': '100%'}
                )
            ], className='content')
        ], style={'display': 'flex', 'gap': '20px'})
    ], style={'padding': '0px'})
])
# welcome_layout = html.Div(
#     children=[html.Div([
#             html.H1("抖音用户行为分析", style={
#                 'fontSize': '48px',
#                 'marginBottom': '30px',
#                 'color': 'white'
#             }),
#             html.P("探索用户作者浏览行为分析与聚类分析", style={
#                 'fontSize': '20px',
#                 'marginBottom': '40px',
#                 'color': 'white'
#             }),
#             html.Button('马上开始', 
#                         id='start-button', 
#                         n_clicks=0, 
#                         className='start-button')
#         ], className="welcome-header"),]
#     , className='welcome-container')


# page1_layout = html.Div([
#     html.Div([
#         html.H1("用户行为分析", className= 'header'),
#         html.Div([
#             # 左侧导航栏
#             html.Div([
#                 html.Div(id='output', ),
#                 html.H3("分析选项", style={'marginBottom': '20px', 'color': '#333'}),
#                 html.Div([
#                     html.H4("用户数据分析", style={'marginTop': '20px', 'color': '#555'}),
#                     dcc.Dropdown(
#                         id='dropdown1',
#                         options=[
#                         {'label': '不同浏览量用户占比', 'value': '1'},
#                         {'label': '用户累计浏览量占比', 'value': '2'},
#                         {'label': '不同点赞量用户占比', 'value': '3'},
#                         {'label': '用户累计点赞量分布', 'value': '4'},
#                         {'label': '完整观看情况', 'value': '5'},
#                         {'label': '观看平均时长', 'value': '6'},
#                         {'label': '去过不同数量城市的用户占比', 'value': '7'}
#                         ],
#                         value='1' # 默认选中的值
#                     ),


#                     html.H4("作者数据分析", style={'marginTop': '30px', 'color': '#555'}),
#                     dcc.Dropdown(
#                         id='dropdown2',
#                         options=[
#                         {'label': '不同浏览量作者占比', 'value': '1'},
#                         {'label': '作者累计浏览量占比', 'value': '2'},
#                         {'label': '不同点赞量作者占比', 'value': '3'},
#                         {'label': '作者累计点赞量分布', 'value': '4'},
#                         {'label': '作者去过不同城市数量分布', 'value': '5'}
#                         ],
#                         value='1' # 默认选中的值
#                     ),
#                     html.H4("作品数据分析", style={'marginTop': '30px', 'color': '#555'}),
#                     dcc.Dropdown(
#                         id='dropdown3',
#                         options=[
#                         {'label': '单日作品发布量', 'value': '1'},
#                         {'label': '作品浏览量占比', 'value': '2'},
#                         {'label': '作品点赞数分布', 'value': '3'}
#                         ],
#                         value='1' # 默认选中的值
#                     ),
#                     html.H4("聚类效果分析", style={'marginTop': '30px', 'color': '#555'}),
#                     dcc.Dropdown(
#                         id='dropdown4',
#                         options=[
#                         {'label': '用户聚类效果', 'value': '1'},
#                         {'label': '作者聚类效果', 'value': '2'}
#                         ],
#                         value='1' # 默认选中的值
#                     ),
#                     html.Button('切换上一页面', 
#                                id='btn-prev', 
#                                n_clicks=0, 
#                                className = 'button'),
                     
#             ], className = 'sidebar'),
#             # 右侧主显示区
#             html.Div([
#                 html.Div(id='graph-title', className = 'graph-title'),
#                 DashECharts(
#                         id='visualization',
#                         style={'height': '100%'}),
#                 #dcc.Graph(id='main-graph', style={'height': '100%'})
#             ], className = 'content')
#         ], style={'display': 'flex', 'gap': '20px'})
#             ], style={'padding': '0px'})
#         ])
#     ])

                    # html.Button('不同浏览量用户占比', 
                    #            id='btn-user-view', 
                    #            n_clicks=0, 
                    #            className = 'button-selected'),
                    # html.Button('用户累计浏览量占比', 
                    #            id='btn-user-accumulate', 
                    #            n_clicks=0, 
                    #            className = 'button'),
                    # html.Button('不同点赞量用户占比', 
                    #            id='btn-user-like', 
                    #            n_clicks=0, 
                    #            className = 'button'),
                    # html.Button('用户累计点赞量分布', 
                    #            id='btn-user-likes', 
                    #            n_clicks=0, 
                    #            className = 'button'),
                    # html.Button('完整观看情况', 
                    #            id='btn-user-fullview', 
                    #            n_clicks=0, 
                    #            className = 'button'),
                    # html.Button('观看平均时长', 
                    #            id='btn-user-avgtime', 
                    #            n_clicks=0, 
                    #            className = 'button'),
                   
                    # html.Button('去过不同数量城市的用户占比', 
                    #            id='btn-user-cities', 
                    #            n_clicks=0, 
                    #            className = 'button'),
# page2_layout = html.Div([
#     html.Div([
#         html.H1("作者行为分析", className= 'header'),
#         html.Div([
#             # 左侧导航栏
#             html.Div([
#                 html.H3("分析选项", style={'marginBottom': '20px', 'color': '#333'}),
#                 html.Div([
#                     # html.H4("作者数据分析", style={'marginTop': '20px', 'color': '#555'}),
#                     html.Button('不同浏览量作者占比', 
#                                id='btn-author-view', 
#                                n_clicks=0, 
#                                className = 'button-selected'),
#                     html.Button('作者累计浏览量占比', 
#                                id='btn-author-accumulate', 
#                                n_clicks=0, 
#                                className = 'button'),
                    
#                     # html.H4("用户数据分析", style={'marginTop': '30px', 'color': '#555'}),
#                     html.Button('不同点赞量作者占比', 
#                                id='btn-author-like', 
#                                n_clicks=0, 
#                                className = 'button'),
#                     html.Button('作者累计点赞量分布', 
#                                id='btn-author-likes', 
#                                n_clicks=0, 
#                                className = 'button'),

#                     html.Button('作者去过不同城市数量分布', 
#                                id='btn-author-cities', 
#                                n_clicks=0, 
#                                className = 'button'),
#                     html.Button('切换下一页面', 
#                                id='btn-next', 
#                                n_clicks=0, 
#                                className = 'button'),
#                     html.Button('切换上一页面', 
#                                id='btn-prev', 
#                                n_clicks=0, 
#                                className = 'button'),
                     
                     
#             ], className = 'sidebar'),
#             # 右侧主显示区
#             html.Div([
#                 html.Div(id='graph-title', className = 'graph-title'),
#                 DashECharts(
#                     id='visualization',
#                     style={'height': '100%'}),
#                 #dcc.Graph(id='main-graph', style={'height': '100%'})
#             ], className = 'content')

        
#         ], style={'display': 'flex', 'gap': '20px'})
#             ], style={'padding': '0px'})
#         ])
#     ])

# page3_layout = html.Div([
#     html.Div([
#         html.H1("作者行为分析", className= 'header'),
#         html.Div([
#             # 左侧导航栏
#             html.Div([
#                 html.H3("分析选项", style={'marginBottom': '20px', 'color': '#333'}),
#                 html.Div([
#                     # html.H4("作者数据分析", style={'marginTop': '20px', 'color': '#555'}),
#                     html.Button('单日作品发布量', 
#                                id='btn-artwork-single', 
#                                n_clicks=0, 
#                                className = 'button-selected'),
#                     html.Button('作品浏览量占比', 
#                                id='btn-artwork-view', 
#                                n_clicks=0, 
#                                className = 'button'),
                    
#                     # html.H4("用户数据分析", style={'marginTop': '30px', 'color': '#555'}),
#                     html.Button('点赞数分布', 
#                                id='btn-artwork-like', 
#                                n_clicks=0, 
#                                className = 'button'),
#                     html.Button('切换下一页面', 
#                                id='btn-next', 
#                                n_clicks=0, 
#                                className = 'button'),
#                     html.Button('切换上一页面', 
#                                id='btn-prev', 
#                                n_clicks=0, 
#                                className = 'button'),
                     
                     
#             ], className = 'sidebar'),
#             # 右侧主显示区
#             html.Div([
#                 html.Div(id='graph-title', className = 'graph-title'),
#                 DashECharts(
#                     id='visualization',
#                     style={'height': '100%'}),
#                 #dcc.Graph(id='main-graph', style={'height': '100%'})
#             ], className = 'content')
#         ], style={'display': 'flex', 'gap': '20px'})
#             ], style={'padding': '0px'})
#         ])
#     ])

# page4_layout = html.Div([
#     html.Div([
#         html.H1("作者-用户聚类分析", className= 'header'),
#         html.Div([
#             # 左侧导航栏
#             html.Div([
#                 html.H3("聚类分析", style={'marginBottom': '20px', 'color': '#333'}),
#                 html.Div([
#                     # html.H4("作者数据分析", style={'marginTop': '20px', 'color': '#555'}),
#                     html.Button('用户聚类效果', 
#                                id='btn-user-cluster', 
#                                n_clicks=0, 
#                                className = 'button-selected'),
#                     html.Button('作者聚类效果', 
#                                id='btn-author-cluster', 
#                                n_clicks=0, 
#                                className = 'button'),
#                     html.Button('切换上一页面', 
#                                id='btn-prev', 
#                                n_clicks=0, 
#                                className = 'button'),
                     
                     
#             ], className = 'sidebar'),
#             # 右侧主显示区
#             html.Div([
#                 html.Div(id='graph-title', className = 'graph-title'),
#                 DashECharts(
#                     id='visualization',
#                     style={'height': '100%'}),
#                 #dcc.Graph(id='main-graph', style={'height': '100%'})
#             ], className = 'content')
#         ], style={'display': 'flex', 'gap': '20px'})
#             ], style={'padding': '0px'})
#         ])
#     ])
