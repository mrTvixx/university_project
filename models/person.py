from random import randrange

class Person:
  def __init__(self, inn, type, shifer, data, id = None):
    self._id = id or randrange(10*10000000)
    self._inn = inn
    self._type = type
    self._shifer = shifer
    self._data = data

  def get_data(self):
    return dict(id = self._id, inn = self._inn, type = self._type, shifer = self._shifer, data = self._data )