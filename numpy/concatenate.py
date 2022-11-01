from numpy import concatenate, array
m, n, p = map(int, input().split())
lst = []
a1 = array([input().split() for _ in range(m)], int)
a2 = array([input().split() for _ in range(n)], int)
print(concatenate((a1, a2)))