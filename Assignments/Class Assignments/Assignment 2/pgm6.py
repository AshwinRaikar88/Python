import re

fhand = open('D:/Downloads/Documents/mbox.txt')

count = dict()

for line in fhand:
  line = line.rstrip()
  if re.search('^From .* [0-9][0-9]:', line):
      x = re.findall('^From .* ([0-9][0-9]):', line)
      
  if len(x) > 0:
#    print(x)   
    for no in x:
        if no not in count:
            count[no] = 1
        else:
            count[no] += 1
            
lst = list()
for key, val in list(count.items()):
  lst.append((key, val))

lst.sort()

for key, val in lst:
  print('Hour',key,'Count: ',val)
