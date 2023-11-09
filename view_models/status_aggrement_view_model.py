from models.status_aggrement import StatusAggrement
from utils.fake_database import db

active_status = StatusAggrement('действует', 1).get_data()
db.write_status(active_status)

blocked_status = StatusAggrement('блокирован', 2).get_data()
db.write_status(blocked_status)
