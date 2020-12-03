# Advent of Code 2020 part 3
import numpy as np

def get_trees(jump):
    filepath='input.txt'

    # load the input and store it as numpy matrix of 0 (free) and 1 (tree)
    cnt = 0
    with open(filepath) as fp:
        for line in fp:
            line = line.strip()
            listarr=list(map(int,line.replace('.','0').replace('#','1'))) # using map to convert to int
            arr = np.array(listarr)
            if cnt == 0:
                out = np.array(arr);
            else:
                out = np.vstack((out,arr))
            cnt += 1


    # get size of input, num of cols is used as "module" and num of rows to stop searching
    sh=out.shape;
    Nrow=sh[0];
    Ncol=sh[1];

    # find all the coordinates that have jump=[1, 3]
    path=np.array([0,0])
    s = np.array([0,0])
    while s[0] < Nrow-1:
        temp=s+jump
        temp[1] = np.mod(temp[1],Ncol)
        path=np.vstack((path,temp));
        s = temp;

    return np.sum(out[path[:,0],path[:,1]])


