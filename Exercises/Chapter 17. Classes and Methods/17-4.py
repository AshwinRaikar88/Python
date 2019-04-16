#   Write an add method for the Point class


class Point:
    """Represents a point in 2-D space."""
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return '(%d,%d)'%(self.x,self.y)
    
    def __add__(self, other):
        return (self.x + other.x,self.y + other.y)

P1 = Point(10,12)
P2 = Point(22,66)

print (P1 + P2)
