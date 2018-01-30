# Uses python3
import sys
import timeit

## SLOW VERSION
# def fibonacci_partial_sum_naive(from_, to):
#     sum = 0

#     current = 0
#     next  = 1

#     for i in range(to + 1):
#         if i >= from_:
#             sum += current

#         current, next = next, current + next

#     return sum % 10

## FAST VERSION
def fibonacci_partial_sum(m, n):
    assert(0 <= n <= 10**18)
    assert(0 <= m <= n)
    if n <= 1: return n
    a, b = 0, 1
    pattern_list = []
    while True:
        pattern_list += [a]
        i = len(pattern_list)//2
        a, b = b, (a+b)%10
        if pattern_list[:i] == pattern_list[i:]: break
    return (sum(pattern_list[:i])*(n//i) + sum(pattern_list[:(n+1)%i]) - sum(pattern_list[:i])*((m-1)//i) - sum(pattern_list[:m%i]))%10

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))

## Test
# m = int(input('m: '))
# n = int(input('n: '))
# start_time = timeit.default_timer()
# output = fibonacci_partial_sum(m, n)
# elapsed_time = timeit.default_timer() - start_time
# print('output: ', output)
# print('elapsed_time: ', elapsed_time)