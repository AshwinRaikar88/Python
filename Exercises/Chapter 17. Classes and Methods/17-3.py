#   Write a str method for the Point class
#   Create a Point object and print it


class Point:
    """Represents a point in 2-D space."""
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return '(%d,%d)'%(self.x,self.y)

P1 = Point(10,12)
print (P1)
