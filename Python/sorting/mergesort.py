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
import sys

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
	if p < r:
		q = (p + r)//2
		mergeSort(array, p, q)
		mergeSort(array, q+1, r)
		mergeSort_merge(array, p, q, r)