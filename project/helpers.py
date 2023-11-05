from geotext import GeoText

def getCityFromText(text):
  cities = GeoText(text).cities
  return cities[0] if cities else None