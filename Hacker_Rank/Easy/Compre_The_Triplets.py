"""
https://www.hackerrank.com/challenges/compare-the-triplets/problem
"""
#!/bin/python3

import os
import sys

#
# Complete the solve function below.
#
def cmp(a, b):
    if a > b:
        return 1
    elif a < 1:
        return -1
    else:
        return 0
    
def solve(a0, a1, a2, b0, b1, b2):
    #
    # Write your code here.
    #
    alice, bob = 0, 0
    for a, b in zip([a0, a1, a2], [b0, b1, b2]):
        if a > b:
            alice += 1
        elif a < b:
            bob += 1
        else:
            pass
    return alice, bob

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    a0A1A2 = input().split()

    a0 = int(a0A1A2[0])

    a1 = int(a0A1A2[1])

    a2 = int(a0A1A2[2])

    b0B1B2 = input().split()

    b0 = int(b0B1B2[0])

    b1 = int(b0B1B2[1])

    b2 = int(b0B1B2[2])

    result = solve(a0, a1, a2, b0, b1, b2)

    f.write(' '.join(map(str, result)))
    f.write('\n')

    f.close()
