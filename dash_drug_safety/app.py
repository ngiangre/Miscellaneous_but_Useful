import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
import plotly.graph_objs as go

from textwrap import dedent
from pyarrow import feather
import numpy as np
import pandas as pd


app = dash.Dash()
app.config.suppress_callback_exceptions = True

#####load and process data#####

data = feather.read_feather(source='/Users/npg2108/Research/Projects/pediatrics/data/20180214_aeolous_stats.tsv.feather',nthreads=16,columns=['drug_concept_name','aed','age_cat'])

uniq_drugs = data.query('aed == "AED"').drug_concept_name.unique()
uniq_drugs = uniq_drugs[np.argsort(uniq_drugs)]

all_age_cat_counts = (data.groupby(['age_cat'])
						  .apply(lambda x : x.shape[0])
					 )
all_age_cat_counts_x = all_age_cat_counts.index.tolist()
all_age_cat_counts_y = all_age_cat_counts.values
all_age_cat_counts_y_norm = np.round((all_age_cat_counts_y / all_age_cat_counts.sum()) * 100,0)


##########


app.layout = html.Div(

	children=[

		dcc.Location(id='url', refresh=True),
		html.Div(id='page-content')
		]
	)	
	
	
index_page = html.Div(
	
	style={'font-family' : 'Verdana'
	        },
	children=[

		html.H1('Visualizing Drug Safety Data in a Web Framework: Interacting with, understanding, and communicating using Python',
			style={'text-align' : 'center','font-size' : 48}
			),

		dcc.Link('Go to ADR table Page', href='/table_page',
			style={'font-size' : 16,'color' : 'blue'}),

		html.Br(),

		dcc.Link('Go to ADR age relation Page', href='/age_page',
			style={'font-size' : 16,'color' : 'blue'}),

		html.Br(),

		dcc.Link('Go to Talk Outline', href='/outline',
			style={'font-size' : 16,'color' : 'blue','left' : '50%',
			'width' : '20%'}),

		html.Hr(),

		dcc.Markdown(dedent('''

			**Academic researchers extensively curate datasets that are of interest to the general public. Often, these data and results from research projects using this data appear in Academic journals as publications, which are the main modes of research communication, funding eligibility, and career advancement. However, research publications are esoteric and are not feasible for widespread communication to the public. Thus, there requires a medium that allows for general communication of research results, along with scholarly communication in peer-reviewed journals.**

			**Dash, from Plotly, is a web framework for interacting and communicating data using python. This app uses Dash to communicate and make interactive data curated from the Federal Drug Administration's Adverse Event Reporting System.**

			'''))
		]
	)


table_page = html.Div(

	style={},

	children=[

		html.H1('Table Page'),

		dcc.Link('Go to Home Page', href='/',
			style={'font-size' : 16,'color' : 'blue'}),

		html.Br(),

		dcc.Link('Go to ADR age relation Page', href='/age_page',
			style={'font-size' : 16,'color' : 'blue'}),

		html.Br(),

		dcc.Link('Go to Talk Outline', href='/outline',
			style={'font-size' : 16,'color' : 'blue','left' : '50%',
			'width' : '20%'}),

		html.Hr()
		]
	),


age_page = html.Div(

	style={},

	children=[

		html.H1('ADR age relation'),

		dcc.Link('Go to Home Page', href='/',
			style={'font-size' : 16,'color' : 'blue'}),

		html.Br(),

		dcc.Link('Go to ADR table Page', href='/table_page',
			style={'font-size' : 16,'color' : 'blue'}),

		html.Br(),

		dcc.Link('Go to Talk Outline', href='/outline',
			style={'font-size' : 16,'color' : 'blue','left' : '50%',
			'width' : '20%'}),

		html.Hr(),

		html.Div(
			style={'class' : "col-sm-4",'border' : '2px solid black',
			'float' : 'left'},
			children=[
			
			html.H1('How many patients are taking these drugs?',
				style={'text-align' : 'center','font-size' : 18}),
			
			dcc.Dropdown(
				id='drug_count',
				options=[{'label' : i, 'value' : i} for i in uniq_drugs],
				value=uniq_drugs[0]),

    		html.Div(id='drug_output',
    			style={'text-align' : 'center'})

			]),

		dcc.Graph(
	        id='drug-reports-at-ages',
	        style={'class' : 'col-sm-4','float' : 'right'},
		)

		]
	)


outline = html.Div(

	style={},

	children=[

		dcc.Link('Go to Home Page', href='/',
			style={'font-size' : 16,'color' : 'blue'}),

		html.Br(),

		dcc.Link('Go to ADR table Page', href='/table_page',
			style={'font-size' : 16,'color' : 'blue'}),

		html.Br(),

		dcc.Link('Go to ADR age relation Page', href='/age_page',
			style={'font-size' : 16,'color' : 'blue'}),

		html.Hr(),

		dcc.Markdown(dedent('''

			# Talk Description:

			   * Our shared responsibility as researchers is to communicate to the larger community the fruits of our labor. Academic papers, while essential for advancing science, falls short to reaching the general public. Larger news agencies, such as the NYTimes, make use of tools in javascript native to the web browser to engage readers with news stories and effectively communicate accompanying data interweaving with text and graphs. Jupyter notebooks, Rmarkdown, and many more computational notebooks have revolutionized reproducible research. In both cases, however, interactivity is lacking. Plotly's Dash allows for communicating, visualizing, and interacting with data that is easy for the researcher to build using just python code. Dash applications used in academic research not only increases communication with the general public but also promotes necessary interactivity components to multiply the effect of understanding.

			# Outline of talk:

			- Motivation for using dash. To enhance,

			   + understanding of data

			   + interaction with data

			   + communication of data to the wider community

			   + Why not Shiny and R?

			      * Shiny doesn't render very quick, Dash does.

			- [What is Dash](https://medium.com/@plotlygraphs/introducing-dash-5ecf7191b503)

			   + Python framework for building analytical web applications, no javascript required.

			   + 3 years old - announced last June.

			   + Open source and MIT licensed.

			   + declarative and reactive

			   + reactive decorators create the reactivity behind the app. It's always "on".

			- What makes Dash

			   + Flask (communicates json packets over http requests), Plotly.js (built on top of D3, renders charts), and React (renders components)

			   + Other Flask Plugins can be used too. 

			   + Can use the full power of CSS. 

			   + two components: 

			      * wrap html in python. The full power of css is available to you

			      * core components, like Graphs and Tables and Dropdowns.

			   + Dash components are Python classes that encode the properties and values of a specific React component and that serialize to JSON. Uses dynamic programming to automatically generate the standard Python classes from annotated React propTypes. Get automatic argument validation, docstrings, and more. 

			   + Not limited to using only the standard Dash components library - can port a React.js components into a python class that can be [used by Dash](https://plot.ly/dash/plugins). 



			- What can you do with it?

			   + Show dash app gallery

			- What am I doing with it?

			   * Explain

			   * Walk through components/parts I use (show code)

			   * Show app
			   
			''')
			)
		]
	)


# Update the index
# This callback constantly looks at the page location with id="url",
# and gives the pathname to the function immediately following the callback.
# The function then gives what it returns, which is a new layout.
# That new layout itself has a url! So the new url is displayed
# Every time we click the link, the pathname changes (href) and we get returned the 
# corresponding page. 
@app.callback(
	dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/outline':
        return outline
    if pathname == '/table_page':
    	return table_page
    if pathname == '/age_page':
    	return age_page
    else:
        return index_page


#Show number of patients taking selected drug in dataset
@app.callback(
    dash.dependencies.Output('drug_output', 'children'),
    [dash.dependencies.Input('drug_count', 'value')])
def callback_drug(value):
    return 'There are {} patients that reported taking {}'.format(
    	data.query('drug_concept_name==@value').count().values[0],
    	value)

#Update bar graph for drug
@app.callback(
	dash.dependencies.Output('drug-reports-at-ages','figure'),
	[dash.dependencies.Input('drug_count','value')])
def callback_drug_reports_at_ages_bars(value):

	series = (data.query('drug_concept_name == @value')
						   .groupby(['age_cat'])
						   .apply(lambda x : x.shape[0])
						   )
	x = series.index.tolist()
	y = series.values
	y_norm = np.round((series.values / series.sum()) * 100,0)

	drug_trace = go.Bar(
		                x=x,
		                y=y_norm,
		                name='{}'.format(value),
		                text=['{} reports'.format(i) for i in y],
		                marker=go.Marker(
		                    color='rgb(55, 83, 109)'
		                )
		            )

	all_trace = go.Bar(
		                x=all_age_cat_counts_x,
		                y=all_age_cat_counts_y_norm,
		                name='All drugs',
		                text=['{} reports'.format(i) for i in all_age_cat_counts_y],
		                marker=go.Marker(
		                    color='rgb(180,180,180)'
		                )
		            )
	return { 'data' : [
		            all_trace,drug_trace
		            ],
	            'layout' : go.Layout(
		            title='Patients taking {} at different age intervals'.format(value),
		            showlegend=True,
		            yaxis = dict(
		            	title="Percentage of reports",
		            	type='percent'
		            ),
		            xaxis = dict(
		            	title="Age category"
		            ),
		            legend=go.Legend(
		                x=0,
		                y=1.0
		            ),
		            margin=go.Margin(l=40, r=20, t=40, b=100)
	        	)
			}

#enable bootstrap styling
external_css = ["https://bootswatch.com/3/paper/bootstrap.css"]

for css in external_css:
    app.css.append_css({"external_url": css})


if __name__ == '__main__':
	app.run_server(debug=True)