# Uses python3
import sys

def get_change(m):
    #write your code here
    assert(1 <= m <= 10**3)
    count = 0
    denominations = [10, 5, 1]
    for denom in denominations:
    	if m >= denom:
    		count += m//denom
    		m %= denom
    	if m == 0: break
    return count

if __name__ == '__main__':
	m = int(sys.stdin.read())
	print(get_change(m))


# m = int(input('m: '))
# print(get_change(m))