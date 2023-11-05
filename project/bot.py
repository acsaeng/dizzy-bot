import os
from dotenv import load_dotenv
import discord
from responses.time import Time
from responses.weather import Weather
import helpers
import constants

load_dotenv()

class DizzyBot:
  def __init__(self):
    self.token = os.getenv('DISCORD_BOT_TOKEN')

  def run_bot(self):
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
      print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
      if message.author != client.user:
        await self.send_message(message)

    client.run(self.token)

  def handle_response(self, message):
    user_message_lower = message.lower()

    if constants.BOT_NAME in user_message_lower:
      if any(word in user_message_lower for word in constants.TIME_KEYWORDS):
        city = helpers.getCityFromText(message)
        time = Time(city)
        return time.formatResponse()
      elif any(word in user_message_lower for word in constants.WEATHER_KEYWORDS):
        city = helpers.getCityFromText(message)
        weather = Weather(city)
        return weather.formatResponse()

  async def send_message(self, message):
    # try:
      bot_response = self.handle_response(message.content)
      await message.channel.send(bot_response['content'], embed=bot_response['embed'])
    # except Exception as error:
      # print('Error:', error)