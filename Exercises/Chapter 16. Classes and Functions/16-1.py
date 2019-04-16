class Time():
	"""Represents the time of day.
	attributes: hour, minute, second"""

def print_time(t):
	print('%.2d:%.2d:%.2d'%(t.hour,t.minute,t.second))
	
time = Time()
time.hour = 11
time.minute = 59
time.second = 30

print_time(time)
