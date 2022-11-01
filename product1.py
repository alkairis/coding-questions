from itertools import product
length, mod = tuple(map(int, input().split()))
maxelm = []
for _ in range(length):
	numb, *lst = list(map(int, input().split()))
	maxelm.append(lst)

print(list(product(*maxelm)))
