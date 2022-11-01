no = int(input())
double, missing = [], []
for _ in range(no):
	inp = int(input())
	x = list(map(int, input().split()))
	for _ in range(1, inp+1):
		if(x.count(_) > 1):
			double.append(_)
		elif(_ not in x):
			missing.append(_)

for i in range(len(double)):
	print(f'{double[i]} {missing[i]}')
