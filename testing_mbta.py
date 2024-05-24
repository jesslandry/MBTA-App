
from pymbta3 import Schedules
api_key = '8023186685c54979aaba087928ff2554'

sched = Schedules(api_key)

sc = sched.get(stop='place-mgngl', direction_id=0, min_time='18:00', max_time='19:00')

for data in sc['data']:
    print(data['attributes']['departure_time'])