AGGREMENTS_KEY = 'aggrements'
PERSONS_KEY = 'persons'
STATUSES_KEY = 'statuses'
TYPES_KEY = 'types'

class FakeDatabase:
  def __init__(self):
    self._db = dict()
    self._db[AGGREMENTS_KEY] = dict()
    self._db[PERSONS_KEY] = dict()
    self._db[STATUSES_KEY] = dict()
    self._db[TYPES_KEY] = dict()

  # методы чтения данных
  def read_aggrement(self, id = None):
    data = self._db[AGGREMENTS_KEY]

    if (id):
      return data[id]

    return data

  def read_person(self, id = None):
    data = self._db[PERSONS_KEY]

    if (id):
      return data[id]

    return data

  def read_type(self, id = None):
    data = self._db[TYPES_KEY]

    if (id):
      return data[id]

    return data

  def read_status(self, id = None):
    data = self._db[STATUSES_KEY]

    if (id):
      return data[id]

    return data
  

  # методы удаления
  def delete_aggrement(self, id):
    aggreements_list = self.read_aggrement()
    del aggreements_list[id]
  

  # методы записи данных
  def write_aggrement(self, data):
    aggrements = self.read_aggrement()
    aggrements[data['id']] = data

  def write_person(self, data):
    persons = self.read_person()
    persons[data['id']] = data

  def write_type(self, data):
    types = self.read_type()
    types[data['id']] = data

  def write_status(self, data):
    statuses = self.read_status()
    statuses[data['id']] = data


db = FakeDatabase()
