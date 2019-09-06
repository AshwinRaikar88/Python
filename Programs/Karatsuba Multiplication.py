import math
import string

def karatsuba(x,y):

    if x < 10 or y < 10:
        print('NOT KSuba')
        print(x*y)

    else:
        mi = min( len( str(x) ), len( str(y) ) )
        m = mi-1
        x1 =str(x)
        y1 =str(y)

        a = x1[0:-m]
        b = x1[-m:] 
        c = y1[0:-m]
        d = y1[-m:]

        x1 = int(a)
        x0 = int(b)
        y1 = int(c)
        y0 = int(d)

        z2= x1 * y1
        z0= x0 * y0 
        z1= ( x1 + x0 ) * ( y1 + y0 ) - z2 - z0

        result = z2 * (10**m)**2 + z1 * 10**m + z0
        print(result)

karatsuba(12345,67890)
