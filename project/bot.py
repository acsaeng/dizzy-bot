import os
from dotenv import load_dotenv
import discord
from responses.weather import Weather
import helpers

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
    user_message = message.lower()

    if 'dizzy' in user_message:
      if 'weather' in user_message:
        city = helpers.getCityFromText(user_message)
        weather = Weather(city)
        return weather.formatResponse()

  async def send_message(self, message):
    try:
      bot_response = self.handle_response(message.content)
      await message.channel.send(bot_response['content'], embed=bot_response['embed'])
    except Exception as error:
      print('Error:', error)