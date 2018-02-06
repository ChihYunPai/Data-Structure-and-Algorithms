def test(a=[], b=0, c=len(a)):
	print(a[b], a[c])

a=[1,2,3,4]
test(a, b=1)
