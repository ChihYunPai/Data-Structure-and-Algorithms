# Uses python3
import sys
import timeit

##SLOW VERSION
# def get_fibonacci_last_digit_naive(n):
#     if n <= 1:
#         return n

#     previous = 0
#     current  = 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current

#     return current % 10

## FAST VERSION
# def get_fibonacci_last_digit(n):
#     assert(0 <= n <= 10**7)
#     if n <= 1: return n
#     F_ld = [int(0)]*(n+1) # F_ld: Fibonacci_last_digit
#     F_ld[0] = 0
#     F_ld[1] = 1
#     for i in range(2, n+1):
#         F_ld[i] = (F_ld[i-1] + F_ld[i-2])%10
#     return F_ld[n]

## MEMORY IMPROVED
def get_fibonacci_last_digit(n):
    assert(0 <= n <= 10**7)
    if n <= 1: return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, (a+b)%10
    return b

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))


## Test
# n = int(input())
# start_time = timeit.default_timer()
# print(get_fibonacci_last_digit(n))
# elapsed_time = timeit.default_timer() - start_time
# print('elapsed_time: ', elapsed_time)