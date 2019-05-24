import string

fhand = open('D:/Downloads/Documents/mbox-short.txt')

counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.translate(line.maketrans('', '', string.digits))
    line = line.lower()
    words = line.split()
    for word in words:
        for letter in word:
            if letter not in counts:
                counts[letter] = 1
            else:
                counts[letter] += 1

#print(counts)

lst = list()
for key, val in list(counts.items()):
  lst.append((key, val))

lst.sort(reverse=True)

for key, val in lst:
  print('Letter',key,'Count: ',val)
