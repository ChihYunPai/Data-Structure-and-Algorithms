#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    numApple = 0
    for appleDistance in apples:
        if s <= (a + appleDistance) <= t:
            numApple += 1;
    print(numApple)
    
    numOrange = 0
    for orangeDistance in oranges:
        if s <= (b + orangeDistance) <= t:
            numOrange += 1
    print(numOrange)
    
if __name__ == '__main__':
    st = input().split()
    s = int(st[0])
    t = int(st[1])
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    countApplesAndOranges(s, t, a, b, apples, oranges)