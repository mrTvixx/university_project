from random import randrange

class TypeAggrement:
  def __init__(self, type, id = None):
    self._id = id or randrange(10*10000000)
    self._type = type

  def get_data(self):
    return dict(id = self._id, type = self._type )