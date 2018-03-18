"""
https://www.hackerrank.com/challenges/diagonal-difference/problem
"""
#!/bin/python3

import sys

def diagonalDifference(a):
    # Complete this function
    n = len(a)
    # primary diagonal:
    pd = sum([a[i][i] for i in range(n)])
    # secondary diagonal:
    sd = sum([a[i][n - i - 1] for i in range(n)])
    # difference:
    return abs(pd - sd)

if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
       a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
       a.append(a_t)
    result = diagonalDifference(a)
    print(result)
