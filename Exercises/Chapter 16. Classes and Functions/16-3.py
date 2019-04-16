# Write a correct version of increment that doesn’t contain any loops.

class Time():
	"""Represents the time of day.
	attributes: hour, minute, second"""

def increment(time, seconds):
    time.second += seconds

    while time.second >= 60:
        time.second -= 60
        time.minute += 1

    while time.minute >= 60:
        time.minute -= 60
        time.hour += 1
        
def print_time(t):
	print('%.2d:%.2d:%.2d'%(t.hour,t.minute,t.second))


time = Time()
time.hour = 11
time.minute = 59
time.second = 30

increment(time, 180)
print_time(time)
