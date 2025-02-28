from dash import html
import pandas as pd
import numpy as np
from dash import html, dcc, Input, Output, callback, State
import plotly.express as px

df=pd.read_csv("data/processed-data/past-data.csv")


layout = html.Div(className="page-content", children=[
    html.Link(rel="stylesheet", href="/assets/segmentation.css"),
    html.Div(className="grid-container segmentation", children=[
        
        # Churn Rate by Segment
        html.Div(className="card churn-rate", children=[
            html.P("Churn Rate by Segment"),
            html.Div(
                dcc.Graph(id="churn-rate-segment", config={"displayModeBar": False}, style={"width": "100%", "height": "100%"})
                    )]),

        # Segment Distribution
        html.Div(className="card segment-distribution", children=[html.P("Segment Distribution")]),

        # Segment Descriptions Container
        html.Div(className="card-group segment-descriptions", children=[
            html.H3("Segment Descriptions", className="group-title"),
            html.Div(className="cards-container", children=[
                html.Div(className="card", children=[html.P("Graph 4")]),
                html.Div(className="card", children=[html.P("Graph 5")]),
            ])
        ]),

        # Segment Profile Radar Chart Container
        html.Div(className="card segment-radar", children=[html.P("KPI 1")]),


        # Churn Rate by Product Use
        html.Div(className="card churn-rate-product", children=[html.P("KPI 1")]),

    ])
])


# Callback for Churn Rate by Segment
@callback(
    Output("churn-rate-segment", "figure"),
    Input("churn-rate-segment", 'id')
)
def update_activity(_):
    gmm_churn_rate = df.groupby('GMM_Cluster')['Churn_Probability'].mean()
    gmm_churn_rate = gmm_churn_rate.sort_values(ascending=False).reset_index()
    fig = px.bar(gmm_churn_rate, title="Churn Rate by Gender")
    fig.update_layout(yaxis_tickformat=".0%",
                      margin=dict(t=10, b=10, l=10, r=10),
                      xaxis_title=None,
                      yaxis_title=None,
                      title=None,
                      dragmode=False,
                      xaxis=dict(
                          tickfont=dict(
                          size=10,
                          color='rgb(82, 82, 82)',
                          ),
                          tickmode='array',
                          ),
                      yaxis=dict(
                          showgrid=True,
                          zeroline=False,
                          showline=False,
                          showticklabels=True,
                          showticksuffix="none",
                        ),
                      template="plotly_white",
                      hoverlabel=dict(
                          bgcolor="white",  
                          font_size=12,     
                          font_color="black",
                          font_family="Poppins",  
                          bordercolor="white"  
                        ),
                      )
    return fig