#   Write an init method for the Point class that takes x and y as optional 
#   parameters and assigns them to the corresponding attributes

class Point:
    """Represents a point in 2-D space."""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def print_obj(self):
        print('(%d,%d)'%(self.x,self.y))

P1 = Point()
P1.print_obj()
