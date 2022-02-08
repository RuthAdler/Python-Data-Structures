name=input("Enter file name ")
if len(name)<1:name="mbox-short.txt"
file_open=open(name)
lst=list()
for line in file_open:
    if not line.startswith("From "):
        continue
    else:
        line.rstrip()
        words=line.split()
        time=words[5].split(':')
        lst.append(time[0])

orgnaized_time=sorted(lst)
di=dict()
for word in orgnaized_time:
    di[word]=di.get(word,0) + 1
for key,val in di.items():
    print(key,val)
