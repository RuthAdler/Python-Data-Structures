fname = input('Enter the file name: ')
fhand = open(fname)
fread=fhand.read()
for lx in fread:
     line = lx.rstrip()
print(fread.upper())
