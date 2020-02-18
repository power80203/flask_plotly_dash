import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.graph_objs as go


layout_basic = html.Div([dbc.NavbarSimple(
    children=[
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("", header=True),
                dbc.DropdownMenuItem("language", href="#"),
                dbc.DropdownMenuItem("normal", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="Setting",
        ),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More", header=True),
                dbc.DropdownMenuItem("Profile", href="#"),
                dbc.DropdownMenuItem("Log out", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="User",
        ),
    ],
    brand="FET DAAS",
    brand_href="#",
    color="warning",
    dark= False,
),html.Br()
,
dbc.ListGroup(
    [
        dbc.ListGroupItem("Active item", color="success"),
        dbc.ListGroupItem("測試報表1", href="apps/app1"),
        dbc.ListGroupItem("測試報表2", href="apps/app2"),
    ],
)
])


# html.Div([
#         dbc.Row(dbc.Col(html.Div("A single column"))),
#         dbc.Row(
#             [
#                 dbc.Col(html.Div("One of three columns")),
#                 dbc.Col(html.Div("One of three columns")),
#                 dbc.Col(html.Div("One of three columns")),
#             ]
#         ),
    
#     # html.H3('這個是首頁'),
#     # dcc.Link('報表1', href='/apps/app1'),
#     # html.Br(),
#     # html.Br(),
#     # dcc.Link('報表2', href='/apps/app2')
    
# ])



trace1 = go.Bar(
    x=['giraffes', 'orangutans', 'monkeys'],
    y=[20, 14, 23],
    name='SF Zoo'
)
trace2 = go.Bar(
    x=['giraffes', 'orangutans', 'monkeys'],
    y=[12, 18, 29],
    name='LA Zoo'
)

layout1 = html.Div([
    html.Div([dbc.NavbarSimple(
    children=[
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("", header=True),
                dbc.DropdownMenuItem("language", href="#"),
                dbc.DropdownMenuItem("normal", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="Setting",
        ),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More", header=True),
                dbc.DropdownMenuItem("Profile", href="#"),
                dbc.DropdownMenuItem("Log out", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="User",
        ),
        dbc.Button("Home", color="link", href="/")
    ],
    brand="FET DAAS",
    brand_href="#",
    color="warning",
    dark= False,
)]),
    html.Div([
            html.H3('App 1'),
        html.H1('Hello Dash'),html.Div([
        html.P('Dash converts Python classes into HTML'),
        html.P('This conversion happens behind the scenes by Dash\'s JavaScript front-end')
                ])
            ], style={'width': '150%', 'display': 'inline-block', 'vertical-align': 'middle'}),
    html.Div([dcc.Graph(id='bar_plot2',
        figure=go.Figure(data=[trace1, trace2],
        layout=go.Layout(barmode='stack', title ='Dash Data Visualization')))]
        ,style={'width': '49%', 'display': 'inline-block', 'vertical-align': 'middle'})])


layout2 = html.Div([
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
])