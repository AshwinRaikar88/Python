#Assignment Program 4

fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File',fname,'not found')
    exit()
    
for line in fhand:
    Uppercase=line.upper()
    print(Uppercase)
