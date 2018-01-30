# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

## SLOW VERSION
# result = 0
# for i in range(0, n):
#     for j in range(i+1, n):
#         if a[i]*a[j] > result:
#             result = a[i]*a[j]

first = max(a[0], a[1])
second = min(a[0], a[1])
for i in range(2, n):
	if a[i] > second:
		second = a[i]
	if second > first:
		first, second = second, first
result = first*second
print(result)
