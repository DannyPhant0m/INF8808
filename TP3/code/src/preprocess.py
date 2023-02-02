'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd


def convert_dates(dataframe):
    '''
        Converts the dates in the dataframe to datetime objects.

        Args:
            dataframe: The dataframe to process
        Returns:
            The processed dataframe with datetime-formatted dates.
    '''
    # TODO : Convert dates
    
    dataframe = pd.read_csv('assets/data/arbres.csv')
    
    dataframe["Date_Plantation"] = pd.to_datetime(dataframe["Date_Plantation"], format='%Y-%m-%d')
    
    return dataframe


def filter_years(dataframe, start, end):
    '''
        Filters the elements of the dataframe by date, making sure
        they fall in the desired range.

        Args:
            dataframe: The dataframe to process
            start: The starting year (inclusive)
            end: The ending year (inclusive)
        Returns:
            The dataframe filtered by date.
    '''
    # TODO : Filter by dates
    
    filtered_dataframe = dataframe.loc[(dataframe.Date_Plantation.dt.year >= start)
                                       & (dataframe.Date_Plantation.dt.year <= end)]
    
    filtered_dataframe = filtered_dataframe.sort_values(by=["Date_Plantation"], ascending=[True])
        
    return filtered_dataframe


def summarize_yearly_counts(dataframe):
    '''
        Groups the data by neighborhood and year,
        summing the number of trees planted in each neighborhood
        each year.

        Args:
            dataframe: The dataframe to process
        Returns:
            The processed dataframe with column 'Counts'
            containing the counts of planted
            trees for each neighborhood each year.
    '''
    # TODO : Summarize df
    
    dataframe = dataframe.groupby(['Arrond_Nom','Arrond',dataframe.Date_Plantation.dt.year]).size().reset_index(name='Count')
    
    return dataframe


def restructure_df(yearly_df):
    '''
        Restructures the dataframe into a format easier
        to be displayed as a heatmap.

        The resulting dataframe should have as index
        the names of the neighborhoods, while the columns
        should be each considered year. The values
        in each cell represent the number of trees
        planted by the given neighborhood the given year.

        Any empty cells are filled with zeros.

        Args:
            yearly_df: The dataframe to process
        Returns:
            The restructured dataframe
    '''
    # TODO : Restructure df and fill empty cells with 0
    
    restruct_df = yearly_df.drop(columns=["Arrond"])
    
    restruct_df["Date_Plantation"] = restruct_df["Date_Plantation"].astype(str) + '-12-31'
    
    restruct_df = restruct_df.pivot(index="Arrond_Nom", columns="Date_Plantation", values="Count")
    
    restruct_df = restruct_df.fillna(0)
    
    return restruct_df


def get_daily_info(dataframe, arrond, year):
    '''
        From the given dataframe, gets
        the daily amount of planted trees
        in the given neighborhood and year.

        Args:
            dataframe: The dataframe to process
            arrond: The desired neighborhood
            year: The desired year
        Returns:
            The daily tree count data for that
            neighborhood and year.
    '''
    # TODO : Get daily tree count data and return
    
    # Have to implement heatmap first to see if it works    
    daily_tree_count = dataframe.get_value(arrond,year)
    
    return daily_tree_count
