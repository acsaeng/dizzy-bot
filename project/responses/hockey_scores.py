import discord
from datetime import datetime
from pytz import timezone
import api
import constants

class HockeyScores:
  def __init__(self):
    self.hockey_scores = None

    self.__get_hockey_scores()

  def __get_hockey_scores(self):
    response = api.get_hockey_scores()
    
    if response:
      self.hockey_scores = []

      for game in response['games']:
        hockey_score = {
          'status': game['status'],
          'progress': game.get('progress'),
          'start_time': game['startTime'],
          'score': game['scores']
        }
        self.hockey_scores.append(hockey_score)

  def format_response(self):
    if self.hockey_scores:
      embeds = []

      for hockey_score in self.hockey_scores:
        away_team = list(hockey_score['score'].keys())[0]
        home_team = list(hockey_score['score'].keys())[1]

        embed = discord.Embed()
        embed.add_field(name=f'{away_team}\n{home_team}', value='')
        embed.add_field(name='{}\n{}'.format(hockey_score['score'][away_team], hockey_score['score'][home_team]), value='')

        embed_status_field = {}
        game_status = hockey_score['status']['state']

        if game_status == constants.GAME_STATUS['FINAL']:
          embed_status_field['name'] = constants.GAME_STATUS_LABEL['FINAL']
          embed_status_field['value'] = ''

          if hockey_score['score'].get('overtime'):
            embed_status_field['name'] += constants.FINAL_SUFFIX['OVERTIME']
          elif hockey_score['score'].get('shootout'):
            embed_status_field['name'] += constants.FINAL_SUFFIX['SHOOTOUT']
        
        elif game_status == constants.GAME_STATUS['LIVE']:
          embed_status_field['name'] = hockey_score['status']['progress']['currentPeriodTimeRemaining']['pretty'].title()
          embed_status_field['value'] = hockey_score['status']['progress']['currentPeriodOrdinal']

        elif game_status == constants.GAME_STATUS['PREVIEW']:
          time = datetime.fromisoformat(hockey_score['start_time']).astimezone(timezone(constants.GAME_TIMEZONE)).strftime('%I:%M %p')
          embed_status_field['name'] = f'{time} {constants.GAME_TIMEZONE_SUFFIX}'
          embed_status_field['value'] = ''

        elif game_status == constants.GAME_STATUS['POSTPONED']:
          embed_status_field['name'] = constants.GAME_STATUS_LABEL['POSTPONED']
          embed_status_field['value'] = ''
        
        embed.add_field(name=embed_status_field['name'], value=embed_status_field['value'])
        embeds.append(embed)
      
      return { 'content': constants.HOCKEY_SCORES_RESPONSE_SUCCESS, 'embeds': embeds }
    
    else:
      return { 'content': constants.HOCKEY_SCORES_RESPONSE_ERROR, 'embeds': None }
