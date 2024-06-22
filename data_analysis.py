import pandas as pd

def analyze_data(df):
    """
    Performs data analysis on the DataFrame.

    Parameters:
    - df (pd.DataFrame): Input DataFrame.

    Returns:
    - pd.DataFrame: Grouped and sorted data.
    """
    kolom_analisis = ['terms', 'name', 'price', 'Sales Volume']
    grouped_data = df.groupby('terms')[kolom_analisis].apply(lambda x: x.nlargest(5, columns='Sales Volume')).reset_index(drop=True)
    sorted_df = df.sort_values(by=['terms', 'Sales Volume'], ascending=[True, False])
    
    return grouped_data, sorted_df
