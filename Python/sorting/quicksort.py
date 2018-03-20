"""
Quick Sort
================================
Time:
	Average Case:	O(n*log(n))
	Worst Case:		O(n^2)
	Best Case:		O(n*log(n))
Space:
	Worst Case:		O(n*log(n))
================================
"""
def partition(array, low, high):
	pivot = array[low]
	i = low
	j = high
	while True:
		while array[i] < pivot:
			i += 1
		while array[j] > pivot:
			j -= 1
		if i >= j:
			return j
		array[i], array[j] = array[j], array[i]


def quicksort(array, low, high):
	if low < high:
		pivot = partition(array, low, high)
		quicksort(array, low, pivot)
		quicksort(array, pivot + 1, high)


array = [9,8,7,6,5,4,3,2,1]
quicksort(array, 0, len(array)-1)
print(array)