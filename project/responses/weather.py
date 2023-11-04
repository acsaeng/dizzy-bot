import os
from dotenv import load_dotenv
import requests
import discord

load_dotenv()

class Weather:
  def __init__(self, city):
    self.city = city
    self.country = None
    self.temperature = None
    self.precipitation = None
    self.humidity = None
    self.wind = None
    self.condition = None
    self.icon_url = None

    self.__getLocalWeatherData()
  
  def __getLocalWeatherData(self):
    response = requests.get(os.getenv('WEATHER_API_URL'), params={
      'key': os.getenv('WEATHER_API_API_KEY'),
      'q': self.city
    })

    if response.status_code == 200:
      response = response.json()
      self.city = response['location']['name']
      self.country = response['location']['country']
      self.temperature = round(response['current']['temp_c'])
      self.condition = response['current']['condition']['text']
      self.precipitation = round(response['current']['precip_mm'])
      self.humidity = response['current']['humidity']
      self.wind = round(response['current']['wind_kph'])
      self.icon_url = f'http:{response["current"]["condition"]["icon"]}'

  def formatResponse(self):
    if self.city and self.temperature:
      embed = discord.Embed(title=f'{self.temperature}\xb0C')
      embed.add_field(name=self.condition, value=f'{self.city}, {self.country}', inline=False)
      embed.add_field(name="Precipitation", value=f'{self.precipitation} mm')
      embed.add_field(name="Humidity", value=f'{self.humidity}%')
      embed.add_field(name="Wind", value=f'{self.wind} km/h')
      embed.set_thumbnail(url=self.icon_url)
      return { 'content': f'Here is the current weather forecast for {self.city}', 'embed': embed }
    
    else:
      return 'Sorry, I could not find the weather forecast :( \nPlease try another city...'