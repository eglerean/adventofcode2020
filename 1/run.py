import numpy as np
from findpairs import findpairs
from findtriplets import findtriplets

# Solution for advent of code 2020 #1
# Load a list as a numpy array, call "findpair" to find which pairs have a joint sum of
# 2020 and then multiplies each found pair

# first a test
testlist = np.array([1, 2019, 2, 1, 2018, 4, 5, 6])

matched_pairs = findpairs(testlist,2020)
matched_triplets = findtriplets(testlist,2020)

# test seems fine, now with real data

lista = np.loadtxt('input.txt')
matched_pairs = findpairs(lista,2020)
matched_triplets = findtriplets(lista,2020)

# compute the multiplication and outputs it
for n in matched_pairs:
    print(n[0]*n[1])

for n in matched_triplets:
    print(n[0]*n[1]*n[2])
