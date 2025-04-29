import pandas as pd


def extract_from_csv(file_path: str) -> pd.DataFrame:
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        raise Exception(f'An unexpected error occurred.\nError: {e}.')


def drop_columns(df):
    """ Drop unused columns"""
    columns_to_drop = [
        df.columns[0], 'german_name', 'egg_type_number',
        'japanese_name', 'egg_type_1', 'egg_type_2',
        'egg_cycles', 'base_friendship', 'base_experience',
        'growth_rate', 'against_normal', 'against_fire',
        'against_water', 'against_electric', 'against_grass',
        'against_ice', 'against_fight', 'against_poison',
        'against_ground', 'against_flying', 'against_psychic',
        'against_bug', 'against_rock', 'against_ghost',
        'against_dragon', 'against_dark', 'against_steel', 'against_fairy',
        'type_number', 'abilities_number', 'percentage_male', 'catch_rate'
    ]
    df.drop(columns_to_drop, axis=1, inplace=True)
    return df


def drop_empty_rows(df):
    """ Drop rows with no abilities"""
    df = df.dropna(subset='ability_1')
    return df


def clean_categorical_columns(df):
    """ Fill null values with None"""
    df['type_2'] = df['type_2'].fillna('None')
    df['ability_2'] = df['ability_2'].fillna('None')
    df['ability_hidden'] = df['ability_hidden'].fillna('None')
    return df


def get_image_url(pokedex_id: int) -> str:
    pokedex_id = str(pokedex_id).zfill(3)
    image_url = f"https://raw.githubusercontent.com/HybridShivam/Pokemon/refs/heads/master/assets/images/{pokedex_id}.png"
    return image_url


def add_url_as_new_column(df):
    df['image_url'] = df['pokedex_number'].apply(lambda x: get_image_url(x))
    return df


def extract_and_clean_data(file_path):
    """ Extract and clean Pokemon dataset"""
    df = extract_from_csv(file_path)
    df = drop_columns(df)
    df = drop_empty_rows(df)
    df = clean_categorical_columns(df)
    df = add_url_as_new_column(df)
    return df



