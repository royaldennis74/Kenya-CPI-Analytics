import pandas as pd

def clean_spaces(df, columns):
    """
    Removes leading and trailing spaces from specified columns.
    """
    df[columns] = df[columns].apply(lambda x: x.str.strip())
    return df

def capitalize_columns(df, columns):
    """
    Capitalizes strings in the specified columns.
    """
    df[columns] = df[columns].apply(lambda x: x.str.title())
    return df

def replace_symbols(df, column, pattern, replacement=""):
    """
    Replaces unwanted symbols or text using regex.
    """
    df[column] = df[column].str.replace(pattern, replacement, regex=True)
    return df

def convert_dates(df, columns):
    """
    Converts selected columns to datetime format.
    """
    for col in columns:
        df[col] = pd.to_datetime(df[col], errors="coerce")
    return df
