import os
from dotenv import load_dotenv
import requests

load_dotenv()

class Time:
  def __init__(self, city):
    self.city = city
    self.country = None
    self.datetime = None

    self.__getLocalTime()
  
  def __getLocalTime(self):
    response = requests.get(os.getenv('WEATHER_API_URL'), params={
      'key': os.getenv('WEATHER_API_API_KEY'),
      'q': self.city
    }).json()

    print('response', response)

    self.city = response['location']['name']
    self.country = response['location']['country']
    self.datetime = response['locaiton']['localtime']

  def formatResponse(self):
    if (self.city and self.datetime):
      return f'The time in {self.city} is {self.datetime}'
    else:
      return "Sorry I couldn't find the time. Please try another city."
    

time = Time('Oslo')
