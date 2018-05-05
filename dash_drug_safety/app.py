import dash
import dash_core_components as dcc
import dash_html_components as html
from textwrap import dedent

app = dash.Dash()

app.layout = html.Div([

    dcc.Location(id='url', refresh=True),
    html.Div(id='page-content')
	
])	
	
	
index_page = html.Div(
	
	style={'font-family' : 'Verdana'
	        },
	children=[

		html.H1('Visualizing Drug Safety Data in a Web Framework: Interacting with, understanding, and communicating using Python',
			style={'text-align' : 'center','font-size' : 48}
			),

		html.Hr(),

		dcc.Link('Go to Talk Outline', href='/outline',style={'font-size' : 16,'color' : 'blue'})
])

outline = html.Div([

		dcc.Link('Go to Home Page', href='/',style={'font-size' : 16,'color' : 'blue'}),

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

			- What is Dash

			- What makes Dash

			   + Flask and React

			   + two components: 

			      * wrap html in python. The full power of css is available to you

			      * core components, like Graphs and Tables and Dropdowns.

			- What can you do with it?

			   + Show dash app gallery

			- What am I doing with it?

			   * Explain

			   * Walk through components/parts I use (show code)

			   * Show app
			''')
			)

])


# Update the index
# This callback constantly looks at the page location with id="url",
# and gives the pathname to the function immediately following the callback.
# The function then gives what it returns, which is a new layout.
# That new layout itself has a url! So the new url is displayed
# Every time we click the link, the pathname changes (href) and we get returned the 
# corresponding page. 
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/outline':
        return outline
    else:
        return index_page

if __name__ == '__main__':
	app.run_server(debug=True)