from PIL import Image
import pandas as pd
import requests


def get_image(url):
    response = requests.get(url, stream=True)
    im = Image.open(response.raw)
    return im


def get_image_url(pokedex_id: int) -> str:
    pokedex_id = str(pokedex_id).zfill(3)
    image_url = f"https://raw.githubusercontent.com/HybridShivam/Pokemon/refs/heads/master/assets/images/{pokedex_id}.png"
    return image_url
