from collections import OrderedDict
for _ in range(int(input())):
    N = int(input())
    dic = OrderedDict()
    for _ in range(N*3):
        prob, mark = input().split()
        dic[prob] = dic.get(prob, 0)+int(mark)
    print(*sorted(dic.values()))
    

'''
3
1
A 1
B 2
C 3
2
AA 1
AB 1
AB 1
AC 1
AC 1
AD 1
1
Z 100
Z 100
Z 100
'''