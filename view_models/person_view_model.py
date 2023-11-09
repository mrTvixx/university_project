from models.person import Person
from utils.fake_database import db

person_entity = Person(123456789, 'Физ. лицо', 'секретное слово', '14.05.2019', 1).get_data()
db.write_person(person_entity)

person_individual = Person(987654321, 'Юр. лицо', 'сукрет', '21.10.2022', 2).get_data()
db.write_person(person_individual)
