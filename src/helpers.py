from geotext import GeoText
import constants

def get_city_from_text(text):
  cities = GeoText(text).cities
  return cities[0] if cities else None


def hyperlink_music_response(response, playlist_link):
  return response.replace('playlist', f'[playlist]({playlist_link})')