"""
https://www.hackerrank.com/challenges/mini-max-sum/problem
"""
#!/bin/python3

import sys

def miniMaxSum(arr):
    # Complete this function
    minValue = 10 ** 9
    maxValue = sumValue = 0
    for num in arr:
        minValue = min(minValue, num)
        maxValue = max(maxValue, num)
        sumValue += num
    print(sumValue - maxValue, sumValue - minValue)
            
    

if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)
