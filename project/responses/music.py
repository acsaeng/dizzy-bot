import random
import helpers
import constants

class Music:
  def __init__(self):
    self.playlist = None

    self.__selectPlaylist()

  def __selectPlaylist(self):
    self.playlist = random.choice(constants.MUSIC_PLAYLISTS)

  def formatResponse(self):
    if self.playlist:
      return { 'content': helpers.hyperlinkMusicResponse(random.choice(constants.MUSIC_RESPONSE_SUCCESS), self.playlist), 'embed': None }
    else:
      return { 'content': constants.MUSIC_RESPONSE_ERROR, 'embed': None }
