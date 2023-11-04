from geotext import GeoText

def getCityFromText(text):
  for word in reversed(text.split()):
    city = GeoText(word.title()).cities
    
    if city:
      return city[0]
  
  return None