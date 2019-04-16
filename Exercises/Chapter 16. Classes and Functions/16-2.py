# Write a boolean function called is_after that takes two Time objects,
#	t1 and t2, and returns True if t1 follows t2 chronologically and False otherwise

#	Challenge: don’t use an if statement

#	Status: Compleated!

class Time():
	"""Represents the time of day.
	attributes: hour, minute, second"""
	
	def time_to_int(self):
		minutes = self.hour * 60 + self.minute
		seconds = minutes * 60 + self.second
		return seconds
	
	def is_after(self,other):
		return self.time_to_int() > other.time_to_int()
	
time1 = Time()
time1.hour = 11
time1.minute = 30
time1.second = 00

time2 = Time()
time2.hour = 10
time2.minute = 30
time2.second = 00

print(time1.is_after(time2))
