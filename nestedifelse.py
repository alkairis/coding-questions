x, lst, ans = int(input()), list(map(int, input().split())), bool
ans = False if not all(i > 0 for i in lst) else (True if any(i==int(str(i)[::-1]) for i in lst) else False)
print(ans)