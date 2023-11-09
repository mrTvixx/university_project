from models.type_aggrement import TypeAggrement
from utils.fake_database import db

diler_type = TypeAggrement('дилерский', 1).get_data()
db.write_type(diler_type)

broker_type = TypeAggrement('брокерский', 2).get_data()
db.write_type(broker_type)

management_type = TypeAggrement('управления', 3).get_data()
db.write_type(management_type)