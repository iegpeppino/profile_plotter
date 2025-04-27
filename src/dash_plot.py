from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import locale

locale.setlocale(locale.LC_ALL, 'es_ES.utf8')


df = pd.read_csv("src/TC1-Alejandro.csv", parse_dates=["Reloj Perfil 1"], header=0)
df['Reloj Perfil 1'] = pd.to_datetime(df["Reloj Perfil 1"], format="%d/%m/%Y %H:%M:%S")
df = df.rename(columns={"Reloj Perfil 1": "Fecha"})

app = Dash(__name__)

app.layout = html.Div([
    html.H1('Perfil de carga', style={"text-align":"center"}),
    html.H4("Rango de Fechas"),
    dcc.DatePickerRange(
        id='date-picker-range',
        start_date=df["Fecha"].min(),
        end_date=df["Fecha"].max(),
        display_format="YYYY-MM-DD"
    ),
    dcc.Graph(id= "time-series-chart"),
    html.H4("Elegir parametros:"),
    dcc.Dropdown(
        id="column-dropdown",
        options= [{"label": col, "value": col} for col in df.columns if col != "Fecha"],
        multi= True,
        value= []
    ),
])

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
      
        title="Perfiles de Carga"
        )
    return fig

if __name__ == "__main__":
    app.run(debug=True)