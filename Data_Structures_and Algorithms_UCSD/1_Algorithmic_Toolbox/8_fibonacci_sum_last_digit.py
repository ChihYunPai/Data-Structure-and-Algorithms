# Uses python3
import sys
import timeit

## SLOW VERSION
# def fibonacci_sum_naive(n):
#     if n <= 1:
#         return n

#     previous = 0
#     current  = 1
#     sum      = 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current
#         sum += current

#     return sum % 10

## FAST VERSION
def fibonacci_sum(n):
    assert(0 <= n <= 10**18)
    if n <= 1: return n
    a, b = 0, 1
    pattern_list = []
    while True:
        pattern_list += [a]
        i = len(pattern_list)//2
        a, b = b, (a+b)%10
        if (pattern_list[:i] == pattern_list[i:]): break
    return (sum(pattern_list[:i])*(n//i) + sum(pattern_list[:((n+1)%i)]))%10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum(n))


## Test
# n = int(input('n: '))
# start_time = timeit.default_timer()
# output = fibonacci_sum(n)
# elapsed_time = timeit.default_timer() - start_time
# print('output: ', output)
# print('elapsed_time: ', elapsed_time)