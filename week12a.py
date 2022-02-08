name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fopen = open(name)
lst=list()
for line in fopen:
    if not line.startswith("From "):
        continue
    else:
        line=line.rstrip() #removes spaces
        words=line.split() #divied to words
        time = words[5].split(':') #getting the time
        lst.append(time[0]) #add to the list the forst word on location 1st

o=sorted(lst)
n=dict()
for word in o:
    n[o] = n.get(word,0) + 1
for key,val in n.items():
    print(key,val)


