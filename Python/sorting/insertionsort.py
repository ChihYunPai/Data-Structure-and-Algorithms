"""
Insertion Sort
================================
Time:
	Average Case:	O(n*log(n))
	Worst Case:   	O(n*log(n))
	Best Case:    	O(n*log(n))
Space:
	Worst Case:   	O(n)
================================
"""
def insertionSort(array):
	i = 1
	while i < len(array):
		j = i - 1
		while j >= 0 and array[j-1] > array[j]:
			array[j], array[j-1] = array[j-1], array[j]
			j -= 1
		i += 1