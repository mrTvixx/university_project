from random import randrange

from utils.fake_database import db

class Agreement:
  def __init__(self, person_id, type_id, status_id, number, data_open, data_clouse, id = None):
    self._id = id or randrange(10*10000000)
    self._person_id = person_id
    self._type_id = type_id
    self._status_id = status_id
    self._number = number
    self._data_open = data_open
    self._data_clouse = data_clouse

  def get_data(self):
    return dict(
      id = self._id,
      person = db.read_person(self._person_id)['inn'],
      type = db.read_type(self._type_id)['type'],
      status = db.read_status(self._status_id)['status'],
      number = self._number,
      data_open = self._data_open,
      data_clouse = self._data_clouse,
    )