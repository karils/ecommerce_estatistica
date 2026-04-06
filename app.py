import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# carregar dados
df = pd.read_csv('ecommerce_estatistica.csv')

# separar numéricas
numericas = df.select_dtypes(include=['number'])

# gráficos
hist = px.histogram(numericas, title="Histograma das Variáveis")

scatter = px.scatter(
    numericas,
    x=numericas.columns[0],
    y=numericas.columns[1],
    title="Dispersão"
)

corr = numericas.corr()
heatmap = px.imshow(corr, text_auto=True, title="Mapa de Calor")

bar = px.bar(
    numericas.mean().sort_values(),
    title="Média das Variáveis"
)

coluna_cat = df.select_dtypes(include=['object']).columns[0]
pie = px.pie(df, names=coluna_cat, title="Distribuição")

density = px.density_contour(
    numericas,
    x=numericas.columns[0],
    y=numericas.columns[1],
    title="Densidade"
)

reg = px.scatter(
    numericas,
    x=numericas.columns[0],
    y=numericas.columns[1],
    trendline="ols",
    title="Regressão"
)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard E-commerce", style={'textAlign': 'center'}),
    dcc.Graph(figure=hist),
    dcc.Graph(figure=scatter),
    dcc.Graph(figure=heatmap),
    dcc.Graph(figure=bar),
    dcc.Graph(figure=pie),
    dcc.Graph(figure=density),
    dcc.Graph(figure=reg),
])

if __name__ == '__main__':
    app.run(debug=True)
