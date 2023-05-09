
from dash import (
    Dash,
    html
)

def create_app(server):

    app = Dash(
        __name__,
        server=server,
        url_base_pathname="/dashboard/"
               )
    
    app.layout = html.Div(
        id = 'app',
        children=[
            html.H1("Hello Dashboard"),
            html.A(children="Home",
                   href="/")
        ]
    )

    return app