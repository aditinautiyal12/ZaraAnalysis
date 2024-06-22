import pandas as pd

def load_data(file_path):
    """
    Loads data from CSV file.

    Parameters:
    - file_path (str): Path to the CSV file.

    Returns:
    - pd.DataFrame: Loaded DataFrame.
    """
    df = pd.read_csv(file_path, sep=';')
    return df
