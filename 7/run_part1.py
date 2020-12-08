import re
import numpy as np
filepath='input.txt'



# load the input and store it as numpy matrix of 0 (free) and 1 (tree)
cnt = 0
items={};
keys= [];
#make list
with open(filepath) as fp:
    for line in fp:
        line = line.strip()
        regex = r'^.*bags contain'
        list1=re.findall(regex,line)
        item=list1[0].replace(" bags contain","")
        items[item]=cnt
        keys.append(item)
        cnt += 1

tree=np.zeros((cnt,cnt))
cnt=0
with open(filepath) as fp:
    for line in fp:
        line = line.strip()
        regex = r'bags contain.*'
        list1=re.findall(regex,line)
        tempitems=list1[0].replace("bags contain ",'').replace(", ",",").split(',')
        for i in tempitems:
            temparr=i.split(" ")
            if temparr[0] == "no":
                break
            tree[cnt,items[temparr[1]+" "+temparr[2]]]=1
        cnt += 1

# test the data structure

out=np.nonzero(tree[items["shiny gold"],:])
for i in out[0]:
    print(keys[i])

# find shiny gold
temp=np.nonzero(tree[:,items["shiny gold"]]) # all parents of shiny gold
parents=np.unique(temp[0]);
cnt = 0
visited=np.zeros(len(items))
while len(parents>0):
    print(parents)
    curr=parents[0]
    visited[curr]=1
    parents=parents[1:]
    temp=np.nonzero(tree[:,curr]);
    moreparents=temp[0]
    #parents=np.unique(np.append(parents,moreparents))
    parents=np.append(parents,moreparents)
    cnt += 1

print(cnt)
print(np.sum(visited))


        
