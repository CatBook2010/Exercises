from time_file import Time
from datetime import datetime as dt

time = Time()

time.setTime(55550505)
print(f"Here is your time: {time.getHour():.0f}:{time.getMinute():.0f}:{time.getSecond():.0f}")