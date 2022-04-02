name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

time=list()
hrs= list()

for line in handle:
    if not line.startswith('From '):
        continue
    collection = line.split()
    time.append(collection[5])
for word in time:
    seperate = word.split(':')
    hrs.append(seperate[0])
    #print(hrs)
        
    
hrsdict = dict()

for words in hrs:
    hrsdict[words] = hrsdict.get(words,0) + 1

    

for x,y in sorted(hrsdict.items()):
    print(x,y)
