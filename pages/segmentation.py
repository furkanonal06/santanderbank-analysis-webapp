from dash import html

layout = html.Div(className="page-content", children=[
    html.Link(rel="stylesheet", href="/assets/segmentation.css"),
    html.Div(className="grid-container segmentation", children=[
        
        # Churn Rate by Segment
        html.Div(className="card churn-rate", children=[html.P("KPI 1")]),

        # Segment Distribution
        html.Div(className="card segment-distribution", children=[html.P("KPI 1")]),

        # Segment Descriptions Container
        html.Div(className="card-group segment-descriptions", children=[
            html.H3("Graph 2", className="group-title"),
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