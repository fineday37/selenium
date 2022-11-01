import datetime

time = (datetime.datetime.now()-datetime.timedelta(days=1)).strftime("%Y-%m-%d")
print(time)

times = str(time)

print(times)
print(type(times))