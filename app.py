import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import pages.churn_analysis
import pages.data_overview
import pages.segmentation
import pages.insights_recommendations
import pages.prediction_model
import pages.risk_analysis
import pandas as pd
import numpy as np
import joblib
from components.navbar import Navbar
from dash import page_registry

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)  # defining the app

app.title = "X-Bank Dashboard"


# Application layout

app.layout = html.Div(className="dashboard-grid",children=[
    html.Nav(id="navbar-container", className="navbar", children=[
        html.Div(className="navbar-content", children=[
            html.H1(id="navbar-title", className="navbar-title"),
            html.P(id="navbar-subtitle", className="navbar-subtitle")
        ])
    ]),
    html.Aside(className="sidebar",
             children=[
                html.Div(className="top",
                          children=[
                              html.Div(className="sidebar-title",
                                       children=[
                                           html.I(className="fa-solid fa-money-check-dollar"),
                                           html.Span("X-Bank")
                                       ]),
    html.Ul(className="sidebar-list", children=[
        html.Li([
            html.A(
                id="churn-analysis-link",
                className="sidebar-link",
                href="/",
                children=[
                    html.I(className="fa-solid fa-magnifying-glass-chart"),
                    html.Span("Churn Analysis", className="nav-item")
                ]
            ),
        ]),
        html.Li([
            html.A(
                id="segmentation-link",
                className="sidebar-link",
                href="/segmentation",
                children=[
                    html.I(className="fa-solid fa-circle-nodes"),
                    html.Span("Customer Segmentation", className="nav-item")
                ]
            ),
        ]),
        html.Li([
            html.A(
                id="risk-analysis-link",
                className="sidebar-link",
                href="/risk_analysis",
                children=[
                    html.I(className="  "),
                    html.Span("Risk Analysis", className="nav-item")
                ]
            ),
        ]),
        html.Li([
            html.A(
                id="insights-link",
                className="sidebar-link",
                href="/insights_recommendations",
                children=[
                    html.I(className="fa-solid fa-list-check"),
                    html.Span("Insights & Recommendations", className="nav-item")
                ]
            ),
        ]),
        html.Li([
            html.A(
                id="prediction-model-link",
                className="sidebar-link",
                href="/prediction_model",
                children=[
                    html.I(className="fa-solid fa-laptop-code"),
                    html.Span("Churn Prediction Model", className="nav-item")
                ]
            ),
        ]),
        html.Li([
            html.A(
                id="data-overview-link",
                className="sidebar-link",
                href="/data_overview",
                children=[
                    html.I(className="fa-solid fa-database"),
                    html.Span("Data Overview", className="nav-item")
                ]
            ),
        ]),
    ])
                          ]),
        
    
    ]),

    dcc.Location(id="url", refresh=False), # tracks the current page
    html.Div(id="page-content", className="main") # content of each page
])

# defining font-awesome and fonts -------------------------------------------------
app.index_string = """
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        {%css%}
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css">
    </head>
    <body>
        {%app_entry%}
        {%config%}
        {%scripts%}
        {%renderer%}
    </body>
</html>

<style>
@import url("https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap");
@import url('https://fonts.googleapis.com/css2?family=Zen+Dots&display=swap');
</style>
"""

server = app.server

# Callback to update Navbar dynamically
@app.callback(
    [Output("navbar-title", "children"),
     Output("navbar-subtitle", "children")],
    [Input("url", "pathname")]
)
def update_navbar(pathname):
    if pathname == "/":
        return "Churn Analysis", "Analyze customer churn trends and KPIs"
    elif pathname == "/churn_analysis":
        return "Churn Analysis", "Explore customer churn trends"
    elif pathname == "/insights_recommendations":
        return "Insights & Recommendations", "Explore and evaluate actionable business insights & recommendations"
    elif pathname == "/prediction_model":
        return "Prediction Model", "Predict customer churn dynamically."
    elif pathname == "/segmentation":
        return "Customer Segmentation", "Identify customer groups and behaviors."
    elif pathname == "/risk_analysis":
        return "Risk Analysis", "Evaluate customer risks and probabilities."
    elif pathname == "/data_overview":
        return "Data Overview", "Explore the dataset and key statistics."
    else:
        return "Page Not Found", ""

# Callback to update the active link
@app.callback(
    [
    Output("churn-analysis-link", "className"),
    Output("segmentation-link", "className"),
    Output("risk-analysis-link", "className"),
    Output("insights-link", "className"),
    Output("prediction-model-link", "className"),
    Output("data-overview-link", "className"),
    ],
    [
    Input("url", "pathname")
    ]
)
def update_active_tab(pathname):
    # Default class
    default_class = "sidebar-link"
    active_class = "sidebar-link active"

    # Check the current path and assign the active class
    return (
        active_class if pathname == "/" else default_class,
        active_class if pathname == "/segmentation" else default_class,
        active_class if pathname == "/risk_analysis" else default_class,
        active_class if pathname == "/insights_recommendations" else default_class,
        active_class if pathname == "/prediction_model" else default_class,
        active_class if pathname == "/data_overview" else default_class
    )


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/":
        return pages.churn_analysis.layout
    elif pathname == "/segmentation":
        return pages.segmentation.layout
    elif pathname == "/risk_analysis":
        return pages.risk_analysis.layout
    elif pathname == "/insights_recommendations":
        return pages.insights_recommendations.layout
    elif pathname == "/prediction_model":
        return pages.prediction_model.layout
    elif pathname == "/data_overview":
        return pages.data_overview.layout
    else:
        return pages.churn_analysis.layout

if __name__ == "__main__":
    app.run_server(debug=True)