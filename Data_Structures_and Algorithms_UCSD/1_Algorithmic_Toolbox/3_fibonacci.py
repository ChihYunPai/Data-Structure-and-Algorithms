# Uses python3
import timeit

## SLOW VERSION:
# def calc_fib(n):
#     if (n <= 1):
#         return n
#     return calc_fib(n - 1) + calc_fib(n - 2)

## FAST VERSION:
# def calc_fib(n):
# 	assert(0 <= n <= 45) # constraints
# 	if n <= 1: return n
# 	F = [int(0)]*(n+1)
# 	F[0] = 0
# 	F[1] = 1
# 	for i in range(2, n+1):
# 		F[i] = F[i-1] + F[i-2]
# 	return F[n]

## MEMORY IMPROVED:
def calc_fib(N):
	assert(0 <= n <= 45) #constraints
	if n <= 1 : return n
	a, b = 0, 1
	for _ in range(2, n+1):
		a, b = b, (a+b)
	return b


n = int(input())
# start_time = timeit.default_timer()
print(calc_fib(n))
# elapsed_time = timeit.default_timer() - start_time
# print('elapsed_time: ', elapsed_time)
