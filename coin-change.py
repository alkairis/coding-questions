lst = []
result = []

for i in range(int(input())):
    m = input()
    lst.append(list(map(int, input().split())))

for i in lst:
    result.append(max(i))
print(*result)
