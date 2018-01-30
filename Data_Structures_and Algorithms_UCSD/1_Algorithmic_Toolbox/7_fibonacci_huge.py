# Uses python3
import sys
import timeit

# SLOW VERSION
# def get_fibonacci_huge_naive(n, m):
#     if n <= 1:
#         return n

#     previous = 0
#     current  = 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current

#     return current % m


# FAST VERSION
def get_fibonacci_huge(n, m):
    assert(1 <= n <= 10**18)
    assert(2 <= m <= 10**5)
    if n <= 1: return n
    a, b = 0, 1
    pattern_list = []
    while True:
        pattern_list += [a]
        i = len(pattern_list)//2
        a, b = b, (a+b)%m
        if (pattern_list[:i] == pattern_list[i:]) or (i > m//2): break
    return pattern_list[n%i]

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))


## Test
# n = int(input('n: '))
# m = int(input('m: '))
# start_time = timeit.default_timer()
# output = get_fibonacci_huge(n, m)
# elapsed_time = timeit.default_timer() - start_time
# print('output: ', output)
# print('elapsed_time: ', elapsed_time)