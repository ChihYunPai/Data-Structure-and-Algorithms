# Uses python3
import sys
import timeit

##SLOW VERSION
# def gcd_naive(a, b):
#     current_gcd = 1
#     for d in range(2, min(a, b) + 1):
#         if a % d == 0 and b % d == 0:
#             if d > current_gcd:
#                 current_gcd = d

#     return current_gcd

def gcd(a, b):
	while b:
		a, b = b, a%b
	return a

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))




## Test
# a = int(input('a: '))
# b = int(input('b: '))
# assert(all([1 <= a, b <= 2*(10**9)]))
# start_time = timeit.default_timer()
# print(gcd(a, b))
# elapsed_time = timeit.default_timer() - start_time
# print('elapsed_time: ', elapsed_time)