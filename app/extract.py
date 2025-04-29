import pandas as pd
# Function to extract data

# Test if pytest works
def sum(x):
    return x + 5


# Write code for extracting data below
def extract_from_csv(file_path: str) -> pd.DataFrame:
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        raise Exception(f'An unexpected error occurred.\nError: {e}.')
