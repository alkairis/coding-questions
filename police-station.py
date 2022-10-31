n, m = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort(reverse=True)
result = sum(lst[0:2])-2*m
print(result)
