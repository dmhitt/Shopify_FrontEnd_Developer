import json
import requests
from .config import key


def api_call():

    start_date = "2022-01-01"
    end_date = "2022-01-20"

    target_url = f"https://api.nasa.gov/planetary/apod?api_key={key}&start_date={start_date}&end_date={end_date}"
    earth_pictures  = requests.get(target_url).json()
   

    return earth_pictures