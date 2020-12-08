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
visited=np.zeros(L)
visited_time=np.zeros(L)
accumulator = 0

curr=0
cnt = 1
while np.where(visited==2)[0].size == 0:
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
        curr += value
        continue
    if command == "nop":
        curr += 1


print(accumulator)
print(accumulator_previous)
print(visited_time)
