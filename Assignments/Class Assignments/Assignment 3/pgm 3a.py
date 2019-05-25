'''3. Execute the program which retrieves a particular file on server using URLlib and
Sockets library.'''

# Using URLlib library: 

import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
