import itertools
import math

with open('input.txt') as f:
    lines = f.readlines()

lines = lines[:-1]

for i in range(len(lines)):
    lines[i] = lines[i][:-1]
    lines[i] = list(lines[i])
    for j in range(len(lines[i])):
        lines[i][j] = int(lines[i][j] )
 
# flattening list
flat = list(itertools.chain(*lines)) # can use in built extend function also

n = 13
sublists = [flat[i:i+n] for i in range(len(flat) - (n-1))]

print(max( map(math.prod, sublists)))