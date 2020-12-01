import numpy as np

# list should be a numpy array, no input validation yet
# ugly solution with nested for loops :)

def findtriplets(list, N):
    out=np.empty((0,3), int)
    for x in range(0,list.size):
        for y in range(x+1,list.size):
            for z in range(y+1,list.size):
                temp=list[x]+list[y]+list[z]
                if temp == N :
                    out = np.append(out, np.array([[list[x],list[y],list[z]]]), axis=0)
    return out

