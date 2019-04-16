#	Write a “pure” version of increment that creates and returns a new
#	Time object rather than modifying the parameter.


class Time():
	"""Represents the time of day.
	attributes: hour, minute, second"""

def increment(time, seconds):
    newtime = Time()
	
    newtime.second = time.second
    newtime.minute = time.minute
    newtime.hour = time.hour
    
    newtime.second += seconds

    while newtime.second >= 60:
        newtime.second -= 60
        newtime.minute += 1

    while newtime.minute >= 60:
        newtime.minute -= 60
        newtime.hour += 1
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
