'''
    Provides the templates for the tooltips.
'''


def get_heatmap_hover_template():
    '''
        Sets the template for the hover tooltips in the heatmap.

        Contains three labels, followed by their corresponding
        value, separated by a colon : neighborhood, year and
        trees planted.

        The labels are font 'Roboto Slab' and bold. The values
        are font 'Roboto' and regular weight.
    '''
    # TODO : Define and return the hover template
    hover_template = """
        <span style = 'font-family: Roboto Slab; font-weight: Bold;'>Neighborhood</span style = 'font-family: Roboto;'> : %{y}</span><br>
        <span style = 'font-family: Roboto Slab; font-weight: Bold;'>Year</span style = 'font-family: Roboto;'> : %{x}</span><br>
        <span style = 'font-family: Roboto Slab; font-weight: Bold;'>Trees planted</span style = 'font-family: Roboto;'> : %{z}</span>""" + "<extra></extra>"
        
    return hover_template

def get_linechart_hover_template():
    '''
        Sets the template for the hover tooltips in the heatmap.

        Contains two labels, followed by their corresponding
        value, separated by a colon : date and trees planted.

        The labels are font 'Roboto Slab' and bold. The values
        are font 'Roboto' and regular weight.
    '''
    # TODO : Define and return the hover template
    hover_template = """
        <span style = 'font-family: Roboto Slab; font-weight: Bold;'>Date</span style = 'font-family: Roboto;'> : %{y}</span><br>
        <span style = 'font-family: Roboto Slab; font-weight: Bold;'>Trees</span style = 'font-family: Roboto;'> : %{x}</span>""" + "<extra></extra>"
        
    return hover_template

