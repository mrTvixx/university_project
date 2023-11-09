def format_types(types):
  obj = {}

  for value in types.values():
    obj[value['type']] = value['id']

  return obj

def format_statuses(statuses):
  obj = {}

  for value in statuses.values():
    obj[value['status']] = value['id']

  return obj

def format_person(persons):
  obj = {}

  for value in persons.values():
    obj[value['inn']] = value['id']

  return obj