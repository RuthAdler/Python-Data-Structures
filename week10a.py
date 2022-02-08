fname = input("Enter file name: ")
fopen = open(fname)
lst = list()
for l in fopen:
    lx=l.rstrip().split()
    for word in lx:
        if not word in lst:
            lst.append(word)

print(sorted(lst))

