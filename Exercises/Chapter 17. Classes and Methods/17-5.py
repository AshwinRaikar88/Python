#	Write an add method for Points that works with either a Point object or a tuple:
 
#		If the second operand is a Point, the method should return a new Point 
#		whose x coordinate is the sum of the x coordinates of the operands, and likewise for the y coordinates.

#		If the second operand is a tuple, the method should add the first element of the tuple to the x
#		coordinate and the second element to the y coordinate, and return a new Point with the result


class Point:
    """Represents a point in 2-D space."""
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return '(%d,%d)'%(self.x,self.y)
    
    def __add__(self, other):
        if isinstance(other, Point):
            return self.obj_add(other) 
        else:
            return self.tup_add(other)
       
    def obj_add(self, other):
        new_point = Point()
        new_point.x = self.x + other.x 
        new_point.y = self.y + other.y
        return new_point
		
    def tup_add(self, tupl):
        new_point= Point()
        new_point.x = self.x + tupl[0]
        new_point.y = self.y + tupl[1]
        return new_point
    
#objects P1 & P2
P1 = Point(10,12)
P2 = Point(22,66)
#tuple t1
t1 = (10,12)
#New points are returned
P3 = P1 + P2
print('New Point P3:',P3)
P4 = P3 + t1
print('New Point P4:',P4)
#Points P1 & P2 are not modified
print ('Point P1:',P1)
print ('Point P2:',P2)
