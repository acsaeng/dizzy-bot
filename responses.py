from geotext import GeoText

def getHockeyScores():
  return

def getWeatherFromLocation(user_message):
  locations = GeoText(user_message)
  return f'Weather in {locations.cities[0]}'