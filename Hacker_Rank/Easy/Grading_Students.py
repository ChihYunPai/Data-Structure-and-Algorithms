"""
https://www.hackerrank.com/challenges/grading/problem
"""
#!/bin/python3

import sys

def solve(grades):
    # Complete this function
    for i, x in enumerate(grades):
        if x >= 38 and (5 - x%5) < 3:
            grades[i] = x + (5 - x%5)
    return grades

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))


