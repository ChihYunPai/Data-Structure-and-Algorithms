"""
Traveling Salesman Problem,
Implementation of Held–Karp algorithm,
https://en.wikipedia.org/wiki/Held%E2%80%93Karp_algorithm#Graph_model
"""
from collections import defaultdict
from itertools import combinations

d = [[0,2,9,10], [1,0,6,4], [15,7,0,8], [6,3,12,0]] # d[x][y]: given cost from y to x

def TSP(d, n):
	total_set = tuple(range(1, n))
	c = defaultdict(dict)
	for k in range(1, n):
		c[tuple([k])][k] = d[0][k]
	

	for s in range(2, n):
		for comb in list(combinations(total_set, s)):
			for k in comb:
				sub_set = tuple(set(comb) - set([k]))
				c[comb][k] = min([(c[sub_set][m] + d[m][k]) for m in sub_set])
	return min([c[total_set][k] + d[k][0] for k in range(1, n)])

print('TSP result: ', TSP(d, 4))