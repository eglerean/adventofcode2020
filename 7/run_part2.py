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
            tree[cnt,items[temparr[1]+" "+temparr[2]]]=temparr[0]
        cnt += 1

# test the data structure

out=np.nonzero(tree[items["shiny gold"],:])
for i in out[0]:
    print(keys[i])

print(tree.shape)

# find shiny gold
def getchildren(itemname,itemnum):
    temp=np.nonzero(tree[items[itemname],:])
    children=np.unique(temp[0])
    tempout=itemnum
    print(children)
    if(len(children) > 0):
        for n in children:
            tempout += itemnum*getchildren(keys[n],tree[items[itemname],n])

    return tempout 

#temp=np.nonzero(tree[items["shiny gold"],:]) # all children of shiny gold
#children=np.unique(temp[0]);

out = getchildren("dark violet",1)
print(out) 
out = getchildren("shiny gold",1)
print(out) 
