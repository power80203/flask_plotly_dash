from dash.dependencies import Input, Output
import dash_core_components as dcc
import plotly.graph_objs as go
from app import app
from data import PlotData


# get data
_plotData = PlotData()
_plotData.loadData('./data/iris.csv')


trace1 = go.Bar(
    x= [ i for i in _plotData.returnData('sp')],
    y= [ i for i in _plotData.returnData('x1')],
    name='SF Zoo'
)
trace2 = go.Bar(
    x=['giraffes', 'orangutans', 'monkeys'],
    y=[12, 18, 29],
    name='LA Zoo'
)

@app.callback(
    Output('my-id21', 'children'),
    [Input('cx2', "value")])
def display_value(value):
    if value == '999':
        return dcc.Graph(id='bar_plot2',
        figure=go.Figure(data=[trace1, trace2],
        layout=go.Layout(barmode='overlay', title = 'Dash Data Visualization')))
    elif value == '1':
        return dcc.Graph(id='bar_plot2',
        figure=go.Figure(data=[trace1],
        layout=go.Layout(title = 'Dash Data Visualization')))
    elif value == '2':
        return dcc.Graph(id='bar_plot2',
        figure=go.Figure(data=[trace2],
        layout=go.Layout(barmode='stack', title = 'Dash Data Visualization')))


@app.callback(
    Output('app-2-display-value', 'children'),
    [Input('app-2-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)