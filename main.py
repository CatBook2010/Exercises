from datetime import datetime as dt
from datetime import timedelta



sec = 55550505
td = timedelta(seconds = sec)
some_dt = dt(1, 1, 1) + td

print(some_dt)

hh = some_dt.time().hour
mm = some_dt.time().minute
ss = some_dt.time().second

print(hh, mm, ss)