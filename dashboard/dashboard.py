import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

from conf.database import dbconf
from libs.DatabaseConnection import DatabaseConnection

import seaborn as sns
import plotly.graph_objects as go

import dash_table

from dash.dependencies import Input, Output, State


# Initialize Database connection
db_pool = DatabaseConnection(db_config = dbconf) # belum connect database
db_pool.init_pool()

cnx = db_pool.get_connection()
cursor = cnx.cursor()

query = '''SELECT 
    `Claim Number`, 
    `Date Received`,
    `Incident Date`, 
    `Airport Code`,
    `Airport Name`, 
    `Airline Name`, 
    `Claim Type`, 
    `Claim Site`, 
    `Item`,
    `Claim Amount`, 
    `Status`, 
    `Close Amount`, 
    `Disposition`,
    `Day Differences`,
    `Amount Differences`,
    `item_category` 
    FROM tsa_claims_dashboard
    '''

cursor.execute(query)
result = cursor.fetchall()
tsa = pd.DataFrame(result, columns=['Claim Number', 'Date Received',
    'Incident Date', 'Airport Code',
    'Airport Name', 'Airline Name', 'Claim Type', 'Claim Site', 'Item',
    'Claim Amount', 'Status', 'Close Amount', 'Disposition',
    'Day Differences', 'Amount Differences', 'item_category'
])
cursor.close()
cnx.close()

print(tsa)

def generate_table(dataframe, page_size=10):
    return dash_table.DataTable(
        id='dataTable',
        columns=[ {'name': i, 'id': i} for i in dataframe.columns],
        data=dataframe.to_dict('records'),
        page_action='native',
        page_current=0,
        page_size=page_size,
        style_table={'overflowX':'scroll'}
    )

external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    id = 'main-container',
    className = 'container-fluid',
    children=[

        # header
        html.Div(
            className = 'row mt-2 mb-2',
            children = [
                html.Div(
                    className = 'col-12',
                    children = [
                        html.H2('Ujian Modul 2 Dashboard TSA'),
                        html.P('Created by: Rizky Prilian')
                    ]
                )
            ]
        ),


        #tabs container
        html.Div(
            className = 'row',
            children = [
                html.Div(
                    className = 'col-12',
                    children = [

                        #dcc.Tabs

                        dcc.Tabs(
                            value='DataFrameTable',
                            children = [

                                # DataFrameTable
                                dcc.Tab(
                                    value='DataFrameTable',
                                    label='DataFrame Table',
                                    children=[

                                        html.Div(
                                            className='row mt-4',
                                            children=[
                                                html.Div(
                                                    className='col-12',
                                                    children = [html.H4('DataFrame TSA')]
                                                )
                                            ]
                                        ),

                                        # DF Filter
                                        html.Div(
                                            className='row mt-4',
                                            children=[

                                                #claim site
                                                html.Div(
                                                    className='col-2',
                                                    children = [

                                                        html.Label('Claim Site'),

                                                        dcc.Dropdown(
                                                            value='all',
                                                            id='filter-df-claimsite',
                                                            options=[
                                                                {'label': 'Checked Baggage', 'value': 'Checked Baggage'},
                                                                {'label': 'Checkpoint', 'value': 'Checkpoint'},
                                                                {'label': 'Other', 'value': 'Other'},
                                                                {'label': 'Motor Vehicle', 'value': 'Motor Vehicle'},
                                                                {'label': 'Bus Station', 'value': 'Bus Station'},
                                                                {'label': 'All', 'value': 'all'}
                                                            ]
                                                        )

                                                    ]
                                                ),
                                                # / claim site

                                                html.Div(className='col-2', children=[
                                                    html.Label('Max Rows'),
                                                    dcc.Input(value='10', type='number', id='df-maxrows', step=1, min=1)
                                                ]),

                                                html.Div(id='btn-search', className='col-1', children=[
                                                    html.Label(''),
                                                    html.Button(
                                                        className='btn btn-primary',
                                                        children='Search'
                                                    )
                                                    ]),

                                            ]
                                        ),
                                        # / DF Filter

                                        html.Div(className='row mt-4', children=[
                                            html.Div(
                                                id='data-table',
                                                className='col-12 pl-2',
                                                children=[generate_table(tsa, page_size=10)])
                                        ])
                                    ]
                                ),
                                # -- end of DataFrameTable

                                # BarChart
                                dcc.Tab(
                                    value='BarChart',
                                    label='Bar-chart',
                                    children=[

                                        # DF Filter
                                        html.Div(
                                            className='row mt-4',
                                            children=[

                                                #Y1
                                                html.Div(
                                                    className='col-2',
                                                    children = [

                                                        html.Label('Y1'),
                                                        # Claim Amount 	Close Amount 	Day Differences 	Amount Differences
                                                        dcc.Dropdown(
                                                            value='Claim Amount',
                                                            id='filter-bar-y1',
                                                            options=[
                                                                {'label': 'Claim Amount', 'value': 'Claim Amount'},
                                                                {'label': 'Close Amount', 'value': 'Close Amount'},
                                                                {'label': 'Day Differences', 'value': 'Day Differences'},
                                                                {'label': 'Amount Differences', 'value': 'Amount Differences'}
                                                            ]
                                                        )

                                                    ]
                                                ),
                                                # / Y1

                                                #Y2
                                                html.Div(
                                                    className='col-2',
                                                    children = [

                                                        html.Label('Y2'),

                                                        dcc.Dropdown(
                                                            value='Claim Amount',
                                                            id='filter-bar-y2',
                                                            options=[
                                                                {'label': 'Claim Amount', 'value': 'Claim Amount'},
                                                                {'label': 'Close Amount', 'value': 'Close Amount'},
                                                                {'label': 'Day Differences', 'value': 'Day Differences'},
                                                                {'label': 'Amount Differences', 'value': 'Amount Differences'}
                                                            ]
                                                        )

                                                    ]
                                                ),
                                                # / Y2

                                                #X
                                                html.Div(
                                                    className='col-2',
                                                    children = [

                                                        html.Label('X'),

                                                        dcc.Dropdown(
                                                            value='Claim Type',
                                                            id='filter-bar-x',
                                                            options=[
                                                                {'label': 'Claim Type', 'value': 'Claim Type'},
                                                                {'label': 'Claim Site', 'value': 'Claim Site'},
                                                                {'label': 'Disposition', 'value': 'Disposition'}
                                                            ]
                                                        )

                                                    ]
                                                ),
                                                # / X


                                            ]
                                        ),
                                        # / DF 
                                        
                                        html.Div(className='row', children=[
                                            dcc.Graph(
                                                id='bar-plot',
                                                figure={
                                                    'data': [
                                                        {'x': 'Claim Type', 'y': tsa['Claim Amount'], 'type': 'bar', 'color': 'Claim Type'}
                                                    ],
                                                    'layout': {
                                                        'title': 'Bar Chart'
                                                    }
                                                },
                                                className='col-12'
                                            )
                                        ])

                                    ]
                                ),
                                # -- end of BarChart
                            
                                # ScatterChart
                                dcc.Tab(
                                    value='ScatterChart',
                                    label='Scatter-Chart',
                                    children=[

                                        html.Div(className='row', children=[
                                            dcc.Graph(
                                                id = 'graph-scatter',
                                                figure = {'data': [
                                                    go.Scatter(
                                                        x = tsa[tsa['Claim Type'] == i]['Claim Amount'],
                                                        y = tsa[tsa['Claim Type'] == i]['Close Amount'],
                                                        mode='markers',
                                                        name = i,
                                                        ) for i in tsa['Claim Type'].unique()
                                                    ],
                                                    'layout': go.Layout(
                                                        xaxis= {'title': 'Claim Amount'},
                                                        yaxis={'title': 'Close Amount'},
                                                        title= 'Scatter Plot',
                                                        hovermode='closest'
                                                    )
                                                },
                                                className = 'col-12'
                                            )
                                        ])


                                    ]
                                ),
                                # -- end of ScatterChart
                            
                                # PieChart
                                dcc.Tab(
                                    value='PieChart',
                                    label='Pie-Chart',
                                    children=[]
                                )
                                # -- end of PieChart
                            ]
                        )
                    ]
                )
            ]
        )

    ] # main-container.container-fluid
)








@app.callback(
    Output(component_id='data-table', component_property='children'),
    [
        Input(component_id='btn-search', component_property='n_clicks')
    ],
    [
        State(component_id='filter-df-claimsite', component_property='value'),
        State(component_id='df-maxrows', component_property='value')
    ]
)
def process_filter(n_clicks, filter_claimsite, maxrows):

    if filter_claimsite != 'all':
        return generate_table(tsa[tsa['Claim Site'] == str(filter_claimsite)], page_size=int(maxrows))
    else:
        return generate_table(tsa, page_size=int(maxrows))
        


if __name__ == '__main__':
    app.run_server(debug=True,port=42217)