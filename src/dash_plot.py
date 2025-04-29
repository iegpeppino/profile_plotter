from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import locale

locale.setlocale(locale.LC_ALL, 'es_ES.utf8')


df = pd.read_csv("src/TC1-Alejandro.csv", parse_dates=["Reloj Perfil 1"], header=0)
df['Reloj Perfil 1'] = pd.to_datetime(df["Reloj Perfil 1"], format="%d/%m/%Y %H:%M:%S")
df = df.rename(columns={"Reloj Perfil 1": "Fecha"})

app = Dash(__name__)

app.layout = html.Div(
    style={
        "backgroundColor": "#e8f5e9",
        "padding": "40px",
        "fontFamily": "'Poppins', 'Roboto', sans-serif",
        "minHeight": "100vh"
    },
    children=[
        # HEADER + DATE RANGE ROW
        html.Div(
            style={
                "display": "flex",
                "justifyContent": "space-between",
                "alignItems": "center",
                "marginBottom": "40px",
                "flexWrap": "wrap"  # 👈 Makes it responsive on small screens
            },
            children=[
                html.H1(
                    'Perfil de carga',
                    style={
                        "color": "#1b5e20",
                        "fontSize": "40px",
                        "fontWeight": "bold",
                        "margin": "0"
                    }
                ),
                html.Div(
                    children=[
                        html.H4(
                            "Rango de Fechas",
                            style={
                                "color": "#2e7d32",
                                "fontSize": "18px",
                                "marginBottom": "5px",
                                "textAlign": "right"
                            }
                        ),
                        dcc.DatePickerRange(
                            id='date-picker-range',
                            start_date=df["Fecha"].min(),
                            end_date=df["Fecha"].max(),
                            display_format="YYYY-MM-DD",
                            style={
                                "backgroundColor": "white",
                                "border": "2px solid #66bb6a",
                                "borderRadius": "10px",
                                "padding": "10px",
                                "fontSize": "16px"
                            }
                        ),
                    ],
                    style={
                        "textAlign": "right"
                    }
                )
            ]
        ),

        # GRAPH
        dcc.Graph(
            id="time-series-chart",
            style={
                "backgroundColor": "white",
                "padding": "30px",
                "borderRadius": "12px",
                "boxShadow": "0 4px 12px rgba(0,0,0,0.1)",
                "marginBottom": "40px",
                "height": "600px"
            }
        ),

        # DROPDOWN
        html.Div(
            style={"marginTop": "20px"},
            children=[
                html.H4(
                    "Elegir parámetros:",
                    style={
                        "color": "#2e7d32",
                        "fontSize": "24px",
                        "marginBottom": "10px"
                    }
                ),
                dcc.Dropdown(
                    id="column-dropdown",
                    options=[{"label": col, "value": col} for col in df.columns if col != "Fecha"],
                    multi=True,
                    value=[],
                    style={
                        "backgroundColor": "white",
                        "border": "2px solid #66bb6a",
                        "borderRadius": "10px",
                        "padding": "12px",
                        "fontSize": "16px",
                        "color": "#1b5e20",
                        "width": "100%",
                        "maxWidth": "500px"
                    }
                ),
            ]
        )
    ]
)

@app.callback(
    Output("time-series-chart", "figure"),
    [Input("date-picker-range", "start_date"),
     Input("date-picker-range", "end_date"),
     Input("column-dropdown", "value")]
)
def update_chart(start_date, end_date, selected_columns):
    filtered_df = df[(df["Fecha"] >= start_date) & (df["Fecha"] <= end_date)]

    if not selected_columns:
        return px.line(filtered_df, x="Fecha", y=[],  title="No hay parametros seleccionados")

    fig = px.line(
        filtered_df, x="Fecha",
        y=selected_columns,
        title= ', '.join(selected_columns)
        )
    return fig

if __name__ == "__main__":
    app.run(debug=True)