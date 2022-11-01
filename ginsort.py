l, u, e, o = [],[],[], []
for i in sorted(input()):
	if i.isupper():
		u.append(i)
	elif i.islower():
		l.append(i)
	elif i.isdigit():
		if int(i)%2==0:
			e.append(i)
		else : o.append(i)

print(''.join(l+u+o+e))