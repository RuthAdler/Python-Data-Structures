fopen = open("mbox-short.txt")
count=0
mails=list()
for l in fopen:
    lx = l.rstrip()
    if not lx.startswith("From:"):continue
    count=count+1
    word=lx.split()
    mails.append(word[1])
    for x in mails:
        x=x.rstrip()
print(*mails,sep="\n")
print("There were", count, "lines in the file with From as the first word")