"""
Bubble Sort
================================
Time:
	Average Case:	O(n ^ 2)
	Worst Case:   	O(n ^ 2)
	Best Case:    	O(n)
Space:
	Worst Case:   	O(1)
================================
"""
def bubbleSort(array):
	changed = True
	while changed:
		changed = False
		for i in range(len(array) - 1):
			if array[i] > array[i+1]:
				array[i], array[i+1] = array[i+1], array[i]
				changed = True