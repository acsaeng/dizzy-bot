import os
from dotenv import load_dotenv
import requests

load_dotenv()

def getGeocodingDataByCity(city):
  response = requests.get(os.getenv('API_NINJAS_GEOCODING_URL') + (city or ''), headers={ 'X-Api-Key': os.getenv('API_NINJAS_API_KEY') })
  return response.json()[0] if response.status_code == requests.codes['ok'] else {}


def getWorldTimeDataByCity(lat, lon):
  response = requests.get(os.getenv('API_NINJAS_WORLD_TIME_URL').format(lat, lon), headers={'X-Api-Key': os.getenv('API_NINJAS_API_KEY') })
  return response.json() if response.status_code == requests.codes['ok'] else {}


def getWeatherDataByCity(city):
  response = requests.get(os.getenv('WEATHER_API_URL'), params={
      'key': os.getenv('WEATHER_API_API_KEY'),
      'q': city
    })
  return response.json() if response.status_code == requests.codes['ok'] else {}