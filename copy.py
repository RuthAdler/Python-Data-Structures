fname = input("Enter the file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fhand = open(fname)
lst = list()
for line in fhand:
    if not line.startswith('From '):
        continue
    else:
        line.rstrip() #removes white space
        words = line.split() #dived to words
        time = words[5].split(':') #takes the 5th word-the hour, and divid it by :
        lst.append(time[0]) #adds the first variable (at location 0) to the list
a = sorted(lst) #sort the list from small to large
counts = dict() #creats a dictinary
for word in a: #for every word in the list
    counts[word] = counts.get(word,0) + 1 #if the word is not in the list, add it, if its alredy there, add 1 to counts
for key,val in counts.items(): #for every tuple in the count dic
    print(key,val)