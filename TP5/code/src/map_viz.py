'''
    Contains the functions to set up the map visualization.

'''

import plotly.graph_objects as go
import plotly.express as px

import hover_template as hover


def add_choro_trace(fig, montreal_data, locations, z_vals, colorscale):
    '''
        Adds the choropleth trace, representing Montreal's neighborhoods.

        Note: The z values and colorscale provided ensure every neighborhood
        will be grey in color. Although the trace is defined using Plotly's
        choropleth features, we are simply defining our base map.

        The opacity of the map background color should be 0.2.

        Args:
            fig: The figure to add the choropleth trace to
            montreal_data: The data used for the trace
            locations: The locations (neighborhoods) to show on the trace
            z_vals: The table to use for the choropleth's z values
            colorscale: The table to use for the choropleth's color scale
        Returns:
            fig: The updated figure with the choropleth trace

    '''
    # TODO : Draw the map base
    
    fig.add_trace(
        go.Choroplethmapbox(
            geojson=montreal_data, 
            locations=locations, 
            z=z_vals, 
            colorscale=colorscale, 
            marker_opacity=0.2, 
            featureidkey="properties.NOM",
            showscale=False,
        )
    )
    
    fig.update_traces(hovertemplate=hover.map_base_hover_template())
    
    return fig


def add_scatter_traces(fig, street_df):
    '''
        Adds the scatter trace, representing Montreal's pedestrian paths.

        The marker size should be 20.

        Args:
            fig: The figure to add the scatter trace to
            street_df: The dataframe containing the information on the
                pedestrian paths to display
        Returns:
            The figure now containing the scatter trace

    '''
    # TODO : Add the scatter markers to the map base
    
    colors = ['royalblue', 'tomato', 'mediumspringgreen', 'mediumpurple', 'orange', 'turquoise', 'hotpink']

    trace_groups = {}

    for i, row in street_df.iterrows():
        name = row['properties.TYPE_SITE_INTERVENTION']
        if name in trace_groups:
            trace_groups[name].append(
                go.Scattermapbox(
                    lon=[row['properties.LONGITUDE']],
                    lat=[row['properties.LATITUDE']],
                    hovertemplate=hover.map_marker_hover_template(name),
                    mode='markers',
                    marker=dict(
                        size=20,
                        opacity=1
                    ),
                )
            )
        else:
            trace_groups[name] = [
                go.Scattermapbox(
                    name=name,
                    lon=[row['properties.LONGITUDE']],
                    lat=[row['properties.LATITUDE']],
                    hovertemplate=hover.map_base_hover_template(),
                    mode='markers',
                    marker=dict(
                        size=20,
                        opacity=1
                    ),
                    customdata=[
                        row["properties.NOM_PROJET"],
                        row["properties.MODE_IMPLANTATION"],
                        row["properties.OBJECTIF_THEMATIQUE"],
                    ],
                )
            ]
            
    for i, (name, traces) in enumerate(trace_groups.items()):
        fig.add_trace(go.Scattermapbox(
            name=name,
            lon=[trace['lon'][0] for trace in traces],
            lat=[trace['lat'][0] for trace in traces],
            mode='markers',
            hovertemplate=hover.map_marker_hover_template(name),
            marker=dict(
                size=20,
                color=colors[i % len(colors)],
                opacity=1
            ),
        ))

    return fig