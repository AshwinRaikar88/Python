import re

fhand = open('mbox-short.txt')

count = dict()

for line in fhand:
  line = line.rstrip()
  if re.search('^From .* [0-9][0-9]:'.line):
      x = re.findall('^From .* ([0-9][0-9]):', line)
      
  if len(x) > 0:
    print(x)
    
    for no in x:
      if no not in count:
        count[line] = 1
       else:
        count[line] += 1

