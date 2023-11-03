import os
from dotenv import load_dotenv
import discord
import responses

load_dotenv()


def run_discord_bot():
  TOKEN = os.getenv('DISCORD_BOT_TOKEN')

  intents = discord.Intents.default()
  intents.message_content = True
  client = discord.Client(intents=intents)

  @client.event
  async def on_ready():
    print(f'{client.user} is now running!')

  @client.event
  async def on_message(message):
    if message.author != client.user:
      await send_message(message)

  client.run(TOKEN)


def handle_response(message):
  user_message = message.lower()

  if 'dizzy' in user_message:
    if 'hockey scores' in user_message:
      return responses.getHockeyScores()
    if 'play' in user_message and ('song' in user_message or 'music' in user_message):
      return
    elif 'weather' in user_message:
      return responses.getWeatherFromLocation(user_message)
    elif 'time' in user_message:
      return


async def send_message(message):
  try:
    bot_response = handle_response(message.content)
    await message.channel.send(bot_response)
  except Exception as error:
    print('Error:', error)

