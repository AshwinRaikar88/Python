#	Rewrite increment using
#       time_to_int and
#       int_to_time

class Time():
	"""Represents the time of day.
	attributes: hour, minute, second"""
	
def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds
	
def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def add_time(t1, t2):
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

def increment(time, seconds):
    newtime = Time()
    newtime.second = time.second
    newtime.minute = time.minute
    newtime.hour = time.hour
    
	add_seconds = time_to_int(newtime) + seconds
	newtime = int_to_time(add_seconds)
	
    print('Pure function output ')   
    print_time(newtime)
	
def print_time(t):
	print('%.2d:%.2d:%.2d \n'%(t.hour,t.minute,t.second))


time = Time()
time.hour = 11
time.minute = 59
time.second = 30

print('The original Time ')
print_time(time)

increment(time, 180)

print('After executing increment')
print_time(time)
