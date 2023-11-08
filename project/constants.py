BOT_NAME = 'dizzy'

TIME_KEYWORDS = ['time']
TIME_RESPONSE_SUCCESS = 'Here is the current time in'
TIME_ICON_URL = 'https://cdn3.emoji.gg/emojis/7611-clock.png'
TIME_RESPONSE_ERROR = 'Sorry, I could not find the time :pensive:\nPlease try another city :alarm_clock:'

WEATHER_KEYWORDS = ['weather']
WEATHER_RESPONSE_SUCCESS = 'Here is the current weather forecast in'
WEATHER_RESPONSE_ERROR = 'Sorry, I could not find the weather forecast :cloud_rain:\nPlease try another city :map:'

MUSIC_KEYWORDS = ['music', 'song', 'spotify']
MUSIC_RESPONSE_SUCCESS = ["Here's a fave playlist of mine! :musical_note:",
                          'Time to party with this playlist! :partying_face:', 
                          "I've really been enjoying this playlist lately :green_heart:"]
MUSIC_PLAYLISTS = [
  'https://open.spotify.com/playlist/37i9dQZEVXbupijRAp0nXw?si=5b3188afbca748f4',
  'https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M?si=e91a8f579a0d43bc',
  'https://open.spotify.com/playlist/37i9dQZF1DX9tPFwDMOaN1?si=add16baccdf04450'
]
MUSIC_RESPONSE_ERROR = "Sorry, I'm really not in the mood right now :sweat: \nLet's do it another time :musical_note:"

HOCKEY_SCORES_KEYWORDS = ['hockey', 'hockey score', 'hockey scores', 'nhl']
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