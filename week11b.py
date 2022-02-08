name = input("Enter file:")
if len(name) < 1:name = "mbox-short.txt"
fopen= open(name)
di = dict()

for lx in fopen:
    if not lx.startswith("From:"):continue
    lx=lx.rstrip().split()
    for l in lx:
        if not l=="From:":
            di[l]=di.get(l, 0) + 1
max_value=max(di.values())  # maximum value
max_keys = [k for k, v in di.items() if v == max_value] # getting all keys containing the `maximum`
print(*max_keys,max_value)

