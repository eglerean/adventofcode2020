import numpy as np
import trees_library as tl

jump=np.array([1,3])

out = tl.get_trees(jump)

print(out)

print('---')
# part 2

jumps = np.array([
    [1,1],
    [1,3],
    [1,5],
    [1,7],
    [2,1]
    ])

cnt = 0;
values = np.array([]);
for row in jumps:
    print(row)
    out=tl.get_trees(row)
    print(out)
    values=np.append(values,out)

print('Final result is')
print(np.prod(values))
