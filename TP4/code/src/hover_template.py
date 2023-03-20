'''
    Provides the template for the tooltips.
'''


def get_bubble_hover_template():
    '''
        Sets the template for the hover tooltips.
        
        Contains four labels, followed by their corresponding
        value and units where appropriate, separated by a
        colon : country, population, GDP and CO2 emissions.

        The labels' font is bold and the values are normal weight

        returns:
            The content of the tooltip
    '''
    # TODO : Generate tooltip
    hover_template = """
        <span style = 'font-weight: Bold;'>Country</span> : %{customdata[0]}</span><br>
        <span style = 'font-weight: Bold;'>Population</span> : %{customdata[1]}</span><br>
        <span style = 'font-weight: Bold;'>GDP</span> : %{x} $ (USD)</span><br>
        <span style = 'font-weight: Bold;'>CO2 emissions</span> : %{y} metric tonnes</span>""" + "<extra></extra>"
        
    return hover_template
