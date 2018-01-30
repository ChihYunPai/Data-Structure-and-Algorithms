# Uses python3
import sys
import timeit

## SLOW VERSION
# def lcm_naive(a, b):
#     for l in range(1, a*b + 1):
#         if l % a == 0 and l % b == 0:
#             return l

#     return a*b

def gcd(a, b):
	while b:
		a, b = b, a%b
	return a

def lcm(a, b):
	return int(int((a/gcd(a,b)))*b)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

## Test
# a = int(input('a: '))
# b = int(input('b: '))
# start_time = timeit.default_timer()
# print(lcm(a, b))
# elapsed_time = timeit.default_timer() - start_time
# print('elapsed_time: ', elapsed_time)