# Uses python3
import sys

def optimal_summands(n):
    summands = []
    for i in range(1, n+1):
        n -= i
        if n <= i:
            summands.append(n + i)
            break
        else:
        	summands.append(i)
        	if n == 0: break
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')

# Local Test
# n = int(input('n: '))
# summands=optimal_summands(n)
# print(sum(summands), summands)
