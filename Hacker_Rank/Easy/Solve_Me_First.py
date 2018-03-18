"""
Complete the function solveMeFirst to compute the sum of two integers.

Function prototype:

int solveMeFirst(int x, int y);

where,

x is the first integer input.
y is the second integer input
Return values

sum of the above two integers
Sample Input

x = 2
y = 3
Sample Output

5
Explanation

The sum of the two integers  and  is computed as: 2 + 3 = 5
"""
def solveMeFirst(a,b):
    return a + b
  

num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)
