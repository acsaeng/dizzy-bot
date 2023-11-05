from geotext import GeoText
import constants

def getCityFromText(text):
  cities = GeoText(text).cities
  return cities[0] if cities else None


def hyperlinkMusicResponse(response, playlist_link):
  return response.replace('playlist', f'[playlist]({playlist_link})')