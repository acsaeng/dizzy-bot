BOT_NAME = 'dizzy'

HELP_KEYWORD = 'help'
HELP_RESPONSE = '''
Hello! My name is Dizzy and I'm you're personal Discord assistant! :wave:
To get started, you can ask me one of the following commands:

  `time`: Get the local time of a specified city :clock3:
    e.g. `Dizzy, what time is it in Toronto?`
  
  `weather`: Get the weather of a specified city :sunny:
    e.g. `Dizzy, what's the weather in Vancouver?`

  `music`: Get some personal music recommendations :musical_note:
    e.g. `Dizzy, recommend some music.`

  `hockey_scores`: Get the current hockey scores from the NHL :hockey:
    e.g. `Dizzy, what are the current hockey scores?`
'''

SORRY_RESPONSE = "Sorry, I couldn't understand your request. Please ask something else or ask me for help to get a list of the available commands. :mag_right:"

TIME_KEYWORDS = ['time']
TIME_RESPONSE_SUCCESS = 'Here is the current time in'
TIME_ICON_URL = 'https://cdn3.emoji.gg/emojis/7611-clock.png'
TIME_RESPONSE_ERROR = 'Sorry, I could not find the time. Please try another city :alarm_clock:'

WEATHER_KEYWORDS = ['weather', 'temperature', 'forecast']
WEATHER_RESPONSE_SUCCESS = 'Here is the current weather forecast in'
WEATHER_RESPONSE_ERROR = 'Sorry, I could not find the weather forecast. Please try another city. :white_sun_cloud:'

MUSIC_KEYWORDS = ['music', 'song', 'spotify']
MUSIC_RESPONSE_SUCCESS = ["Here's a fave playlist of mine! :musical_note:",
                          'Time to party with this playlist! :partying_face:', 
                          "I've really been enjoying this playlist lately :green_heart:"]
MUSIC_PLAYLISTS = [
  'https://open.spotify.com/playlist/37i9dQZEVXbupijRAp0nXw?si=5b3188afbca748f4',
  'https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M?si=e91a8f579a0d43bc',
  'https://open.spotify.com/playlist/37i9dQZF1DX9tPFwDMOaN1?si=add16baccdf04450'
]
MUSIC_RESPONSE_ERROR = "Sorry, I'm really not in the mood right now. Let's do it another time :musical_note:"

HOCKEY_SCORES_KEYWORDS = ['hockey', 'hockey score', 'hockey scores', 'nhl']
HOCKEY_SCORES_RESPONSE_SUCCESS = 'Here are the current hockey scores'
HOCKEY_SCORES_RESPONSE_ERROR = 'Sorry, I could not fetch the hockey scores. Please try again later. :hockey:'
GAME_STATUS = {
 'FINAL': 'FINAL',
 'LIVE': 'LIVE',
 'PREVIEW': 'PREVIEW',
 'POSTPONED': 'POSTPONED',
}
GAME_STATUS_LABEL = {
  'FINAL': 'Final',
  'POSTPONED': 'Postponed',
}
FINAL_SUFFIX = {
  'OVERTIME': ' (OT)',
  'SHOOTOUT': ' (SO)',
}
GAME_TIMEZONE = 'US/Eastern'
GAME_TIMEZONE_SUFFIX = '(ET)'