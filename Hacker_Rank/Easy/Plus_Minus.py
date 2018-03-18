"""
https://www.hackerrank.com/challenges/plus-minus/problem
"""
#!/bin/python3

import sys

def plusMinus(arr):
    # Complete this function
    pos = neg = zero = 0
    n = len(arr)
    for a in arr:
        if a > 0:
            pos += 1
        elif a < 0:
            neg += 1
        else:
            zero += 1
    print(format(pos/n, '5f'))
    print(format(neg/n, '5f'))
    print(format(zero/n, '5f'))
            

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    plusMinus(arr)
