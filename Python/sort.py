import sys

def bubbleSort(array):
	changed = True
	while changed:
		changed = False
		for i in range(len(array) - 1):
			if array[i] > array[i+1]:
				array[i], array[i+1] = array[i+1], array[i]
				changed = True

def selectionSort(array):
	for i in range(0, len(array)-1):
		min = i
		for j in range(i+1, len(array)):
			if array[j] < array[min]:
				min = j
		if min != i:
			array[i], array[min] = array[min], array[i]

def insertionSort(array):
	i = 1
	while i < len(array):
		j = i - 1
		while j >= 0 and array[j-1] > array[j]:
			array[j], array[j-1] = array[j-1], array[j]
			j -= 1
		i += 1

def mergeSort_merge(array, p, q, r):
	n1 = q - p + 1
	n2 = r - q
	L = [0]*n1
	R = [0]*n2
	for i in range(n1):
		L[0] = array[p + i -1]
	for j in range(n2):
		R[j] = array[q + j]
	L[n1 + 1] = sys.maxsize
	R[n2 + 1] = sys.maxsize
	i = j = 0
	for k in range(p-1, r):
		if L[i] <= R[j]:
			array[k] = L[i]
			i += 1
		else: # L[i] > R[j]
			array[k] = R[j]
			j += 1

def mergeSort(array):
	"""
	Merge Sort
	================================
	Time:
		Average Case:	O(n*log(n))
		Worst Case:   	O(n*log(n))
		Best Case:    	O(n*log(n))
	Space:
		Worst Case:   	O(n)
	================================
	"""
	if p < r:
		q = (p + r)//2
		mergeSort(array, p, q)
		mergeSort(array, q+1, r)
		mergeSort_merge(array, p, q, r)

def quickSort_partition(array, low, high):
	pivot = array[high]
	i = low - 1
	for j in range(low, high):
		if array[j] < pivot:
			i += 1
			array[i], array[j] = array[j], array[i]
	if array[high] < array[i+1]:
		array[i+1], array[high] = array[high], array[i+1]
	return (i+1)


def quickSort(array, low=0, high):
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
	if low < high:
		p = quickSort_partition(array, low, high)
		quickSort(array, low, p-1)
		quickSort(array, p+1, high)



def heapSort(array):
	return array

def becketSort(array):
	return array

def countingSort(array):
	return array

def radixSort(array):
	return array