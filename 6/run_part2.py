import numpy as np
import string

filepath='input.txt'
temprecord={i for i in list(string.ascii_lowercase)}
records=[]
with open(filepath) as fp:
    for line in fp:
        line=line.strip()
        if not line:
            records.append(len(temprecord))
            temprecord={i for i in list(string.ascii_lowercase)}
            continue
        temp={i for i in list(line)}
        temprecord=temprecord.intersection(temp)

records.append(len(temprecord))
print(records)

cnt=0
for n in records:
    cnt += n

print(cnt)

