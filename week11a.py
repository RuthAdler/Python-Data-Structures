name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fopen= open(name)
counts = dict()
mails=list()
for lx in fopen:
    if not lx.startswith("From:"):continue
    word = lx.split()
    mails.append(word[1])

for mail in mails:
    counts[mails] = counts.get(mail, 0) + 1

max_value=max(counts.values())  # maximum value
max_keys = [k for k, v in counts.items() if v == max_value] # getting all keys containing the `maximum`
print(max_keys,max_value)





