import numpy
x, y = input().split()
lst = []
for _ in range(int(x)):
	lst.append(list(map(int, input().split())))
arr = numpy.array(lst)
print(arr.transpose())
print(arr.flatten())