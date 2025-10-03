import random
from datetime import datetime,timedelta
start_date=datetime(2020,1,1)
end_date=datetime(2023,1,1)
delta=end_date-start_date
print(delta)
random_days=random.randint(0,delta.days)
print(random_days)
random_date=start_date + timedelta(days=random_days)
print("random date:",random_date.strftime("%y-%m-%d"))