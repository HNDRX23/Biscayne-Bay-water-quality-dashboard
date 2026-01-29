import requests
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://api.nasa.gov/planetary/apod?api_key="
unique_key = os.getenv("NASA_API_KEY")
print(unique_key)


# we never expose passwords tokens in code

def apod_generator(url,unique_key):
    final_url = url + unique_key
    response = requests.get(final_url)
    return response.json()

    api_key = os.getenv("NASA_API_KEY")


