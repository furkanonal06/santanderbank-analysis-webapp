from dash import html

layout = layout = html.Div([
    html.H1("Insights & Recommendations"),
    html.P("🚧 Work in Progress 🚧"),
]),

html.Div(className="page-content", children=[
    html.Link(rel="stylesheet", href="/assets/insights.css"),
    html.Div(className="grid-container insights-actions", children=[
        
        # Insights
        html.Div(className="card insights", children=[html.P("Insights")]),

        # Recommendations
        html.Div(className="card recommendations", children=[html.P("Recommendations")]),

        # Action Points
        html.Div(className="card actions", children=[html.P("Actions")]),

    ])
])