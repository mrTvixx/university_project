from models.agreement import Agreement
from utils.fake_database import db

aggrement_1 = Agreement(1, 1, 1, 123, '20.02.2022', '20.02.2023', 123).get_data()
db.write_aggrement(aggrement_1)

aggrement_2 = Agreement(2, 2, 2, 321, '25.03.2021', '25.06.2024', 321).get_data()
db.write_aggrement(aggrement_2)