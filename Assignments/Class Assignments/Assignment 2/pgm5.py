fhand = open('D:/Downloads/Documents/mbox-short.txt')

count = dict()

for line in fhand:
    line = line.rstrip()
    word = line.split()
    if len(word)==0 or len(word)<2 or word[0] != 'From':
        continue
    else:
        if word[1] not in count:
            count[word[1]] = 1
        else:
            count[word[1]] += 1

print(count,'\n')
print('Person with most e-mails: ',max(count))
