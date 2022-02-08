fname = input('Enter the file name: ')
fhand = open(fname)
count=0
countline=0
for lx in fhand:
     if lx.startswith("X-DSPAM-Confidence: "):
          ly=lx.rstrip()
          countline = countline + 1
          a = len(ly)
          b = a-6
          count=count+float(ly[b:a])
print("Average spam confidence:", count/countline)

