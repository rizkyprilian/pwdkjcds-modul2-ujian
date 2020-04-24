import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

import seaborn as sns
import plotly.graph_objects as go

import dash_table

from dash.dependencies import Input, Output, State

tips = sns.load_dataset('tips')

def generate_table(dataframe, page_size=10):
    return dash_table.DataTable(
        id='dataTable',
        columns=[ {'name': i, 'id': i} for i in dataframe.columns],
        data=dataframe.to_dict('records'),
        page_action='native',
        page_current=0,
        page_size=page_size
    )

external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    html.Div(className='row mt-2 mb-4', children=[

        html.Div(children=[

            dcc.Tabs(
                value='PieChart',
                content_style = {
                    'fontFamily': 'Helvetica, Arial, sans-serif',
                    'border': '1px solid #d6d6d6',
                    'borderTop': 'none',
                    'padding': '44px'
                },
                children=[

                    dcc.Tab(value='', label='tab4', children=[
                        
                        html.Div(className='row', children=[

                            html.Div(className='col-2', children=[
                                html.Label('Smoker'),

                                dcc.Dropdown(
                                    value='',
                                    id='filter-smoker',
                                    options=[
                                        {'label': 'No', 'value': 'No'},
                                        {'label': 'Yes', 'value': 'Yes'},
                                        {'label': 'None', 'value': ''}
                                    ]
                                )
                            ]),

                            html.Div(className='col-2', children=[
                                html.Label('Sex'),

                                dcc.Dropdown(
                                    value='',
                                    id='filter-sex',
                                    options=[
                                        {'label': 'Male', 'value': 'Male'},
                                        {'label': 'Female', 'value': 'Female'},
                                        {'label': 'None', 'value': ''}
                                    ]
                                )
                            ]),

                            html.Div(className='col-2', children=[
                                html.Label('Day'),

                                dcc.Dropdown(
                                    value='',
                                    id='filter-day',
                                    options=[
                                        {'label': 'Sun', 'value': 'Sun'},
                                        {'label': 'Mon', 'value': 'Mon'},
                                        {'label': 'Tue', 'value': 'Tue'},
                                        {'label': 'Wed', 'value': 'Wed'},
                                        {'label': 'Thu', 'value': 'Thu'},
                                        {'label': 'Fri', 'value': 'Fri'},
                                        {'label': 'Sat', 'value': 'Sat'},
                                        {'label': 'None', 'value': ''}
                                    ]
                                )
                            ]),

                            html.Div(className='col-2', children=[
                                html.Label('Time'),

                                dcc.Dropdown(
                                    value='',
                                    id='filter-time',
                                    placeholder='None',
                                    options=[
                                        {'label': 'Dinner', 'value': 'Dinner'},
                                        {'label': 'Lunch', 'value': 'Lunch'},
                                        {'label': 'None', 'value': ''}
                                    ]
                                )
                            ]),

                            html.Div(className='col-2', children=[
                                html.Label('Max Rows'),
                                dcc.Input(value='10', type='number', id='maxrows', step=1, min=1)
                            ]),

                            html.Div(id='btn-search', className='col-1', children=[html.Button(children='Search')]),
                            html.Div(id='btn-reset', className='col-1', children=[html.Button(children='Reset')])
                        ]),

                        html.Div(className='row mt-4', children=[
                            html.Div(id='data-table', className='col-12', children=[generate_table(
                                dataframe=tips[(tips['smoker'] == 'Yes') & (tips['sex'] == 'Female')]
                                )])
                        ])

                        
                    ]),

                    dcc.Tab(
                        value='BarPlot',
                        label='BarPlot',
                        children=[

                            html.Div(className='row', children=[
                                
                                # category 1
                                html.Div(className='col-2', children=[
                                    html.Label('Category 1'),
                                    dcc.Dropdown(
                                        value='sex',
                                        id='graph-cat-1',
                                        placeholder='None',
                                        options=[
                                            {'label': 'Smoker', 'value': 'smoker'},
                                            {'label': 'Sex', 'value': 'sex'},
                                            {'label': 'Day', 'value': 'day'},
                                            {'label': 'Time', 'value': 'time'},
                                            {'label': 'Size', 'value': 'size'}
                                        ]
                                    )
                                ]),

                                # type 1
                                html.Div(className='col-2', children=[
                                    html.Label('Type 1'),
                                    dcc.Dropdown(
                                        value='bar',
                                        id='graph-type-1',
                                        placeholder='None',
                                        options=[
                                            {'label': 'Bar', 'value': 'bar'},
                                            {'label': 'Violin', 'value': 'violin'}
                                        ]
                                    )
                                ]),

                                # category 2
                                html.Div(className='col-2', children=[
                                    html.Label('Category 2'),
                                    dcc.Dropdown(
                                        value='sex',
                                        id='graph-cat-2',
                                        placeholder='None',
                                        options=[
                                            {'label': 'Smoker', 'value': 'smoker'},
                                            {'label': 'Sex', 'value': 'sex'},
                                            {'label': 'Day', 'value': 'day'},
                                            {'label': 'Time', 'value': 'time'},
                                            {'label': 'Size', 'value': 'size'}
                                        ]
                                    )
                                ]),

                                # type 2
                                html.Div(className='col-2', children=[
                                    html.Label('Type 2'),
                                    dcc.Dropdown(
                                        value='bar',
                                        id='graph-type-2',
                                        placeholder='None',
                                        options=[
                                            {'label': 'Bar', 'value': 'bar'},
                                            {'label': 'Violin', 'value': 'violin'}
                                        ]
                                    )
                                ]),

                                # numerical
                                html.Div(className='col-2', children=[
                                    html.Label('Numerical'),
                                    dcc.Dropdown(
                                        value='tip',
                                        id='graph-numerical',
                                        placeholder='None',
                                        options=[
                                            {'label': 'Total Bill', 'value': 'total_bill'},
                                            {'label': 'Tip', 'value': 'tip'}
                                        ]
                                    )
                                ]),

                                #search button
                                html.Div(id='btn-graph-apply', className='col-2', children=[html.Button(children='Apply')])

                            ]),

                            html.Div(className='row', children=[
                                dcc.Graph(
                                    id='example-graph',
                                    figure={
                                        'data': [
                                            {'x': tips['smoker'], 'y': tips['tip'], 'type': 'bar', 'name': 'smoker'},
                                            {'x': tips['sex'], 'y': tips['tip'], 'type': 'violin', 'name': 'sex'}
                                        ],
                                        'layout': {
                                            'title': 'Tips Dash Data Visualization'
                                        }
                                    },
                                    className='col-12'
                                )
                            ])
                        ]
                    ),

                    dcc.Tab(
                        value='ScatterPlot',
                        label='ScatterPlot',
                        children=[

                            html.Div(className='row', children=[

                                html.Div(className='col-2', children=[
                                    html.Label('Category'),
                                    dcc.Dropdown(
                                            value='sex',
                                            id='scatter-filter-cat',
                                            placeholder='None',
                                            options=[
                                                {'label': 'Smoker', 'value': 'smoker'},
                                                {'label': 'Sex', 'value': 'sex'},
                                                {'label': 'Day', 'value': 'day'},
                                                {'label': 'Time', 'value': 'time'},
                                                {'label': 'Size', 'value': 'size'}
                                            ]
                                    )
                                ])

                            ]),

                            html.Div(className='row', children=[
                                dcc.Graph(
                                    id = 'graph-scatter',
                                    figure = {'data': [
                                        go.Scatter(
                                            x = tips[tips['day'] == i]['tip'],
                                            y = tips[tips['day'] == i]['total_bill'],
                                            mode='markers',
                                            name = 'Day {}'.format(i)
                                            ) for i in tips['day'].unique()
                                        ],
                                        'layout': go.Layout(
                                            xaxis= {'title': 'Tip'},
                                            yaxis={'title': ' Total Bill'},
                                            title= 'Tips Dash Scatter Visualization',
                                            hovermode='closest'
                                        )
                                    },
                                    className = 'col-12'
                                )
                            ])

                        ]
                    ),

                    dcc.Tab(
                        value='PieChart',
                        label='PieChart',
                        children=[

                            html.Div(className='col-12', children=[

                                html.Div(className='row', children=[
                                    html.Div(className='col-2', children=[
                                        html.Label('Category'),
                                        dcc.Dropdown(
                                            value='sex',
                                            id='pie-filter-cat',
                                            placeholder='None',
                                            options=[
                                                {'label': 'Smoker', 'value': 'smoker'},
                                                {'label': 'Sex', 'value': 'sex'},
                                                {'label': 'Day', 'value': 'day'},
                                                {'label': 'Time', 'value': 'time'},
                                                {'label': 'Size', 'value': 'size'}
                                            ]
                                        )
                                    ]),

                                    html.Div(className='col-2', children=[
                                        html.Label('Numerical'),
                                        dcc.Dropdown(
                                            value='total_bill',
                                            id='pie-filter-numerical',
                                            placeholder='None',
                                            options=[
                                                {'label': 'Total Bill', 'value': 'total_bill'},
                                                {'label': 'Tip', 'value': 'tip'},
                                            ]
                                        )
                                    ])
                                
                                ]),


                                html.Div(className='row', children=[
                                    dcc.Graph(
                                        id = 'pie-chart',
                                        figure = {
                                            'data':[
                                                    go.Pie(labels = [i for i in tips['sex'].unique()], 
                                                            values= [tips[tips['sex'] == i]['tip'].mean() for i in tips['sex'].unique()])
                                                    ],
                                            'layout': go.Layout(title = 'Tip mean divided by Sex')
                                        },
                                        className = 'col-12'
                                    )
                                ])

                            ])
                        ]
                    )
            ]),

        ],
        className='col-12',
        )

    ]) #.row

], className='container-fluid')



@app.callback(
    Output('example-graph', 'figure'),
    [Input('btn-graph-apply','n_clicks')],
    [
        State('graph-type-1', 'value'),
        State('graph-cat-1', 'value'),
        State('graph-type-2', 'value'),
        State('graph-cat-2', 'value'),
        State('graph-numerical', 'value')
    ]
)
def update_graph(n_clicks, graph_type_1, graph_cat_1, graph_type_2, graph_cat_2, graph_numerical):
    return {
                'data': [
                    {'x': tips[graph_cat_1], 'y': tips[graph_numerical], 'type': graph_type_1, 'name': graph_cat_1},
                    {'x': tips[graph_cat_2], 'y': tips[graph_numerical], 'type': graph_type_2, 'name': graph_cat_2}
                ],
                'layout': {
                    'title': 'Tips Dash Data Visualization'
                }
            }




@app.callback(
    Output('graph-scatter', 'figure'),
    [
        Input('scatter-filter-cat', 'value')
    ]
)
def filter_scatter(scatter_filter_cat):
    return {'data': [
                go.Scatter(
                    x = tips[tips[scatter_filter_cat] == i]['tip'],
                    y = tips[tips[scatter_filter_cat] == i]['total_bill'],
                    mode='markers',
                    name = '{} {}'.format(scatter_filter_cat.capitalize(),i)
                    ) for i in tips[scatter_filter_cat].unique()
                ],
                'layout': go.Layout(
                    xaxis= {'title': 'Tip'},
                    yaxis={'title': ' Total Bill'},
                    title= 'Tips Dash Scatter Visualization Separated by {}'.format(scatter_filter_cat.capitalize()),
                    hovermode='closest'
                )
            }


@app.callback(
    Output('pie-chart', 'figure'),
    [
        Input('pie-filter-cat', 'value'),
        Input('pie-filter-numerical', 'value')
    ]
)
def change_pie(pie_filter_cat, pie_filter_numerical):
    return {
        'data':[
                go.Pie(labels = [i for i in tips[pie_filter_cat].unique()], 
                        values= [tips[tips[pie_filter_cat] == i][pie_filter_numerical].mean() for i in tips[pie_filter_cat].unique()])
                ],
        'layout': go.Layout(title = '{} mean divided by {}'.format(pie_filter_numerical, pie_filter_cat))
    }


@app.callback(
    [
        Output(component_id='filter-smoker', component_property='value'),
        Output(component_id='filter-sex', component_property='value'),
        Output(component_id='filter-day', component_property='value'),
        Output(component_id='filter-time', component_property='value'),
        Output(component_id='maxrows', component_property='value'),
        Output('btn-search','n_clicks')
    ],
    [Input('btn-reset','n_clicks')]
)
def reset_search(n_clicks):
    return '','','','',10,1



@app.callback(
    Output(component_id='data-table', component_property='children'),
    [
        Input(component_id='btn-search', component_property='n_clicks')
    ],
    [
        State(component_id='filter-smoker', component_property='value'),
        State(component_id='filter-sex', component_property='value'),
        State(component_id='filter-day', component_property='value'),
        State(component_id='filter-time', component_property='value'),
        State(component_id='maxrows', component_property='value')
    ]
)
def process_filter(n_clicks, filter_smoker, filter_sex, filter_day, filter_time, maxrows):
    search_prop = {}

    if filter_smoker != '':
        search_prop['smoker'] = filter_smoker
    
    if filter_sex != '':
        search_prop['sex'] = filter_sex
    
    if filter_day != '':
        search_prop['day'] = filter_day

    if filter_time != '':
        search_prop['time'] = filter_time

    if len(list(search_prop.keys())) > 0:
        return [generate_table(tips.loc[(
            tips[list(search_prop)] == pd.Series(search_prop)).all(axis=1)],
            page_size=int(maxrows))
            ]
    else:
        return [generate_table(tips, page_size=int(maxrows))]

if __name__ == '__main__':
    app.run_server(debug=True,port=42217)