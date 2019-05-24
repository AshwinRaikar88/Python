import re

fhand = open('D:/Downloads/Documents/mbox-short.txt')

count=0
for line in fhand:
    line = line.rstrip()
    if re.search('^From:.+@', line):
        x=re.findall('^From:(.*@.*)', line)
        print(x)
        count += 1
print("Count: ",count)
