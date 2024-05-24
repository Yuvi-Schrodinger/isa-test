from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from app import app
from graph_api import GraphAPI
from components import sidebar
from pages import campaigns, adsets


# =========  Layout  =========== #
content = html.Div(id="page-content")

app.layout = html.Div(children=[
                dbc.Row([
                        dbc.Col([
                            dcc.Location(id="url"), 
                            sidebar.layout,
                        ], md=2),

                        dbc.Col([
                            content
                    ], md=10)
                ])
            ], style={"padding": "0px"})


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return campaigns.layout

    elif pathname == "/adsets":
        return adsets.layout


if __name__ == "__main__":
    app.run_server(port=8051, host='0.0.0.0')
