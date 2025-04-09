import dash
from dash import dcc, html
import dash.dependencies as dd
import pandas as pd
import plotly.express as px

# Load the sales data
sales_df = pd.read_csv('sales_data.csv')

# Initialize the Dash app
app = dash.Dash(__name__)
app.title = "Company Growth Dashboard"

# Define color theme
colors = {
    'background': '#ffffff',
    'text': '#0033cc'  # Blue
}

# Create visualizations
bar_fig = px.bar(sales_df, x='Product', y='Revenue ($)', color='Region', 
                 title='Revenue by Product', color_discrete_sequence=['#0033cc'])

line_fig = px.line(sales_df.sort_values('Month'), x='Month', y='Revenue ($)', color='Region', 
                   title='Monthly Revenue Growth', color_discrete_sequence=['#0033cc'])

pie_fig = px.pie(sales_df, names='Category', values='Revenue ($)', 
                 title='Revenue Distribution by Category', color_discrete_sequence=['#0033cc'])

scatter_fig = px.scatter(sales_df, x='Units Sold', y='Revenue ($)', color='Product', 
                         title='Units Sold vs Revenue', color_discrete_sequence=px.colors.qualitative.Bold)

heatmap_fig = px.density_heatmap(sales_df, x='Region', y='Category', z='Revenue ($)', 
                                 title='Revenue Heatmap by Region and Category', 
                                 color_continuous_scale='Blues')

# Layout
app.layout = html.Div(style={'backgroundColor': colors['background'], 'padding': '10px'}, children=[
    html.H1(
        children='📈 Company Growth Dashboard',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Visualizing key company metrics.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='bar-chart',
        figure=bar_fig
    ),

    dcc.Graph(
        id='line-chart',
        figure=line_fig
    ),

    dcc.Graph(
        id='pie-chart',
        figure=pie_fig
    ),

    dcc.Graph(
        id='scatter-plot',
        figure=scatter_fig
    ),

    dcc.Graph(
        id='heatmap',
        figure=heatmap_fig
    )
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
