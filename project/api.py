import os
from dotenv import load_dotenv
import requests

load_dotenv()

def get_geocoding_data_by_city(city):
  response = requests.get(os.getenv('API_NINJAS_GEOCODING_URL') + (city or ''), headers={ 'X-Api-Key': os.getenv('API_NINJAS_API_KEY') })
  return response.json()[0] if response.status_code == requests.codes['ok'] else {}


def get_world_time_data_by_location(lat, lon):
  response = requests.get(os.getenv('API_NINJAS_WORLD_TIME_URL').format(lat, lon), headers={'X-Api-Key': os.getenv('API_NINJAS_API_KEY') })
  return response.json() if response.status_code == requests.codes['ok'] else {}


def get_weather_data_by_location(lat, lon):
  response = requests.get(os.getenv('WEATHER_API_URL'), params={
      'key': os.getenv('WEATHER_API_API_KEY'),
      'q': f'{lat},{lon}'
    })
  return response.json() if response.status_code == requests.codes['ok'] else {}


def get_hockey_scores():
  response = requests.get(os.getenv('NHL_SCORE_API_URL'))
  return response.json() if response.status_code == requests.codes['ok'] else {}