from collections import Counter

number, shoes, lst = int(input()), Counter(map(int, input().split())), []
income = 0
for i in range(int(input())):
    size, amount = map(int, input().split())
    if shoes[size]:
        income+=amount
        shoes[size]-=1

print(income)
