customers = []
for _ in range(int(input())):
	customers.append(input())

customers, size = list(customers), len(customers)
dict_cust = []

for i in list(set(customers)):
	cust_count = customers.count(i)
	per = (cust_count/size)*100
	dict_cust.append(per)

output = []
new_dict = dict(zip(list(set(customers)), dict_cust))
for i,j in new_dict.items():
	if(j>5):
		output.append(i)
output.sort()
print(output)
