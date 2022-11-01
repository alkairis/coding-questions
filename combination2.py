import itertools as iter

strlen = int(input())
string = list(map(str, input().split()))
index = int(input())
combinations = list(iter.combinations(string, index))

result = filter(lambda x : 'a' in x, combinations)
print(f'{len(list(result))/len(combinations):.3}')