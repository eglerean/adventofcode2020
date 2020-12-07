import numpy as np

filepath='input.txt'
num=[]
with open(filepath) as fp:
    for line in fp:
        temp=line.replace('F','0').replace('B','1').replace('L','0').replace('R','1');
        num.append(int(temp,2))

num.sort()
print(num)

narr = np.array(num)
ndarr = np.diff(narr) -1;

id=np.where(ndarr==1)
print(id[0])
print(num[id[0][0]])


