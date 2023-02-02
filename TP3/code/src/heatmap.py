'''
    Contains some functions related to the creation of the heatmap.
'''
import plotly.express as px
import hover_template



def get_figure(data):
    '''
        Generates the heatmap from the given dataset.

        Make sure to set the title of the color bar to 'Trees'
        and to display each year as an x-tick. The x and y axes should
        be titled "Year" and "Neighborhood". 

        Args:
            data: The data to display
        Returns:
            The figure to be displayed.
    '''

    # TODO : Create the heatmap. Make sure to set dragmode=False in
    # the layout. Also don't forget to include the hover template.
    fig = px.imshow(data)
    pio.templates.default = 'simple_white+custom'
    fig.update_layout(
        xaxis_title='Year',
        yaxis_title='Neighborhood',
        dragmode = False,
        template = pio.templates.default
    ) 
    #hovertemplate is an attribute of go which isnt imported on this file 
    #the heatmap shows up on a separate tab
    fig.show()
    return fig