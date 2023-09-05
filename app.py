#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 14:40:17 2017

@author: claudiahertzog
"""

from dash import Dash, dcc, html, Input, Output, callback
import dash_auth
import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd
import matplotlib as mpl
import gunicorn                     #whilst your local machine's webserver doesn't need this, Heroku's linux webserver (i.e. dyno) does. I.e. This is your HTTP server

# Keep this out of source code repository - save in a file or a database
VALID_USERNAME_PASSWORD_PAIRS = {
    'kstAdmin': 'fishF3rm!ng'
}

# Instantiate dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.SANDSTONE])
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)


# Reference the underlying flask app (Used by gunicorn webserver in Heroku production deployment)
server = app.server 

# Define Dash layout
def create_dash_layout(app):

    # Set browser tab title
    app.title = "Your app title" 
    
    # Header
    header = html.Div([html.Br(), dcc.Markdown(""" # Hi. I'm your Dash app."""), html.Br()])
    
    # Body 
    body = html.Div([
        html.H3('Kent SeaTech Sales Report',
                style={'display': 'inline',
                       'float': 'left',
                       'margin-left': '7px',
                       'margin-top': '20px',
                       'margin-bottom': '0'
                       }
                ),
        html.Img(src="http://kentseatech.com/wp-content/uploads/2016/08/Kenttesch-logo-retina.png",
                style={
                    'margin-top': '20px',
                    'height': '100px',
                    'float': 'right'
                },
        ),
    ],style={'width': '100%'})

    # Footer
    footer = html.Div([
        html.Br(), 
        html.Br(), 
        dcc.Markdown(""" ### Built with ![Image](heart.png) in Python using [Dash](https://plotly.com/dash/)""")])
    
    # Assemble dash layout 
    app.layout = html.Div([header, body, footer])

    return app

# Construct the dash layout
create_dash_layout(app)

# Run flask app
if __name__ == "__main__": app.run_server(debug=True)
