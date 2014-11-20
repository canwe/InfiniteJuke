Class Measure:
  'Each section of the song'
  
  # Create a list of connections
  connections = []
  
  def __init__(self, audio, pos):
    # set the objects audio and position
    self.audio = audio
    self.pos = pos
