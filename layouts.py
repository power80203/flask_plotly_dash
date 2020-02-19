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
                dbc.DropdownMenuItem("location", href="#"),
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
                dbc.DropdownMenuItem("location", href="#"),
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






head = html.Div([dbc.NavbarSimple(
    children=[
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("", header=True),
                dbc.DropdownMenuItem("language", href="#"),
                dbc.DropdownMenuItem("location", href="#"),
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
)])



body = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Heading"),
                        html.P(
                            """\
                            Donec id elit non mi porta gravida at eget metus.
                            Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum
                            nibh, ut fermentum massa justo sit amet risus. Etiam porta sem
                            malesuada magna mollis euismod. Donec sed odio dui. Donec id elit non
                            mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus
                            commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit
                            amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed
                            odio dui."""
                        ),
                        dbc.Button("View details", color="secondary"),
                    ],
                    md=4,
                ),
                dbc.Col(
                    [
                        html.H2("Graph"),
                        dcc.Graph(
                            figure={"data": [{"x": [1, 2, 3], "y": [1, 4, 9]}]}
                        ),
                    ]
                ),
            ]
        )
    ],
    className="mt-4",
)

layout2 = html.Div([head, body])
