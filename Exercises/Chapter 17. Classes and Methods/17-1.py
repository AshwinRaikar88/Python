# Rewrite time_to_int (from Prototyping Versus Planning) as a method

class Time(object):
    """Represents the time of day."""
    
    def time_to_int(self):
      minutes = self.hour * 60 + self.minute
      seconds = minutes * 60 + self.second
      return seconds

    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))


start = Time()
start.hour = 9
start.minute = 45
start.second = 00

start.print_time()
print(start.time_to_int(),'sec')
