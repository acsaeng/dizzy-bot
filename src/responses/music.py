import random
import helpers
import constants

class Music:
  def __init__(self):
    self.playlist = None

    self.__select_playlist()

  def __select_playlist(self):
    self.playlist = random.choice(constants.MUSIC_PLAYLISTS)

  def format_response(self):
    if self.playlist:
      return { 'content': helpers.hyperlink_music_response(random.choice(constants.MUSIC_RESPONSE_SUCCESS), self.playlist), 'embeds': None }
    else:
      return { 'content': constants.MUSIC_RESPONSE_ERROR, 'embeds': None }
