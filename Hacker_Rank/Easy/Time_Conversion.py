"""
https://www.hackerrank.com/challenges/time-conversion/problem
"""
#!/bin/python3

import sys

def timeConversion(s):
    # Complete this function
    if s[:2] == '12' and s[-2] == 'A':
        return '00' + s[2:-2]
    if s[:2] != '12' and s[-2] == 'P' :
        return str(12 + int(s[0:2])) + s[2:-2]
    return s[:-2]

s = input().strip()
result = timeConversion(s)
print(result)
