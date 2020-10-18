
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Label('dropdown'),
    dcc.Dropdown(
        options=[
            {'label': '佐藤', 'value': 'sato'},
            {'label': '鈴木', 'value': 'suzuki'},
            {'label': '田中', 'value': 'tanaka'},
            {'label': '渡辺', 'value': 'watanabe'},
        ],
        value='tanaka'
    ),

    html.Label('Multi-Select Dropdown'),
])


if __name__ == '__main__':
    app.run_server(debug=True)
