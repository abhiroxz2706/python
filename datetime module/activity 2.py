import pytz
import datetime
#indian time
tz=pytz.timezone("Asia/Kolkata")
datetime_india=datetime.datetime.now(tz)
print("india time:",datetime_india.strftime("%H:%M:%S"))