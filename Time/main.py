from time_file import Time
from datetime import datetime as dt

now = dt.now()

current_time = now.strftime("%H %M %S")
hour, minute, second = map(int, current_time.split(" "))

time = Time(hour, minute, second)

time.setTime(55550505)
print(f"Here is your time: {time.getHour():.0f}:{time.getMinute():.0f}:{time.getSecond():.0f}")