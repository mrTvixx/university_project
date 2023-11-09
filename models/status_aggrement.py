from random import randrange

class StatusAggrement:
  def __init__(self, status, id = None):
    self._id = id or randrange(10*10000000)
    self._status = status

  def get_data(self):
    return dict(id = self._id, status = self._status )