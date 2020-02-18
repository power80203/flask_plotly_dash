import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([
    html.Ul([
            html.Li([
                    dcc.Link('First', href='/first')
                    ], className='active'),
            html.Li([
                    dcc.Link('Second', href='/second')
                    ]),
            html.Li([
            dcc.Link('Third', href='/third')
                    ]),
            ], className='nav navbar-nav')
    ,
    html.h1('back to Home'),
    dcc.Link('back to Home', href='/'),
    html.H3('App 2'),
    dcc.Dropdown(
        id='app-2-dropdown',
        options=[
            {'label': 'App 2 - {}'.format(i), 'value': i} for i in [
                'NYC', 'MTL', 'LA'
            ]
        ]
    ),
    html.Div(id='app-2-display-value'),
    dcc.Link('Go to App 1', href='/apps/app1')
],
className='navbar navbar-default navbar-static-top')


@app.callback(
    Output('app-1-display-value', 'children'),
    [Input('app-1-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)