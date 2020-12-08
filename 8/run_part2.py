import re
import numpy as np
filepath='input.txt'



# load the input and store it as numpy matrix of 0 (free) and 1 (tree)
cnt = 0
values = [];
commands = [];
with open(filepath) as fp:
    for line in fp:
        line = line.strip()
        list1=line.split(' ')
        values.append(int(list1[1]))
        commands.append(list1[0])
        cnt += 1

L=cnt;
accumulator = 0

changethis = -1;
visited_time=np.zeros(L)
while visited_time[-1] == 0:
    changethis += 1
    print(f"iteration {changethis}")
    curr=0
    cnt = 1
    accumulator = 0
    visited=np.zeros(L)
    visited_time=np.zeros(L)
    accumulator_previous = 0
    while np.where(visited==2)[0].size == 0:
        if curr == L:
            print("found it!")
            break
        visited[curr] += 1
        visited_time[curr] = cnt;
        cnt += 1
        command = commands[curr]
        value = values[curr]
        accumulator_previous=accumulator
        if command == "acc": 
            accumulator += value
            curr += 1
            continue
        if command == "jmp":
            if curr == changethis :
                # behaves as a nop
                print(f"changing jmp to nop at line {curr}")
                curr +=1
            else:
                curr += value
            continue
        if command == "nop":
            if curr == changethis:
                # behaves as a jmp
                print(f"changing nop to jmp at line {curr}")
                curr += value
            else:
                curr += 1




print(accumulator)
print(accumulator_previous)
