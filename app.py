import dash
import dash_bootstrap_components as dbc


# external_stylesheets = ['https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css']

# app = dash.Dash(__name__)
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
# app.scripts.config.serve_locally = False
server = app.server
app.config.suppress_callback_exceptions = True

app.title = 'ReportingService_By_ESA'