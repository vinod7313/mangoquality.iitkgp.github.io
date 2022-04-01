import dash                              # pip install dash
from dash import html
from dash import dcc
from dash.dependencies import Output, Input

from dash_extensions import Lottie       # pip install dash-extensions
import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components
import plotly.express as px              # pip install plotly
import pandas as pd                      # pip install pandas
from datetime import date
import calendar
import plotly.graph_objects as go



# Lottie by Emil - https://github.com/thedirtyfew/dash-extensions
url_QUALITY = "https://assets1.lottiefiles.com/packages/lf20_I0lJNs.json"
url_TEMPERATURE = "https://assets4.lottiefiles.com/packages/lf20_qkvneqme.json"
url_VOC = "https://assets3.lottiefiles.com/private_files/lf30_xdwr7zpk.json"
url_CO2 = "https://assets3.lottiefiles.com/packages/lf20_vwoauv0p.json"

options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))

# components
indicator1 = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = 1.2,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "CRISP VALUE", 'font': {'size': 24}},
    delta = {'reference': 2.4, 'increasing': {'color': "RebeccaPurple"}},
    gauge = {
        'axis': {'range': [None, 3], 'tickwidth': 1, 'tickcolor': "darkblue"},
        'bar': {'color': "darkblue"},
        'bgcolor': "white",
        'borderwidth': 2,
        'bordercolor': "gray",
        'steps': [
            {'range': [0, 1], 'color': 'green'},
            {'range': [1, 2], 'color': 'yellow'},
            {'range': [2, 3], 'color': 'red'}],
            'threshold' : {'line': {'color': "black", 'width': 4}, 'thickness': 0.75, 'value': 1.2}}))

indicator2 = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = 12.5,
    mode = "gauge+number",
    title = {'text': "TEMPERATURE in *C"},
    gauge = {'axis': {'range': [None, 30]},
             'steps' : [
                 {'range': [0, 10], 'color': "blue"},
                 {'range': [10, 20], 'color': "yellow"},
                 {'range': [20, 30], 'color': "red"}],
             'threshold' : {'line': {'color': "black", 'width': 4}, 'thickness': 0.75, 'value': 12.5}}))

indicator3 = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = 240,
    mode = "gauge+number",
    title = {'text': "VOC in PPM"},
    gauge = {'axis': {'range': [None, 600]},
             'steps' : [
                 {'range': [0, 200], 'color': "blue"},
                 {'range': [200, 400], 'color': "yellow"},
                 {'range': [400, 600], 'color': "red"}],
             'threshold' : {'line': {'color': "black", 'width': 4}, 'thickness': 0.75, 'value': 240}}))

indicator4 = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = 1200,
    mode = "gauge+number",
    title = {'text': "CO2 in PPM"},
    gauge = {'axis': {'range': [None, 2100]},
             'steps' : [
                 {'range': [0, 700], 'color': "blue"},
                 {'range': [700, 1400], 'color': "yellow"},
                 {'range': [1400, 2100], 'color': "red"}],
             'threshold' : {'line': {'color': "black", 'width': 4}, 'thickness': 0.75, 'value': 1200}}))



# Bootstrap themes by Ann: https://hellodash.pythonanywhere.com/theme_explorer
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])

app.layout = dbc.Container([dbc.NavbarSimple(
    children=[

        dbc.DropdownMenu(
            children=[

                dbc.DropdownMenuItem("NODE1", href="#"),
                dbc.DropdownMenuItem("NODE2", href="#"),
                dbc.DropdownMenuItem("NODE3", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="NODE",
        ),
    ],
    brand="MANGO QUALITY",
    brand_href="#",
    color="primary",
    dark=True,
),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(Lottie(options=options, width="30%", height="30%", url=url_QUALITY)),
                dbc.CardBody([
                    html.H6('CRISP VALUE'),
                    html.H2(id='content-CRISP VALUE', children="1.2")
                ], style={'textAlign':'center'})
            ]),
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(Lottie(options=options, width="30%", height="30%", url=url_TEMPERATURE)),
                dbc.CardBody([
                    html.H6('TEMPERATURE'),
                    html.H2(id='content-TEMPERATURE', children="12.5")
                ], style={'textAlign':'center'})
            ]),
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(Lottie(options=options, width="30%", height="30%", url=url_VOC)),
                dbc.CardBody([
                    html.H6('VOC in PPM'),
                    html.H2(id='content-msg-in', children="240")
                ], style={'textAlign':'center'})
            ]),
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(Lottie(options=options, width="30%", height="30%", url=url_CO2)),
                dbc.CardBody([
                    html.H6('CO2 in PPM'),
                    html.H2(id='content-CO2', children="1200")
                ], style={'textAlign': 'center'})
            ]),
        ], width=3),

    ],className='mb-1'),
    dbc.Row([
        dbc.Col([dcc.Graph(figure=indicator1)], width=3,),
        dbc.Col([dcc.Graph(figure=indicator2)], width=3,),
        dbc.Col([dcc.Graph(figure=indicator3)], width=3,),
        dbc.Col([dcc.Graph(figure=indicator4)], width=3,),
    ],className='mb-1',),
], fluid=True)

if __name__=='__main__':
    app.run_server(debug=False, port=8002)