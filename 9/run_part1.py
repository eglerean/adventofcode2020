import re
import numpy as np
filepath='input.txt'



# load the input and store it as numpy matrix of 0 (free) and 1 (tree)
cnt = 0
N = 25
values = [];
with open(filepath) as fp:
    for line in fp:
        line = line.strip()
        values.append(int(line))
        if cnt >= N:
            tempset=set();
            for x1 in range(N):
                for x2 in range(x1+1,N,1):
                    tempset.add(values[cnt-x1-1]+values[cnt-x2-1])

            if values[cnt] in tempset:
                print(f"{cnt} is valid")
            else:
                print(f"values[{cnt}] is {values[cnt]}")
                print(tempset)
                break

        cnt += 1

