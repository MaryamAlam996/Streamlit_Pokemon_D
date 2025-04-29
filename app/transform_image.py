from PIL import Image
import pandas as pd
import requests


def get_image(url):
    response = requests.get(url, stream=True)
    im = Image.open(response.raw)
    return im



