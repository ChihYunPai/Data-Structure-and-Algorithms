"""
Given an array of integers, find the sum of its elements.

Function Description

Complete the simpleArraySum function in the editor below. It has the following description:

Parameters	Name	Type	Description
n	Integer	Number of elements in the input array.
ar	Integer Array	Array elements whose sum needs to be computed.
Return	The function must return an integer denoting sum of all array elements.
Raw Input Format

The first line contains an integer, , denoting the size of the array. 
The second line contains  space-separated integers representing the array's elements.

Sample Input 0

6
1 2 3 4 10 11
Sample Output 0

31
Explanation 0

We print the sum of the array's elements: 1+2+3+4+10+11=31
"""
#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(n, ar):
    #
    # Write your code here.
    #
    return sum(ar)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(n, ar)

    f.write(str(result) + '\n')

    f.close()





