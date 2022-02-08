file_name=input('Enter file name:')
if len(file_name)<1: file_name='mbox-short.txt'
file_open=open(file_name)
lst=list()
for line in file_open:
    if not line.startswith('From '):continue
    else: #every line that starts with from
        line.rstrip() #remove space:/n
        words=line.split() #['From', 'ray@media.berkeley.edu', 'Thu', 'Jan', '3', '17:07:00', '2008']
        time=words[5].split(':') #['17', '07', '00']
        hour=time[0]#17
        lst.append(hour) #add the hour to the list
orgenaized_lst=sorted(lst) #orgenize the list from low to high
hour_many_times=dict()
for x in orgenaized_lst:
    hour_many_times[x]=hour_many_times.get(x,0)+1
for h,t in hour_many_times.items():
    print(h,t)


