# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
	value = 0.
	# Check constraints
	assert(len(weights) == len(values))
	assert(1 <= len(weights) <= 10**3)
	items = []
	for w, v in zip(weights, values):
		assert(0 < w <= 2*(10**6))
		assert(0 < v <= 2*(10**6))
		items.append([w, v, (v/w)])

	items = sorted(items, key=lambda item: item[2], reverse=True)
	for item in items:
		if capacity == 0: break
		if capacity < item[0]:
			value += item[2]*capacity
			break
		else: #gap >= w
			capacity -= item[0]
			value += item[1]
	return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))


# ## Local Test
# capacity = int(input('capacity: '))
# values = list(map(int, input('values: ').split()))
# weights = list(map(int, input('weights: ').split()))
# opt_value = get_optimal_value(capacity, weights, values)
# print("{:.10f}".format(opt_value))
