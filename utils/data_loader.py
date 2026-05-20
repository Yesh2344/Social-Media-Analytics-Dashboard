import pandas as pd

def load_data():
    try:
        data = pd.read_csv('data.csv')
        return data
    except FileNotFoundError:
        raise FileNotFoundError('Data file not found')
    except pd.errors.EmptyDataError:
        raise ValueError('Data file is empty')
    except pd.errors.ParserError:
        raise ValueError('Data file is corrupted')