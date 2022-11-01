from collections import Counter
list = [1,2,61,12,3,1,1,2,1,21,21,21,21,1,1,2]
list2 = [i for i in range(6)]
print(Counter(list))
c = Counter(list)
d = Counter(list2)
print()
print(c-d)
print(c+d)
print(c | d)
print(c & d)
print()
print(c.elements())
print(sorted(c.elements()))
