# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

df = (pd.read_csv("reportInheritance_aeolus_snomedtree_no_reports.tsv",sep="\t")
        .drop_duplicates(['concept_name'])
    )

df_graph = (df.sort_values(['n_reports'],ascending=True)
        )
df_table = (df.loc[:,['concept_name','n_reports']]
              .drop_duplicates()
              .sort_values(['n_reports'],ascending=False)
    )

def generate_table(dataframe, max_rows=100000):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )


app = dash.Dash()

app.layout = html.Div(children=[
    
    html.H1(children='Association of reports to adverse reactions in AEOLUS', style={'textAlign': 'center'}),

    html.Div(children=
        '''
        The Adverse Event Open Learning through Universal Standardization (AEOLUS) is the standardized dataset from the FDA's adverse drug reaction reporting surveillance system. Here, we are viewing the associated adverse reactions in reports at different levels of generalization from the SNOMED-CT clinical concepts hierarchy. Below, you can view the number of reports associated to the different SNOMED-CT concepts. 

        '''
        ),

    html.Br(),

    html.Div([
        dcc.Graph(
            id='concept_nreports_bar',
            figure={
                'data' : [
                    go.Bar(
                        y=df_graph['concept_name'],
                        x=df_graph['n_reports'],
                        orientation='h'
                        )
                    ],
                'layout' : go.Layout(
                    yaxis={'title' : 'Adverse Reactions',
                            'showticklabels' : False},
                    xaxis={'title' : 'Number of Reports'},
                    margin=go.Margin(
                        l=250,
                        r=20,
                        b=100,
                        t=50
    )
                )
            }
        ),
        generate_table(df_table)
    ])

])

if __name__ == '__main__':
    app.run_server(debug=True)