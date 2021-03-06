import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from layouts import layout1, layout2, layout_basic
import callbacks

app.layout = html.Div([
    dcc.Location(id='url', refresh=True),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/app1':
         return layout1
    elif pathname == '/apps/app2':
         return layout2
    else:
        return layout_basic



if __name__ == '__main__':
    app.run_server(debug=True)