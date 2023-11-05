import discord
import api
import constants

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
    geocoding_response = api.getGeocodingDataByCity(self.city)

    if geocoding_response:
      self.city = geocoding_response['name']
      self.country = geocoding_response['country']
    
      weather_response = api.getWeatherDataByLocation(geocoding_response['latitude'], geocoding_response['longitude'])

      if weather_response:
        self.country = weather_response['location']['country']  
        self.temperature = round(weather_response['current']['temp_c'])
        self.condition = weather_response['current']['condition']['text']
        self.precipitation = round(weather_response['current']['precip_mm'])
        self.humidity = weather_response['current']['humidity']
        self.wind = round(weather_response['current']['wind_kph'])
        self.icon_url = f'http:{weather_response["current"]["condition"]["icon"]}'

  def formatResponse(self):
    if self.city and self.temperature:
      embed = discord.Embed(title=f'{self.temperature}\xb0C')
      embed.add_field(name=self.condition, value=f'{self.city}, {self.country}', inline=False)
      embed.add_field(name="Precipitation", value=f'{self.precipitation} mm')
      embed.add_field(name="Humidity", value=f'{self.humidity}%')
      embed.add_field(name="Wind", value=f'{self.wind} km/h')
      embed.set_thumbnail(url=self.icon_url)
      return { 'content': f'{constants.WEATHER_RESPONSE_SUCCESS} {self.city}', 'embed': embed }
    
    else:
      return { 'content': constants.WEATHER_RESPONSE_ERROR, 'embed': None }