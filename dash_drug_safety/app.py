import dash
import dash_core_components as dcc
import dash_html_components as html
from textwrap import dedent

app = dash.Dash()

app.layout = html.Div(

	style={'background-color' : 'rgb(200,200,200)',
	        'font-size' : 11,
	        'font-family' : 'Verdana'
	        },
	children=[

		html.H1('Visualizing Drug Safety Data in a Web Framework: Interacting with, understanding, and communicating using just Python (no javascript, html, or css)',
			style={'text-align' : 'center'}
			),

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

if __name__ == '__main__':
	app.run_server(debug=True)