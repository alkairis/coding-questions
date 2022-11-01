from itertools import product
length, mod = tuple(map(int, input().split()))
maxelm = []
for _ in range(length):
	numb, *lst = list(map(int, input().split()))
	maxelm.append(lst)
result = map(lambda x : sum(i**2 for i in x)%mod, product(*maxelm))
print(max(list(result)))
