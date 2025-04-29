import pandas as pd

def get_image():
    return None

def get_image_url(pokedex_id: int) -> str:
    pokedex_id = str(pokedex_id).zfill(3)
    image_url = f"https://raw.githubusercontent.com/HybridShivam/Pokemon/refs/heads/master/assets/images/{pokedex_id}.png"
    return image_url


