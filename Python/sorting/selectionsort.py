"""
Selection Sort
================================
Time:
	Average Case:	O(n^2)
	Worst Case:   	O(n^2)
	Best Case:    	O(n^2)
Space:
	Worst Case:   	O(1)
================================
"""
def selectionSort(array):
	for i in range(0, len(array)-1):
		min = i
		for j in range(i+1, len(array)):
			if array[j] < array[min]:
				min = j
		if min != i:
			array[i], array[min] = array[min], array[i]