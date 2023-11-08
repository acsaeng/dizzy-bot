import os
from dotenv import load_dotenv
import discord
from responses.time import Time
from responses.weather import Weather
from responses.music import Music
from responses.hockey_scores import HockeyScores
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

    # Add help message
    if constants.BOT_NAME in user_message_lower:
      if any(word in user_message_lower for word in constants.TIME_KEYWORDS):
        city = helpers.get_city_from_text(message)
        time = Time(city)
        return time.format_response()
      elif any(word in user_message_lower for word in constants.WEATHER_KEYWORDS):
        city = helpers.get_city_from_text(message)
        weather = Weather(city)
        return weather.format_response()
      elif any(word in user_message_lower for word in constants.MUSIC_KEYWORDS):
        music = Music()
        return music.format_response()
      elif any(word in user_message_lower for word in constants.HOCKEY_SCORES_KEYWORDS):
        hockey_scores = HockeyScores()
        return hockey_scores.format_response()
      else:
        # Sorry message
        return {}
    
    return None

  async def send_message(self, message):
    try:
      bot_response = self.handle_response(message.content)

      if bot_response:
        await message.channel.send(bot_response['content'], embeds=bot_response['embeds'])
    except Exception as error:
      print('Error:', error)