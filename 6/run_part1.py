import numpy as np

filepath='input.txt'
temprecord=[]
records=[]
with open(filepath) as fp:
    for line in fp:
        line=line.strip()
        if not line:
            records.append(list({i for i in temprecord}))
            temprecord=[]
        temp=list(line)
        temprecord=temprecord + temp


records.append(list({i for i in temprecord}))
cnt=0
for n in records:
    cnt += len(n)

print(cnt)

