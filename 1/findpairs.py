import numpy as np

# list should be a numpy array, no input validation yet
# it now returns all pairs e.g. (x,j) as well as (j,x)
# one could write it that it returns unique pairs

def findpairs(list, N):
    out=np.empty((0,2), int)
    for x in list:
        temp=list+x
        match=np.where(temp == N)
        if len(match[0]) > 0 :
            for m in match[0]:
                out = np.append(out, np.array([[x,list[m]]]), axis=0)
    return out

