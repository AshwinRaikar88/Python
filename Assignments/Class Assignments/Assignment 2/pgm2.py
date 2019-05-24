import re

fhand = open('mbox-short.txt')

for line in fhand:
    print(line)
    line = line.rstrip()
    if re.search('^From:.+@', line):
        x=re.findall('^From:(.+@)', line)
        print(x)
