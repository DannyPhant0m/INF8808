'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd
from modes import MODE_TO_COLUMN


def summarize_lines(my_df):
    '''
        Sums each player's total of number of lines and  its
        corresponding percentage per act.

        The sum of lines per player per act is in a new
        column named 'PlayerLine'.

        The percentage of lines per player per act is
        in a new column named 'PlayerPercent'

        Args:
            my_df: The pandas dataframe containing the data from the .csv file
        Returns:
            The modified pandas dataframe containing the
            information described above.
    '''
    # TODO : Modify the dataframe, removing the line content and replacing
    # it by line count and percent per player per act
    
    my_df = pd.read_csv('assets/data/romeo_and_juliet.csv')
    
    #On fait la somme des lignes pour chaque joueur dans chaque acte
    new_cleaned_list = my_df.groupby(['Act', 'Player']).size().reset_index(name='LineCount')
    
    #On trouve le pourcentage des lignes pour chaque joueur dans chaque acte
    new_cleaned_list['LinePercent'] = 100 * new_cleaned_list['LineCount'] / new_cleaned_list.groupby('Act')['LineCount'].transform('sum') 
    
    #On ordonne la liste selon le nombre de lignes pour ajouter de la clarté dans le tri
    my_df = new_cleaned_list.sort_values(by=['Act','LineCount'], ascending=[True,False])
        
    return my_df


def replace_others(my_df):
    '''
        For each act, keeps the 5 players with the most lines
        throughout the play and groups the other plyaers
        together in a new line where :

        - The 'Act' column contains the act
        - The 'Player' column contains the value 'OTHER'
        - The 'LineCount' column contains the sum
            of the counts of lines in that act of
            all players who are not in the top
            5 players who have the most lines in
            the play
        - The 'PercentCount' column contains the sum
            of the percentages of lines in that
            act of all the players who are not in the
            top 5 players who have the most lines in
            the play

        Returns:
            The df with all players not in the top
            5 for the play grouped as 'OTHER'
    '''
    # TODO : Replace players in each act not in the top 5 by a
    # new player 'OTHER' which sums their line count and percentage
    
    
    #On vient trouver les 5 joueurs avec le plus de lignes pour tous les actes confondus
    top_players_list = my_df.groupby('Player').sum('LineCount')
    top_players_list = top_players_list.sort_values(by=['LineCount'], ascending=[False])
    top_players = top_players_list.head(5)
    top_players_list = my_df[my_df.Player.isin(top_players.index)]
    
    #On vient trouver tous les joueurs qui ne sont pas dans le top 5
    all_other_players = my_df[~my_df.Player.isin(top_players.index)]
    all_other_players = all_other_players.groupby('Act').agg({
        'Player' : 'last',
        'LineCount' : 'sum',
        'LinePercent' : 'sum'
    }).reset_index()
    all_other_players['Player'] = 'OTHER'

    #On assemble les deux listes ensemble pour retrouver notre df initiale triée
    my_df = pd.concat([top_players_list, all_other_players])
    my_df = my_df.sort_values(by=['Act'], ascending=[True])
    
    return my_df


def clean_names(my_df):
    '''
        In the dataframe, formats the players'
        names so each word start with a capital letter.

        Returns:
            The df with formatted names
    '''
    # TODO : Clean the player names
    
    my_df['Player'] = my_df['Player'].str.title()
    
    my_df = my_df.sort_values(by=['Act','Player'], ascending=[True,True])

    return my_df
