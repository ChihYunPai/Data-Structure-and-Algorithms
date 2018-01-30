#Uses python3
import sys

def isGreaterOrEqual(digit, maxDigit):
	diff = len(str(digit)) - len(str(maxDigit))


	if diff < 0:
		diff = abs(diff)
		newDigit = digit*(10**diff) + int(str(digit%10)*diff)
		return newDigit >= maxDigit
	elif diff > 0:
		newMaxDigit = maxDigit*(10**diff) + int(str(maxDigit%10)*diff)
		return digit >= newMaxDigit
	else:
		return digit >= maxDigit

def largest_number(a):
	#constraints
	assert(1 <= len(a) <= 100)
	assert(1 <= int(min(a)))
	assert(int(max(a)) <= 10**3)
	#write your code here
	# a = list(map(int, a))
	# res = ''
	# value_list = []
	# numOfdigits_Max = len(str(max(a)))
	# for num in a:
	# 	numOfdigits = len(str(num))
	# 	diff = numOfdigits_Max - numOfdigits
	# 	if diff > 0:
	# 		value_list.append([num, num*(10**diff) + int(str(num%10)*diff)])
	# 	else:
	# 		value_list.append([num, num])
	# for item in sorted(value_list, key=lambda x: x[1], reverse=True):
	# 	res += str(item[0])
	# return res
	a = list(map(int, a))
	res = ''
	while(len(a)!=0):
		maxDigit = 0
		for digit in a:
			if isGreaterOrEqual(digit, maxDigit):
				maxDigit = digit
		res += str(maxDigit)
		a.remove(maxDigit)
	return res

if __name__ == '__main__':
	input = sys.stdin.read()
	data = input.split()
	a = data[1:]
	print(largest_number(a))


# Local Test
# a = list(input('a: ').split())
# print(largest_number(a))