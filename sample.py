
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': 'black',
    'text': 'green'
}

app.layout = html.Div(children=[
    html.H1(
        children='Dashでこんなん簡単にできるんか！！',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
        ),

    html.Div(
        children='''
        Dash: A web application framework for Python.
        ''',
        style={
            'textAlign': 'center',
            'color': colors['text'],
        }
    ),


    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3, 4, 5, 6, 7, 8], 'y': [7, 6, 3, 6, 5, 4, 4, 6], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3, 4, 5, 6, 7, 8], 'y': [2, 4, 5, 7, 3, 8, 6, 2], 'type': 'bar', 'name': 'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization',
                # 'plot_bgcolor':colors['background'],
                # 'paper_bgcolor':colors['background'],
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
