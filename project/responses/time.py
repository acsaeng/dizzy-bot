from datetime import date, datetime
import discord
import api
import constants

class Time:
  def __init__(self, city):
    self.city = city
    self.country = None
    self.date = None
    self.time = None

    self.__getLocalTime()
  
  def __getLocalTime(self):
    geocoding_response = api.getGeocodingDataByCity(self.city)

    if geocoding_response:
      self.city = geocoding_response['name']
      self.country = geocoding_response['country']

      world_time_response = api.getWorldTimeDataByLocation(geocoding_response['latitude'], geocoding_response['longitude'])

      if world_time_response:                                     
        # Converting date and time to MM, DD, YYYY and HH:MM formats
        date_list = list(map(int, world_time_response['datetime'].split()[0].split('-')))
        self.date = date(day=date_list[2], month=date_list[1], year=date_list[0]).strftime('%B %#d, %Y')
        self.time = datetime.strptime(world_time_response['datetime'].split()[1], '%H:%M:%S').strftime('%I:%M %p')

  def formatResponse(self):
    if self.city and self.time:
      embed = discord.Embed(title=self.time)
      embed.add_field(name=self.date, value=f'{self.city}, {self.country}')
      embed.set_thumbnail(url=constants.TIME_ICON_URL)
      return { 'content': f'{constants.TIME_RESPONSE_SUCCESS} {self.city}', 'embed': embed }
    else:
      return { 'content': constants.TIME_RESPONSE_ERROR, 'embed': None }
