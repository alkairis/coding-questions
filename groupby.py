from itertools import groupby
print(*[(len(list(a)), int(b)) for b,a in groupby(input())])